from fastapi import FastAPI, Request
import redis

app = FastAPI()

r = redis.Redis(host='redis-server', port=6379)

@app.post("/publish{message}")
async def publish_message(request: Request, message: str):
    r.publish('my-channel', message)
    return {"status": "Message published successfully", "message": message}