#!/usr/bin/env python

from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer('my_favorite_topic', group_id='my_favorite_group')
for msg in consumer:
    print(msg)
