from app import app
from flask import request, jsonify
from pythainlp import word_tokenize, collate, romanize
import json
import os

@app.route("/",methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        data_show = {'count': [], 'word': []}
        q = request.form['q']
        list_word = word_tokenize(q, keep_whitespace=False)
        count_number = len(list_word)
        data_show['count'].append(count_number)
        data_show['word'].append(collate(list_word))
        # print(json.dumps(data_show))
        return jsonify(data_show)
    else:
        return "not allow"    


@app.route("/thai2rom",methods = ['POST','GET'])
def thai2rom():
    if request.method == 'POST':
        q = request.form['q']
        romanizeshow = romanize(q, engine="thai2rom")
        return str(romanizeshow)
    else:
        return "not allow"      