Title: 记一次 zsh 产生僵尸进程解决
Category: Linux
Tags: zsh, zombie, 僵尸, 进程, 阻塞, 命令
Date: 2014-03-21 10:47

## 问题描述
今天使用 vmplayer 运行了 xp 系统, 关闭后在 zsh 里继续敲命令就阻塞了,
然后就关闭了终端重新打开, 还是阻塞, 重复几次依然如此. 然后使用 gVim
将 shell 切换到 bash, 终端可以正常打开, 然后运行
```bash
$ ps aux | grep zsh
wh       27552  0.0  0.1  47244  5164 ?        Ss   09:38   0:00 zsh
wh       27553  0.0  0.1  47244  5156 ?        Ss   09:38   0:00 zsh
wh       27600  0.0  0.0  47348  3492 ?        D    09:38   0:00 zsh
wh       27609  0.0  0.0  47348  3488 ?        D    09:38   0:00 zsh
wh       27614  0.0  0.0  47348  3484 ?        D    09:38   0:00 zsh
wh       27697  0.0  0.1  47248  5172 ?        Ss   09:39   0:00 -/bin/zsh
wh       27718  0.0  0.0  47356  3496 ?        D    09:39   0:00 -/bin/zsh
root     28040  0.0  0.0  36640  2812 tty2     Ss+  09:40   0:00 -zsh
wh       28628  0.0  0.0  47356  3492 ?        D    09:42   0:00 -/bin/zsh
```
发现好多僵尸进程, 而且都 kill 不掉.

## 解决
首先当然是 `strace` 登场
```bash
$ strace zsh
...
pipe([3, 4])                            = 0
fcntl(3, F_DUPFD, 10)                   = 11
close(3)                                = 0
fcntl(4, F_DUPFD, 10)                   = 12
close(4)                                = 0
rt_sigprocmask(SIG_BLOCK, [CHLD], [CHLD WINCH], 8) = 0
clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7fd94caef9d0) = 8750
close(12)                               = 0
fcntl(11, F_GETFL)                      = 0 (flags O_RDONLY)
fstat(11, {st_mode=S_IFIFO|0600, st_size=0, ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fd94caf3000
lseek(11, 0, SEEK_CUR)                  = -1 ESPIPE (Illegal seek)
read(11,
```
然后就会卡在上面那个状态一会, 继续运行, 这段的完整结果为
```
pipe([3, 4])                            = 0
fcntl(3, F_DUPFD, 10)                   = 11
close(3)                                = 0
fcntl(4, F_DUPFD, 10)                   = 12
close(4)                                = 0
rt_sigprocmask(SIG_BLOCK, [CHLD], [CHLD WINCH], 8) = 0
clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7fd94caef9d0) = 8750
close(12)                               = 0
fcntl(11, F_GETFL)                      = 0 (flags O_RDONLY)
fstat(11, {st_mode=S_IFIFO|0600, st_size=0, ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fd94caf3000
lseek(11, 0, SEEK_CUR)                  = -1 ESPIPE (Illegal seek)
read(11, "/data/home/wh\n", 4096)       = 14
read(11, "", 4096)                      = 0
close(11)  
```
从上面可以看出, zsh 打开了一个 pipe, 但是读取的时候阻塞了.

此时我无意中敲了下 `df -h` 发现也很慢, 当然 strace 下 它
```bash
$ strace df -h
...
stat("/mnt", 
```
发现它是卡在了读取 `/mnt`. 尝试 `umount` 它:
```bash
$ sudo umount /mnt
umount: /mnt: target is busy
        (In some cases useful info about processes that
         use the device is found by lsof(8) or fuser(1).)
```
说是被某个程序使用, 现在该 `lsof` 登场了
```bash
$ lsof /mnt
lsof /mnt
lsof: WARNING: can't stat() cifs file system /mnt
      Output information may be incomplete.
lsof: status error on /mnt: Host is down
```
好吧, 看到这里我就想明白了, 因为开虚拟机的时候我挂载了虚拟机里的一个共享目录
```bash
$ sudo mount -t cifs -o guest //ip.of.host/share /mnt
```
在虚拟机关闭之后没有卸载, 导致在对这个目录 `stat` 的时候会有一个网络超时时间.

然后就卸载它
```bash
$ umount -a -t cifs -l /mnt
```

## 检测
现在打开 zsh 也不阻塞了, `df -h` 也同样不阻塞了. 上面 Ss 的进程可以用 -9 杀掉,
但是僵尸(D) 进程无法杀掉.

## 疑惑
为什么 zsh 创建一个 pipe 会涉及到挂载的文件系统呢? 对于这点很疑惑.

## 参考
* lsof: [http://stackoverflow.com/questions/74626/how-do-you-force-a-cifs-connection-to-unmount](http://www.ibm.com/developerworks/cn/aix/library/au-lsof.html)
* 卸载 cifs: [http://stackoverflow.com/questions/74626/how-do-you-force-a-cifs-connection-to-unmount](http://stackoverflow.com/questions/74626/how-do-you-force-a-cifs-connection-to-unmount)
