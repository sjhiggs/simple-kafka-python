from kafka import KafkaConsumer, TopicPartition
import yaml
import ssl

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

config = read_yaml("config.yml")
sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_SSL'

# Create a new context using system defaults, disable all but TLS1.2
context = ssl.create_default_context()
context.options &= ssl.OP_NO_TLSv1
context.options &= ssl.OP_NO_TLSv1_1

app = config['APP']
print("connecting to: {0}".format(app['BOOTSTRAP']))

consumer = KafkaConsumer('test',
                         group_id='my-group',
                         bootstrap_servers=app['BOOTSTRAP'],
                         sasl_plain_username = app['KAFKA_USERNAME'],
                         sasl_plain_password = app['KAFKA_PASSWORD'],
                         security_protocol = security_protocol,
                         ssl_context = context,
                         sasl_mechanism = sasl_mechanism,
                         api_version = (0,10),
                         auto_offset_reset = 'earliest',
                         )


print("all topics: {0}".format(consumer.topics()))
print("subscription: {0}".format(consumer.subscription()))
print("consumer partitions for topic: {0}".format(consumer.partitions_for_topic('test')))
print("bootstrap connected: {0}".format(consumer.bootstrap_connected()))

# Read and print message from consumer
#for msg in consumer:
#    print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

#print(consumer.poll(1000))

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("topic: {0} partition: {1} offset: {2}  value={3}".format(message.topic, message.partition, message.offset, message.value))

# Terminate the script
# sys.exit()

