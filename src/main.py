from contextlib import asynccontextmanager
import requests
from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
from fastapi_utils.tasks import repeat_every


env_path = Path(f"/.env")
load_dotenv(dotenv_path=env_path)




app = FastAPI(
    title="kucoinp2p")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event('startup')
@repeat_every(seconds=200)
async def say_hello():
    data = requests.get("https://www.kucoin.com/_api/otc/ad/list?status=PUTUP&currency=USDT&legal=EUR&page=1&pageSize=10&side=BUY&amount=&payTypeCodes=REVOLUT&lang=en_US")
    highest_price = data.json()['items'][0]['floatPrice']



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )