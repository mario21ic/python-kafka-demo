#!/usr/bin/env python

from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.assign([TopicPartition('foobar', 2)])
msg = next(consumer)
