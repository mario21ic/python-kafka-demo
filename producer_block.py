#!/usr/bin/env python

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send('foobar', b'another_message')
result = future.get(timeout=60)

