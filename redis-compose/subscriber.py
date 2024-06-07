import redis
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to Redis
while True:
    try:
        r = redis.Redis(host='redis-server', port=6379)
        pubsub = r.pubsub()
        pubsub.subscribe('my-channel')
        logger.info("Subscribed to my-channel")

        logger.info("Waiting for messages...")
        for message in pubsub.listen():
            if message['type'] == 'message':
                logger.info(f"Received message: {message['data'].decode('utf-8')}")
    except Exception as e:
        logger.error(f"Error: {e}")
        time.sleep(5)  # Wait before retrying