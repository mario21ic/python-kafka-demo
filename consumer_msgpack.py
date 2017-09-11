#!/usr/bin/env python

from kafka import KafkaConsumer, TopicPartition
import msgpack

consumer = KafkaConsumer(value_deserializer=msgpack.loads)
consumer.subscribe(['msgpackfoo'])
for msg in consumer:
    assert isinstance(msg.value, dict)
