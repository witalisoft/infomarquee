#!/usr/bin/python

from flask import Flask, url_for, request, render_template, jsonify
import datetime
from redisdb import RedisDB

app = Flask(__name__)
priorities = ['normal', 'high']

@app.route('/set', methods=['POST'])
def setdata():
    cnt = 0 
    for prio in priorities:
        try:
            jdata = request.get_json()
            assert(jdata['newalert'][prio][0]['text'])
        except:
            cnt = cnt + 1

    if len(priorities) == cnt:
        return jsonify(status='failed to parse data'),400
    else:
        r = RedisDB('localhost',priorities)
        current_timestamp = int(datetime.datetime.strftime(datetime.datetime.now(),'%s'))
    for prio in priorities:
        try:
            for j in jdata['newalert'][prio]:
                r.setvalues(prio,j['text'],current_timestamp+int(j['duration']))
        except:
            pass
    r.cleanup()
    return jsonify(status='success'),200

@app.route('/get')
def getdata():
    try:
        r = RedisDB('localhost',priorities)
        r.cleanup()
        data = r.getvalues()
        if not data:
            raise('No data')
    except:
        return jsonify(status='no data'),404
    return data,200

with app.test_request_context():
    url_for('static',filename='index.html')
    url_for('static',filename='style.css')

if __name__ == '__main__':
    app.run()

