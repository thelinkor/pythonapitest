import os
import apisetup
import signal
import sys
import subprocess
import time


app  = apisetup.setup()

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/post_json', methods=['POST'])
def process_json():
    c = request.headers.get('Contet-Type')
    data = request.get_json()
    #data = json.loads(request.data)
    v =subprocess.check_output([data['command'], '-l'])
    time.sleep(5)
    print(v)
    return v
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        return json
    else:
        return 'Content-Type not supported!'

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')

if __name__ == "__main__":
    app.run()



