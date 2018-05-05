#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

#conn = MongoClient('mongodb://blackboard:yciF5rhV69#BHS^+@s-bp11f7277b998db4.mongodb.rds.aliyuncs.com:3717,s-bp182385e7507174.mongodb.rds.aliyuncs.com:3717,s-bp14f9fc98bd66d4.mongodb.rds.aliyuncs.com:3717/blackboard')
conn = MongoClient('mongodb://s-bp11f7277b998db4.mongodb.rds.aliyuncs.com:3717,s-bp182385e7507174.mongodb.rds.aliyuncs.com:3717,s-bp14f9fc98bd66d4.mongodb.rds.aliyuncs.com:3717')
#conn = MongoClient('mongodb://root:Jm4V4htz$E#dYn6j*(@s-bp11f7277b998db4.mongodb.rds.aliyuncs.com:3717,s-bp182385e7507174.mongodb.rds.aliyuncs.com:3717,s-bp14f9fc98bd66d4.mongodb.rds.aliyuncs.com:3717')
db = conn['blackboard']
db.authenticate('blackboard','yciF5rhV69#BHS^+')

my_set = db.bag

Count = my_set.find().count()
print(Count)
