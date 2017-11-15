#-*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, request, render_template
import googleFunc

app = Flask(__name__)

import json
from pprint import pprint

with open('data/test_data.json') as data_file:    
    data = json.load(data_file)

memo_arr = data
for i in range(0,len(memo_arr)):
    googleFunc.entity_sentiment_text(memo_arr[i]["content"])
    googleFunc.sentiment_analysis_3args(memo_arr, i, memo_arr[i]["content"])

@app.route("/")
def memo():
    return redirect(url_for("memo_list"))

@app.route("/memo_list")
def memo_list():
    return render_template('memo_list.html', memo_arr = memo_arr, memo_len=len(memo_arr))

@app.route("/memo_reg")
def memo_reg():
    return render_template('memo_reg.html')

@app.route("/memo_read")
def memo_read():
    mtime = request.args.get("time")
    memo_ = None
    for m in memo_arr:
        if mtime == m['time']:
            memo_ = m
            break
    return render_template('memo_read.html', memo=memo_)

@app.route("/memo_reg_act", methods = ['POST'])
def memo_reg_act():
    global memo_arr

    mtitle = request.form['title']
    mcontent = request.form['content']
    
    import time
    mtime = str(time.time())

    senti = googleFunc.sentiment_analysis_1arg(mcontent)

    memo = {"title":mtitle, "content":mcontent, "time":mtime, "sentiment":senti}
    memo_arr = memo_arr +[memo]
    return redirect(url_for('memo_list'))

@app.route("/hi")
def hi():
    return "안녕!!!!"

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

app.run(debug=True, port=4000)