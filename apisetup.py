from flask import Flask, request, json

def page_not_found(e):
    return "The request was sent to a page which does not exist", 404

def setup():
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    return app
    
