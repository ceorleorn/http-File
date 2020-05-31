from flask import *
import os
import time

print('')
print('作者是越努力越幸运，遵守LICENSE哈')
print('链接：https://github.com/snbck/http-file')

Serverconfig = {'serverName': 'DemoServer',
                'serverfile': './demofile', 'serverport': 1301}


app = Flask(__name__)


@app.route('/contect', methods=['GET'])
def ServerContect():
    return Serverconfig['serverName']

@app.route('/getFile',methods=['POST'])
def ServerGetFile():
    if os.path.exists(Serverconfig['serverfile'] + '/' + request.form['path']):
        if os.path.isdir(Serverconfig['serverfile'] + '/' + request.form['path']):
            return str({'state':200,'filetype':'dir','list':os.listdir(Serverconfig['serverfile'] + '/' + request.form['path'])})
        else:
            with open(Serverconfig['serverfile'] + '/' + request.form['path'],'rb') as f:
                return str({'state':200,'filetype':'file','text':f.read()})
    else:
        return str({'state':404})


app.run(port=Serverconfig['serverport'])
