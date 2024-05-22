"""
Emitted Task 1 successfully - AC
Added logger and set up output. 
------

Creates and sends a task message to the queue each execution.
This process runs and finishes. 
Make tasks harder/longer-running by adding dots at the end of the message.

Approach
---------
Work Queues - one task producer / many workers sharing work.


"""

import pika
import sys
import webbrowser

# Adding Logger from utils folder by sepcifying path
from utils.util_logger import setup_logger

# Configuring the Logger:
logger, logname = setup_logger(__file__)


# Define Program functions
#--------------------------------------------------------------------------

def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    ans = input("Would you like to monitor RabbitMQ queues? y or n ")
    print()
    if ans.lower() == "y":
        webbrowser.open_new("http://localhost:15672/#/queues")
        print()
        logger.info()

# call the function defined above
offer_rabbitmq_admin_site()

# create a blocking connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
# use the connection to create a communication channel
channel = connection.channel()
# use the channel to declare a durable queue
# a durable queue will survive a RabbitMQ server restart
# and help ensure messages are processed in order
# messages will not be deleted until the consumer acknowledges
channel.queue_declare(queue="task_queue", durable=True)
# create a message by joining the command line arguments
# Added argv and changed "First task..." to "New task..."
message = " ".join(sys.argv[1, 2, 3:]) or "New task..."
# publish the message to the queue
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
)
# tell the user the message was sent
logger.info(f" [x] sent {message}.")
print(f" [x] Sent {message}")

# close the connection to the server
connection.close()
