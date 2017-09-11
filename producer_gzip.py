#!/usr/bin/env python

from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', compression_type='gzip')
for i in range(1000):
    producer.send('foobar', b'msg %d' % i)
