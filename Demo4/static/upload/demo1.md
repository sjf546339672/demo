### 读取日志

从命令行获取一个参数，该参数表示【待读取文件的完整路径】

要求：开始运行后，如果文件有新的内容行，检测内容行中如果带有【quit】(无论大小写)则将其输出并退出程序运行，否则原样输出即可。

例如：
``` python
# python check_log_output.py /tmp/demo.log
这是一条新内容
这是一条新内容
这是一条新内容
exit
#
```

### 读取日志并将其内容重定向

从命令行获取两个参数，参数1表示【带读取文件的完整路径】，参数2表示【保存输出的新文件】

要求：开始运行后，如果参数1文件有新的内容，将其写入到参数2的文件中，如果超过30s没有内容写入，将参数2的文件对象关闭，并且推出程序运行

例如：
```
# python redirect_log_output.py /tmp/demo.log /tmp/demo_redirect.log
这是一条新内容
这是一条新内容
这是一条新内容
超过20s未读取到新内容，退出运行...
#
# cat /tmp/demo_redirect.log
这是一条新内容
这是一条新内容
这是一条新内容
#
```