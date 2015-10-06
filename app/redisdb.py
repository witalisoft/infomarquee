#!/usr/bin/python

import redis
import datetime
from flask import jsonify

class RedisDB:
    def __init__(self,host,priorities):
        self.priorities = priorities
        try:
            self.connection = redis.Redis(host)
            self.connection.ping()
        except:
            print 'Cannot establish connection to redis on ' + host
            sys.exit(2)
    def setvalues(self,key,value,timestamp):
        self.connection.zadd(key,value,timestamp)
    def getvalues(self):
        ret = {}
        for prio in self.priorities:
            output = self.connection.zrangebyscore(prio,"-inf","inf")
            ret[prio] = output
        return jsonify(ret)
    def cleanup(self):
        current_timestamp = int(datetime.datetime.strftime(datetime.datetime.now(),'%s'))
        for prio in self.priorities:
            output = self.connection.zrangebyscore(prio,"-inf",current_timestamp)
            for i in output:
                self.connection.zrem(prio,i)
