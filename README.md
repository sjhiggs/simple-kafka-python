# Simple pythion client for Kafka (RHOSAK)

Simple client that connects to Red Hat managed kafka instance for testing purposes.  Uses SSL and SASL Plain.

## Install

~~~
pip install kafka-python
pip install pyyaml
~~~

## Client Configuration

1.  Copy config.yml.orig to config.yml
2.  Edit bootstrap server(s), username, password in config.yml

Note: also need to configure service account permissions server-side!

## Run

1.  start consumer

python consumer.py


2.  start producer

python producer.py


## Example output

Producer
~~~
$ python ./producer.py 
connecting to: 
['test.kafka.rhcloud.com:443']
topic: test partition: 0 offset: 105
...
topic: test partition: 0 offset: 114
~~~

Consumer
~~~
$ python ./consumer.py
connecting to: ['test.kafka.rhcloud.com:443']
all topics: {'test'}
subscription: {'test'}
consumer partitions for topic: {0}
bootstrap connected: True
topic: test partition: 0 offset: 105  value=b'test message number 0'
...
topic: test partition: 0 offset: 114  value=b'test message number 9'
~~~

