###################################
#
# Contains the main setup for the server through the Flask Api
#

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

#
# Quite hacky way to achieve gracefull shutdown.
# Keep track fo number of in and out processes and dont exit until we are equal here.
#
inCount = 0
outCount = 0
# keeps track if we are supposed to not accept any new requests.
hasExited = False

@app.route('/post_json', methods=['POST'])
def process_json():
    if hasExited:
        return ("System is shutting down.", 503)
    global inCount
    global outCount

    inCount = inCount +1
    data = request.get_json()
    inputCheckTest = dataParsing.inputValidation(data)
    if not inputCheckTest[0]:
        outCount = outCount +1
        return inputCheckTest[1], inputCheckTest[2]

    v = subprocess.check_output(getCommandArrayFromRequest(data))
    time.sleep(5)

    outCount = outCount +1
    return v

# Parsing  input json into command
def getCommandArrayFromRequest(data):
    out = ['ls']
    if 'path' in data:
        out = out + [data['path']]
    if 'arguments' in data:
        out = out + data['arguments']
    return out

# Here is where we should handle the graceful shutdown.
def signal_handler(sig, frame):
    print('You pressed Ctrl+C.\nShutting down...')
    global hasExited
    hasExited = True
    global inCount
    global outCount
    while inCount > outCount:
        print('Waiting for process ...')
        time.sleep(1)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    app.run(port=5001, threaded = True)



