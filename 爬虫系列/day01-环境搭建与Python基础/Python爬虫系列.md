# Python爬虫系列

## Python爬虫环境搭建

1. 关于如何安装Python环境

   我建议大家用Anaconda环境来作为python的基础环境。具体安装方法，大家可以上网搜索一下，很简单。需要注意的是安装时记得添加环境变量（两个checkbox都要选。）另外，不要按错Python版本，我们现在用的是Python3的版本。

2. 创建属于爬虫的专属虚拟环境

   本专栏使用的是vscode开发工具，大家可以根据自己的爱好和习惯选择开发工具。

   - 在一个你熟悉的地方建一个工作空间，用来保存代码，看到好多朋友之前辛辛苦苦写好的代码，结果忘记保存到哪了。

   - 创建虚拟环境，应为Python3.7版本自带了虚拟机（venv），所以我们并不需要而外的安装其他的虚拟环境的库

     在代码保存位置的同级目录下创建一个叫做**env**的文件夹，然后允许如下命令开始创建。

     我的目录结构：

     ![WX20200229-193459](/Users/tango/Documents/专栏/截图/WX20200229-193459.png)

     进入env的目录下，执行如下命令注意**venv**和“.”之间有个空格：

     ```shell
     python -m venv .
     ```

     运行后的效果如下：

     ![WX20200229-194136](/Users/tango/Documents/专栏/截图/WX20200229-194136.png)

   - 激活虚拟环境

     ```shell
     source bin/activate
     ```

     > 注意我现在所在的目录仍是在env下。激活成功后，会在已有的命令行前面多一个口号

   - 退出虚拟环境

     ```shell
     deactivate
     ```

     ![WX20200229-195229](/Users/tango/Documents/专栏/截图/WX20200229-195229.png)

## 安装爬虫常用的包

我们先将在爬虫中常用的几个第三方库安装一下，其他的等用到的时候在安装。

- requests库

  ```shell
  pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  > 为了安装速度能快一点，我们使用了清华大学的镜像源（-i 后面的就是）

  ![WX20200229-200127](/Users/tango/Documents/专栏/截图/WX20200229-200127.png)

- bs4（BeautifulSoup）

  ```shell
  pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  ![WX20200229-200221](/Users/tango/Documents/专栏/截图/WX20200229-200221.png)

## Python基础语法快速复习

