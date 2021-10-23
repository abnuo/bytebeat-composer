from flask import Flask, render_template, request, abort, Response, redirect, jsonify, send_from_directory, url_for
import os
import time
import json
import sqlite3
import logging
app = Flask(__name__, static_folder='/')
logging.basicConfig(level=logging.INFO)

def getBytebeat2(id):
    #if request.args.get('e', default=None) != None:
    #id = int(request.args.get('id', default="1"))
    #title = request.args.get('t', default="Untitled song")
    con = sqlite3.connect('bytebeats.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM bytebeats WHERE id = '" + str(id) + "'")
    returnId = cur.fetchall()
    cur.close()
    jsons = {"id": returnId[0][0], "title": returnId[0][1], "base64": returnId[0][2]}
    return jsons

@app.route('/')
def index():
    #b64 = getBytebeat(int(id))
    return open("index.html").read()
    #return id

@app.route('/bytebeat/<id>')
def redirect(id):
    bb = getBytebeat2(int(id))
    #return "Redirecting..."
    #return open("index.html").read()
    #time.sleep(1)
    return "<script>window.location.href = \"" + "/#" + bb["base64"] + "\";</script>"

@app.route('/add')
def addBytebeat():
    #if request.args.get('e', default=None) != None:
    exprC = request.args.get('e', default="v3b64q1ZKzk9JVbJS0ijRKtE3NTCwszNVAzE0lWoB")
    title = request.args.get('t', default="Untitled song")
    con = sqlite3.connect('bytebeats.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM bytebeats ORDER BY id DESC LIMIT 1;")
    #id = cur.rowcount + 1
    try:
      id = int(cur.fetchall()[0][0]) + 1
    except Exception as e:
      id = 1
    cur.execute("INSERT INTO bytebeats VALUES (?,?,?)", (id, title, exprC))
    con.commit()
    cur.close()
    return {"id": id}

@app.route('/get')
def getBytebeat():
    #if request.args.get('e', default=None) != None:
    id = int(request.args.get('id', default="1"))
    #title = request.args.get('t', default="Untitled song")
    con = sqlite3.connect('bytebeats.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM bytebeats WHERE id = '" + str(id) + "'")
    returnId = cur.fetchall()
    cur.close()
    jsons = {"id": returnId[0][0], "title": returnId[0][1], "base64": returnId[0][2]}
    return jsons

#port = int(os.environ.get("PORT", 5000))
port = 8000
app.run(host='0.0.0.0', port=port)
