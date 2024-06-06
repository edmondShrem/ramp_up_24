from fastapi import FastAPI
import uvicorn
import redis

r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
r.ping()
app = FastAPI()

@app.post("/publish")
def wee(msg:str):
    try:
        r.publish("hello",msg)
        return {"message": "Message published successfully"}
    except redis.ConnectionError as e:
        return {"error": "Failed to connect to Redis"}
    except Exception as e:
        return {"error": "An unexpected error occurred"}
    