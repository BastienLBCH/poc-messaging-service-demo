import json
from confluent_kafka import Producer
from django.conf import settings

config = {'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVER}

producer = Producer(config)
topic = settings.TOPIC

# Delivery callback
def delivery_callback(err, msg):
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print(f"Produced event to topic {topic} \n{msg.key().decode('utf-8')}: {msg.value().decode('utf-8')} \n\n")


class PublishingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """
        Middleware verifying each request is identified
        If user is authentified execute view normally, else returns http error 401
        :param request:
        :return:
        """

        response = self.get_response(request)

        key = "event"
        message = response.content.decode()

        try:
            if 'event' in json.loads(message):
                producer.produce(topic, message, key, callback=delivery_callback)

                # Block until the messages are sent.
                producer.poll(10000)
                producer.flush()
        except Exception:
            pass

        return response

