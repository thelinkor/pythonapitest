###################
#
# Manual tests.
# Run the main script first and then run this method to get different errors and outputs
# 
#

from flask import request, Flask, json
import requests

def handleRequestOutput(out):
    print(out.content.decode('UTF-8'), "\n\n")

ipAdress = 'http://127.0.0.1:5001/'
defaultPostPath = 'post_json'

##Normal Post
handleRequestOutput(
requests.post(ipAdress+ defaultPostPath,json={'path':'c:\\', 'arguments':['-l', '--all']} ))

##404 error post
handleRequestOutput(
requests.post('http://127.0.0.1:5001/blah',json={'command':'ls'} ))

##No Path
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'bath':'c:\\', 'arguments':['-l', '--all']} ))

##Bad Path
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'path':'c:\\abcd\\', 'arguments':['-l', '--all']} ))

##No ListOnArgumentPosition
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'path':'c:\\', 'arguments':'-l'} ))

##Invalid Argument on input
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'path':'c:\\', 'arguments':['--color','-l & cd ..']} ))

##Normal Post NoArguments
handleRequestOutput(
requests.post('http://127.0.0.1:5001/post_json',json={'path':'c:\\'} ))

