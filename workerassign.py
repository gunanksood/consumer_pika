#!/usr/bin/env python
import pika
import time
import pymongo


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks_queue')
print(' [*] Waiting for messages. To exit press CTRL+C')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def callback(ch, method, properties, body):
    l = body.split(",")
    mydata = {"ID": l[0], "name": l[1], "Marks": l[2]}
    x = mycol.insert_many(mydata)
    print(" [x] Received %s hello " %l[0])
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    # ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=100)

channel.basic_consume(callback,
                      queue='tasks_queue', no_ack=True)


channel.start_consuming()


