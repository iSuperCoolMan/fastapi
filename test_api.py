from fastapi import FastAPI, Request
import sheetApi
import ai


app = FastAPI()
sheetApi = sheetApi.SheetAPI()


@app.post("/")
async def handle_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)

    deformation = ai.create_deformation(data["value"])
    sheetApi.update_values(f"D{data["row"]}", [[deformation]])

    return {"status": "success", "data": data}