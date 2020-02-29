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

1. Python是用缩进（四个空格）来控制代码层级关系的。这点很重要。所以写在了最前面。

2. 基本数据类型

   - Number（数值）

     - int （有符号整数）。比如：10， -10， 0等
     - float（浮点型）。就是我们常说的小数。比如：0.5，3.14等
     - complex（复数）。由实数和虚数两部分构成，形式为a + bj。由于爬虫用到的比较少，这里只需要知道一下就好。

   - String（字符串）

     字符串是用来表示文本的数据类型。比如：name = "路飞"

     - 提取字符

       ```python
       name = "路飞"
       name[0] # 这个将返回‘路’
       ```

     - 字符串切片

       ```python
  word = "人生苦短，我用Python"
       # 需要将苦短提取出来
       word[2:4]
       ```
     
       > 注意切片是包含左边，不包含右边的数值。

       也可以从右边数

       ```python
# 提取Python
       word[-6:]
  ```
       
       
     
     - 拼接， 直接用加号就可以将多个字符串拼接在一起

       ```python
  name = "路飞"
       word = "人生苦短，我用Python"
  name + word
       ```
     
     - 格式化字符串。有的时候我们的字符串中某个内容需要变动，这个时候就可以私用format()函数了。
     
       ```python
  name = "路飞"
       msg = "你好啊，{}".format(name)
  ```
     
  > 更多的用法，我们在实际代码中再为大家介绍。
     
   - List（列表）
   
     python中用 [ ] 来表示列表

     ```python
  name_list = ['路飞', '索隆', '娜美']
     ```

   - Dictionary（字典）

     字典是值包含由键和值组成的数据集合

     ```python
     info = {'name':'路飞', 'age':18}
     ```

     > 要注意的是键不可以重复，而值是可以的。

   - Tuple（元组）

     它和列表很相似，用（）来表示。但是它一旦船家女之后就不能修改了。
   
     ```python
  t = ('a', 'b')
     ```

3. 函数

   - 函数的定义方式

     ```python
     def getInfo():
         print("这是一个函数")
     ```

     > 我们可以通过def 加我们的函数名，来创建函数。

   - 函数的调用

     ```python
     def getInfo():
         print("这是一个函数")
     getInfo()
     ```

   - 全局变量

     ```python
     a = 0
     name = "路飞"
     def change():
         a = 1
         name = "路飞1"
     
     def change2():
         global a
         global name
         a = 1
         name = "路飞1"
     
     change()
     print(name) # 没有添加global 返回 路飞
     print(a) # 没有添加global 返回 0
     change2()
     print(name) # 添加global 返回 路飞1
     print(a) # 添加global 返回 1
     ```

     函数内是可以调用全局变量的，但是如果要修改那么就要加上global关键字。

     

   - 参数

     函数是可以接收参数的

     ```python
   def print_name(name):
         print(name)
     
     print_name("路飞")
     ```
     
     这里的name就是参数，通常我们叫它“形参”，而“路飞”通常称为实参。

4. 条件判断与循环

   - 判断

     ```python
     a = 10
     if a < 10:
         print("a < 10")
     elif a < 5:
         print("a < 5")
     else:
         print("有点太小了")
     ```

     if 后面接的是表达式，为真的时候就会执行该语句的代码。如果为假的时候就会执行elif的判断或者else后面的判断。

   - 循环

     - for 循环

       我们前面知道Python中有列表，那么我如果想变量列表中的所有元素该怎么操作呢?

       ```python
     name_list = ["路飞", "娜美", "乔巴"]
       for name in name_list:
         print(name)
       ```

       ![WX20200229-222212](/Users/tango/Documents/专栏/截图/WX20200229-222212.png)

       我们看到，列表里面的名字依次被打印了出来

     - while循环

       我们想让程序从从1开始数，数到10停止。

       ```python
     i = 10
       while i > 0:
         print(i)
           i -= 1
     ```
       
       ![WX20200229-222502](/Users/tango/Documents/专栏/截图/WX20200229-222502.png)
       
       while后面接的也是表达式，当条件满足时就会执行。
       
       > 注意一定是一个可以结束的表达式，否则会进入死循环。这里的 i -= 1，就是为了让i 每次都减1，这样当i 小于0的时候就不会再执行了。
       
       - 我们用break可以提前结束循环
       - 用continue可以跳过某次循环，具体用法我们再后面的爬虫项目中会和大家慢慢介绍。

5. 类

   这个概念比较抽象，简单的说就是用代码来描述一类事物。比如狗，猫，车这些。

   在python中我们可以用class关键字来定义一个类

   ```python
   class Car():
       '''
       这是一个车的类
       '''
   ```

## 最后

我们这里只是简单的介绍了一下在爬虫中要用到的Python技术。由于篇幅的原因未能给大家讲的很细，希望大家见谅。读者可以关注本公众号获取更多关于的Python基础的文章。

然我讲知识点放到实际爬虫项目中。欢迎大家跟着Tango继续后面的爬虫相关的内容。我们下周见。