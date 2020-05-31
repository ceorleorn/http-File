import os
import time
import requests


host = input('连接地址:')

class ServerHttp():
    def contect(self,host):
        self.host = host
        self.firstrequeststime = time.time()
        self.rp = requests.get(host + '/contect')
        self.secondrequeststime = time.time()
        self.contectTicktime = self.secondrequeststime - self.firstrequeststime
        if self.rp.status_code == 200:
            print('连接服务器成功....')
            print('请求耗时(毫秒):' + str(self.contectTicktime))
            print('信息:')
            print('服务器名称:' + dict(eval(self.rp.text))['serverName'])
            print('服务器地址:' + self.host)
        else:
            print('连接服务器错误')
            print('Http' + str(self.rp.status_code))
            print('请求耗时(毫秒):' + str(self.contectTicktime))
    def getFile(self,src):
        self.rp = requests.post(host + '/getFile',data=['path':src])
        if self.rp.status_code == 200:
            if dict(eval(self.rp.text))['state'] == 200:
                if dict(eval(self.rp.text))['filetype'] == 'file':
                    print('为文件类型')
                    with open('./save/' + host + '/' + src,'wb+') as f:
                        f.write(dict(eval(self.rp.text))['text'])
                    print('保存在' + os.getcwd() + '/save/' + host + '/' + src)
                else:
                    print('为文件夹类型')
                    print('索引如下:')
                    for i in dict(eval(self.rp.status_code))['list']:
                        print('Src :'+ src + '/' + i)
                    print('开始依次下载......')
                    for i in dict(eval(self.rp.status_code))['list']:
                        self.getFile(self,src + '/' + i)
            else:
                print('在服务器中找不到:' + src)
        else:
            print('连接服务器错误')
            print('Http' + str(self.rp.status_code))

s = ServerHttp()
s.contect()
while True:
    requests_src = input('输入目标文件在服务器上请求:')
    s.getFile(requests_src)
    print('请求结束.......')
