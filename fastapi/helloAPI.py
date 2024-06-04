from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": 'Hello. Put your name in the adress bar if you would like me to great you more personally', "hotel?" : "trivago"}


@app.get('/{name}')
async def name(name:str):
    return {"message": "Hello " + name}
