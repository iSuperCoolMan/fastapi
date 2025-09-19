from fastapi import FastAPI, Request
import sheetApi
import ai


app = FastAPI()
sheetApi = sheetApi.SheetAPI()


@app.post("/")
async def handle_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)

    if data["column"] == 1:
        if data["value"]:
            sheetApi.create_checkbox(data["row"])
            print(f"Checkbox created at D{data["row"]}")
            sheetApi.type_arrow_down(data["row"] + 1)
        else:
            sheetApi.clear_value(data["row"], 1)
            print(f"Field cleared at A{data["row"]}")
            sheetApi.clear_value(data["row"] + 1, 4)
            print(f"Field cleared at D{data["row"]}")
    elif data["column"] == 4:
        response = ai.create_deformation(data["value"])
        sheetApi.update_values(f"E{data["row"]}", [[response["deformation"]]])

    return {"status": "success", "data": data}