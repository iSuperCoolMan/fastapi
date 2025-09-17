from fastapi import FastAPI, Request


app = FastAPI()


@app.post("/")
async def handle_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)
    return {"status": "success", "data": data}