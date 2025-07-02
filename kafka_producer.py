from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

orders = [
    {"order_id": 1, "customer": "John", "amount": 120.5},
    {"order_id": 2, "customer": "Alice", "amount": 89.9},
    {"order_id": 3, "customer": "Bob", "amount": 45.3}
]

for order in orders:
    producer.send('retail_orders', value=order)
    time.sleep(1)

print("Orders sent.")
