# 使用
### 运行server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:1301/ (Press CTRL+C to quit)
### 配置server.py
##### 找到server.py的第九行

```python
Serverconfig = {'serverName': 'DemoServer',
                'serverfile': './demofile', 'serverport': 1301}
```
* serverName参数是客户端连接后显示的名称
* serverfile是服务器中可下载文件的路径
* serverport是服务器http协议开启的端口

### 启动client.py并连接
*连接地址:*
##### 如果在本地运行的话直接输入http://127.0.0.1:1301
*连接地址:http://127.0.0.1:1301
连接服务器成功....
请求耗时(毫秒):0.023987293243408203
信息:
服务器名称:DemoServer
服务器地址:http://127.0.0.1:1301
输入目标文件或文件夹:*
此时就可以下载demofile里的东西了，也可以在server.py中替换成别的文件夹
例如输入csdn.png，或者直接输入"/"下载整个demofile文件夹
目前可以正常下载中文，图片等文件
``` markdown
*为文件夹类型
索引如下:
路径 ://csdn.png
路径 ://demodir
路径 ://demofile.py
开始依次下载......

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////csdn.png
为文件夹类型
索引如下:
路径 ://demodir/demo
路径 ://demodir/demo1.py
路径 ://demodir/demo2.py
开始依次下载......
为文件夹类型
索引如下:
路径 ://demodir/demo/demo2d1.py
开始依次下载......

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demodir/demo/demo2d1.py

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demodir/demo1.py

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demodir/demo2.py

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demofile.py
请求结束.......
输入目标文件或文件夹:/
为文件夹类型
索引如下:
路径 ://csdn.png
路径 ://demodir
路径 ://demofile.py
开始依次下载......

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////csdn.png
为文件夹类型
索引如下:
路径 ://demodir/demo
路径 ://demodir/demo1.py
路径 ://demodir/demo2.py
开始依次下载......
为文件夹类型
索引如下:
路径 ://demodir/demo/demo2d1.py
开始依次下载......

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demodir/demo/demo2d1.py

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demodir/demo1.py

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demodir/demo2.py

------------------
为文件类型
保存在C:\Users\Administrator\http-File/save////demofile.py
请求结束.......
```

### 作者的话
##### 作者才上五年级（现在已经六年级啦！！！）哈,如果有语法不简洁或者做的不好的地方请谅解.
##### 但如果觉得做得不错的话给个Star或者Fork支持一下吧！
#### (*^▽^*)



