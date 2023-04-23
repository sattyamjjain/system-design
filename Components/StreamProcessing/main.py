from confluent_kafka import Producer, Consumer
import pandas as pd

conf = {
    'bootstrap.servers': 'my-kafka-broker:9092',
    'client.id': 'my-client-id'
}
producer = Producer(conf)
consumer = Consumer({
    'bootstrap.servers': 'my-kafka-broker:9092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
})

producer.produce('my-topic', key='key', value='value')

consumer.subscribe(['my-topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    print(f"Received message: {msg.value().decode('utf-8')}")

df = pd.read_json(msg.value())

print(df)
