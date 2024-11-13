# Speedybee—自动化测试


### 一、简要框架介绍
```
Approach：通用方法使用
Element：元素
Result：测试报告
test_case：测试用例
```
---
### 二、Github拉取项目代码
```
远程仓库：git remote add origin https://github.com/luo-wj-ai/SpeedybeeApp.git
重命名master分支：git branch -M main
将本地的"main"分支推送到远程仓库"origin"：git push -u origin main

#push代码
git add .
git commit -m "这里面是你需要写的内容"
git push

#pull拉取代码
git pull

#分支
建立分支：git branch iOS
切换分支：git checkout iOS
合并分支：git merge iOS
删除分支：git branch -d iOS
```
---
### 三、运行项目
1. 命令行： python -m unittest -v yourfile.py
2. 参考：https://www.cnblogs.com/youreyebows/p/7867508.html
---
### 参考网址
1. gitub项目源代码：[luo的gitub](https://github.com/luo-wj-ai/SpeedybeeApp)
2. CSDN博客参考
   3. [luo的Android](https://blog.csdn.net/Luoweijie42/article/details/140212378?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22140212378%22%2C%22source%22%3A%22Luoweijie42%22%7D)
   4. [luo的iOS](https://blog.csdn.net/Luoweijie42/article/details/140344444)
3.xpath基础概念：[菜鸟教程](https://www.runoob.com/xpath/xpath-syntax.html)
4.基础unittest教学视频：[哔哩哔哩](【2023最新UnitTest自动化测试框架和unittest数据驱动实战讲解】https://www.bilibili.com/video/BV1AT41167wv?p=5&vd_source=f1420afe1b941d0191a7f686b3a2f85c)