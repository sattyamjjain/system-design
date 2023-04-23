import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="fanout_exchange", exchange_type="fanout")

message = "Hello, world!"

channel.basic_publish(exchange="fanout_exchange", routing_key="", body=message.encode())
connection.close()
