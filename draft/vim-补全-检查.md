Title: Vim 补全和代码检查: YouCompleteMe & syntastic
Date: 2013-08-14
Category: Vim
Tags: Vim, 补全, 7.4, 升级, 代码检查, YouCompleteMe, syntastic


Vim 7.4 发布, 最近升级了Vim, 并安装了YouCompleteMe和Syntastic插件, 这里记录下过程

## 升级Vim
YouCompleteMe 需要Vim 7.3.584+的支持, 并且开启 +python , 可以通过`:version`查看
升级Vim需要先卸载原有的Vim
```bash
sudo apt-get remove vim vim-tiny vim-common vim-runtime gvim vim-gui-common
```
并安装以下依赖
```basoh
sudo apt-get install libncurses5-dev libgnome2-dev libgnomeui-dev \
    libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
    libcairo2-dev libx11-dev libxpm-dev libxt-dev \
    python-dev ruby-dev mercurial checkinstall
```

下载最新的Vim源码, 这里从代码仓库获取(需要`hg`没有自行安装)
```bash
hg clone https://vim.googlecode.com/hg/ vim
```

然后进入目录编译安装Vim
```bash
cd vim
./configure --with-features=huge \
            --enable-rubyinterp=yes \
            --enable-pythoninterp=yes \
            --enable-python3interp=yes \
            --enable-perlinterp=yes \
            --enable-luainterp = yes \
            --enable-gui=gtk2 --enable-cscope --prefix=/usr
make VIMRUNTIMEDIR=/usr/share/vim/vim74
sudo checkinstall
```

## 安装llvm
如果想是想C系语言的补全, 需要libclang 3.2以上的版本, Ubuntu 12.10 自带的是3.0, 所以先安装LLVM, 可以下载二进制文件/编译安装

#### 下载二进制
到[llvm.org](http://llvm.org/releases/download.html#3.3)上下载相应的版本解压到~/ycm_temp

#### 编译
下载(clang)[http://llvm.org/releases/3.3/cfe-3.3.src.tar.gz]和[llvm](http://llvm.org/releases/3.3/llvm-3.3.src.tar.gz), 解压llvm
```bash
mkdir ~/ycm_temp
cd ~/ycm_temp
tar -zxvf llvm-3.3.src.tar.gz -C llvm.src
```

解压 clang到llvm.src/tools
```bash
tar -zxvf cfe-3.3.src.tar.gz -C ~/ycm_temp/llvm.src/tools/
mv ~/ycm_temp/llvm.src/tools/cfe-3.3.src ~/ycm_temp/llvm/tools/clang
```
编译llvm会自动编译clang
```bash
cd ~/ycm_temp
mkdir llvm_build
cd llvm_build
cmake ../llvm.src/CMakeList.txt ../llvm.src
make
```

## 安装YouCompleteMe
使用Vundle安装YouComplete(猛击[这里](/vimpei-zhi-xi-lie-cha-jian-guan-li.html)了解Vundle)

### 编译ycm_core
```bash
mkdir ~/ycm_build
cd ~/ycm_build
cmake -G "Unix Makefiles"  ~/.vim/bundle/YouCompleteMe/cpp -DEXTERNAL_LIBCLANG_PATH=~/ycm_temp/llvm.src/lib/libclang.so 
make ycm_core
```
下载llvm二进制的可以参考
```bash
cmake -G "Unix Makefiles"  ~/.vim/bundle/YouCompleteMe/cpp -DEXTERNAL_LIBCLANG_PATH=~/ycm_temp/llvm_root_path/lib/libclang.so
```
