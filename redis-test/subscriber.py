import redis

def main():
    r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
    p = r.pubsub()
    p.subscribe("hello")
    try:
        for message in p.listen():
            if message['type'] == 'message':
                print(f"Received message: {message['data']}")
    except KeyboardInterrupt:
        print("Subscriber stopped.")
    except redis.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
main()
