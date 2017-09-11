#!/usr/bin/env python

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('foobar2', key=b'foo', value=b'bar')
