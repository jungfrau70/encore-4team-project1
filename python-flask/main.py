# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 08:49:23 2020

@author: OHyic
"""

#import flasks libraries
from flask import Flask, render_template, request, jsonify, url_for, redirect, flash, Response, send_file
from flask_socketio import SocketIO, emit
import webbrowser
from threading import Timer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, port=5000, host='0.0.0.0', debug=True)
    
# if __name__ == '__main__':
#     Timer(1,lambda: webbrowser.open_new("http://0.0.0.0:5000/")).start()
#     socketio.run(app)
    
    
    