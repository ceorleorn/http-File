from flask import *
import os
import time

Serverconfig = []
Serverconfig['serverName'] = 'DemoServer'
Serverconfig['serverfile'] = './demofile'
Serverconfig['serverport'] = 1301


app = Flask(__name__)


@app.route('contect', methods=['GET'])
def ServerContect():
    return str(['serverName':Serverconfig['serverName'], 'contectTime':str(time.time())])


@app.route('getFile', methods=['POST'])
def ServerGetFile():
    if os.path.exists(Serverconfig['serverfile'] + request.form['path'])
       if os.path.isfile(Serverconfig['serverfile'] + request.form['path']):
            return str(['state':200, 'filetype':'dir', 'list':os.listdir(Serverconfig['serverfile'] + request.form['path'])])
        else:
            with open(Serverconfig['serverfile'] + request.form['path'], 'rb') as f:
                return str(['state':200, 'filetype':'file','text':f.read()])
    else:
        return str(['state':404])


app.run(port=Serverconfig['serverport'])
