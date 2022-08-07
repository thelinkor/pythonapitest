import os
import apisetup
import dataParsing
import signal
import sys
import subprocess
import time
from flask import Flask, request, json



app = apisetup.setup()

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/post_json', methods=['POST'])
def process_json():
    data = request.get_json()
    pathCheckTest = dataParsing.isValidPath(data)
    if not pathCheckTest[0]:
        return pathCheckTest[1], pathCheckTest[2]
    v = subprocess.check_output(getCommandArrayFromRequest(data))
    time.sleep(5)
    print(v)
    return v

def getCommandArrayFromRequest(data):
    out = ['ls']
    if 'path' in data:
        out = out + [data['path']]
    if 'arguments' in data:
        out = out + data['arguments']
    return out

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    app.run(port=5001)



