from flask import Flask, render_template, request, abort, Response, redirect, jsonify, send_from_directory
import os
import logging
app = Flask(__name__, static_folder='/')
logging.basicConfig(level=logging.INFO)

@app.route('/hello')
def index():
    return "Hi"

#port = int(os.environ.get("PORT", 5000))
port = 8000
app.run(host='0.0.0.0', port=port)
