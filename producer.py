from kafka import KafkaProducer
import yaml
import ssl

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def on_send_success(record_metadata):
    print("topic: {0} partition: {1} offset: {2}".format( record_metadata.topic, record_metadata.partition, record_metadata.offset))

def on_send_error(excp):
    log.error('error!', exc_info=excp)

config = read_yaml("config.yml")
sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_SSL'

context = ssl.create_default_context()
context.options &= ssl.OP_NO_TLSv1
context.options &= ssl.OP_NO_TLSv1_1

app = config['APP']
print("connecting to: ")
print(app['BOOTSTRAP'])
producer = KafkaProducer( bootstrap_servers=app['BOOTSTRAP'],
                         sasl_plain_username = app['KAFKA_USERNAME'],
                         sasl_plain_password = app['KAFKA_PASSWORD'],
                         security_protocol = security_protocol,
                         ssl_context = context,
                         sasl_mechanism = sasl_mechanism,
                         api_version = (0,10),
                         retries=0)

for i in range(10):
    msg = 'test message number {0}'.format(i) 
    producer.send('test', bytes(msg, 'utf-8')).add_callback(on_send_success).add_errback(on_send_error)

producer.flush()
