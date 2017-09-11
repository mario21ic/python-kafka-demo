#!/usr/bin/env python

from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', key_serializer=str.encode)
producer.send('flipflap', key='ping', value=b'1234')
