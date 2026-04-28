# -*- coding: utf-8 -*-
# 创建时间：2026/04/22
# 作者：fizo
# python学习记录

# 第一节 安装python和虚拟环境

# 1.Windows安装python,首先从官网https://www.python.org/下载安装，安装完成后，打开cmd命令行，输入python --version，显示Python 3.14.4，则安装成功。
# 2.Linux版本安装python：sudo apt-get install python3，打开终端，输入python3 --version，显示Python 3.14.4，则安装成功。

# 创建虚拟环境，可以创建多个虚拟环境，每个环境可以安装不同的模块，每个环境可以运行不同的程序，每个环境可以保存不同的数据，每个环境可以保存不同的配置文件，每个环境可以保存不同的日志文件，每个环境可以保存不同的缓存文件。
# 1.创建虚拟环境：python3 -m venv .myenv(自定义名字)，激活虚拟环境：source .myenv/bin/activate(linux)。
# 2.激活虚拟环境：.myenv/Scripts/Activate(windows)，组策略：查看：Get-ExecutionPolicy，显示：Restricted表示受限，永久启动：Set-ExecutionPolicy RemoteSigned -Scope CurrentUser。
# 3.临时启动：Set-ExecutionPolicy RemoteSigned -Scope Process，当前窗口有效，关闭失效。

# 模块的作用，模块是python的扩展，可以扩展python的功能，如：数据库连接，网络内容抓取，数据处理，数据可视化，数据可视化等等。
# 1.在终端进入虚拟环境进行安装模块，不进入虚拟环境进行安装模块，则安装到全局环境。
# 2.安装模块：pip3 install 模块名字
# 3.升级模块：pip3 install --upgrade 模块名字

# 第二节 安装vscode或者pycharm及插件
# vscode安装：
# 1.Windows版本官网下载安装：https://code.visualstudio.com/Download，选择windows版本，下载安装文件，双击安装文件，安装完成。
# 2.linux版本官网下载安装：https://code.visualstudio.com/Download，选择linux版本，下载安装文件，运行命令：sudo apt install ./<file>.deb，安装完成。
# 
# pyycharm安装：
# 1.Windows版本官网下载安装：https://www.jetbrains.com/pycharm/download/#section=windows，下载安装文件，双击安装文件，安装完成。
# 2.linux版本官网下载安装：https://www.jetbrains.com/pycharm/download/#section=linux，下载安装文件，运行命令：tar -xzf pycharm-*.tar.gz -C /opt/，安装完成。
# 3.Linux版本终端安装，运行命令：sudo apt-get install pycharm-community，运行命令：pycharm，打开pycharm。
# 
# 插件安装，Windows和Linux版本安装方式一样，在插件搜索框中输入插件名称，点击安装。
# 1.翻译插件：Windows推荐：豆包桌面版开启AI划词工具栏选词翻译，pychram推荐安装：translator。
# 2.通义灵码，可自动补全代码，搜索lingma进行安装，或者在官方网https://lingma.aliyun.com/lingma/download下载离线版，打开pycharm，点击从磁盘安装插件。
# 2.通义灵码登录，点击登录，按提示扫描二维码，登录。或者输入邮箱、手机号码和密码，登录。

# jupyter notebook 安装，Windows和Linux版本安装方式一样：
# 1.在终端中运行命令：pip3 install jupyter，安装完成。
# 2.在终端中运行命令：jupyter notebook，打开浏览器，输入http://localhost:8888，打开jupyter notebook。
# 3.在终端中运行命令：pip3 install jupyterlab-language-pack-zh-CN，安装中文语言包。

# 注意：本教程默认使用windows系统，使用vscode开发，jupyter notebook进行数据可视化，linux系统或者使用pycharm，请自行研究安装。