import os
import apisetup
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
    v = subprocess.check_output(getCommandArrayFromRequest(data))
    time.sleep(5)
    print(v)
    return v

def getCommandArrayFromRequest(data):
    out = ['ls']
    if 'path' in data.keys():
        out = out + [data['path']]
    if 'arguments' in data.keys():
        out = out + data['arguments']
    return out

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')

if __name__ == "__main__":
    app.run()



