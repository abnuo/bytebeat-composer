from flask import Flask, render_template, request, abort, Response, redirect, jsonify, send_from_directory
import os
import sqlite3
import logging
app = Flask(__name__, static_folder='/')
logging.basicConfig(level=logging.INFO)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/add')
def addBytebeat():
    #if request.args.get('e', default=None) != None:
    exprC = request.args.get('e', default="v3b64q1ZKzk9JVbJS0ijRKtE3NTCwszNVAzE0lWoB")
    title = request.args.get('t', default="Untitled song")
    con = sqlite3.connect('bytebeats.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM bytebeats ORDER BY id DESC LIMIT 1;")
    #id = cur.rowcount + 1
    id = cur.fetchall()[0][0] + 1
    cur.execute("INSERT INTO bytebeats VALUES (?,?,?)", (id, title, exprC))
    con.commit()
    cur.close()
    return str(id)

@app.route('/get')
def getBytebeat():
    #if request.args.get('e', default=None) != None:
    id = int(request.args.get('id', default="1"))
    #title = request.args.get('t', default="Untitled song")
    con = sqlite3.connect('bytebeats.db')
    cur = con.cursor()
    #cur.execute("INSERT INTO bytebeats VALUES (?,?)", (title, exprC))
    cur.close()
    return "Hi"

#port = int(os.environ.get("PORT", 5000))
port = 8000
app.run(host='0.0.0.0', port=port)
