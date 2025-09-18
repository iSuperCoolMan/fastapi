from fastapi import FastAPI, Request
from sheetApi import SheetAPI
import ai



app = FastAPI()
sheetApi = SheetAPI()


@app.post("/")
async def handle_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)

    deformation = ai.create_deformation(data["value"])
    sheetApi.update_values(f"D{data["row"]}", deformation)

    return {"status": "success", "data": data}