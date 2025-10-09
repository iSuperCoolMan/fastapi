from fastapi import FastAPI, Request
import sheetApi
import ai


app = FastAPI()
sheetApi = sheetApi.SheetAPI()


@app.post("/arrow/1")
async def handle_edit_first_column(request: Request):
    data = await request.json()
    print("Received data:", data)

    if data["value"]:
        sheetApi.create_checkbox(data["id"], data["row"])
        print(f"Checkbox created at D{data["row"]}")
    else:
        sheetApi.clear_value(data["id"], data["row"], 4)
        print(f"Checkbox deleted at D{data["row"]}")

    return {"status": "success", "data": data}


@app.post("/arrow/4")
async def handle_edit_fourth_column(request: Request):
    data = await request.json()
    print("Received data:", data)

    response = ai.create_deformation(data["value"])
    sheetApi.update_values(data["id"], f"E{data["row"]}", [[response["deformation"]]])
    sheetApi.update_note_value(data["id"], data["row"], response["description"])
    sheetApi.update_values(data["id"], f"D{data["row"]}", [["FALSE"]])

    return {"status": "success", "data": data}