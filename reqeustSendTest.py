from flask import request, Flask, json
import requests

def handleRequestOutput(out):
    print(out.content, "\n\n")

##Normal Post
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'path':'c:\\', 'arguments':['-l', '--all']} ))

##404 error post
handleRequestOutput(
requests.post('http://127.0.0.1:5001/blah',json={'command':'ls'} ))

##No Path
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'bath':'c:\\abcd\\', 'arguments':['-l', '--all']} ))

##Bad Path
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'path':'c:\\abcd\\', 'arguments':['-l', '--all']} ))
