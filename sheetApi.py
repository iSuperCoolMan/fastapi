from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


filename = "token.json"
id = "1R_Fn8pZjGBPLyNb-2PogOoJexma0ASICCq-5sJir-Ec"


class SheetAPI:
    __creds = None
    __service = None
    __sheet = None
    __sheet_id = None


    def __init__(self, creds_file_name: str = filename, sheet_id: str = id):
        self.__creds = Credentials.from_authorized_user_file(filename=creds_file_name)
        self.__service = build("sheets", "v4", credentials=self.__creds)
        self.__sheet = self.__service.spreadsheets()
        self.__sheet_id = sheet_id


    def get_values(self, range: str):
        sheet_read = self.__sheet.values().get(
            spreadsheetId=self.__sheet_id,
            range=range
        ).execute()

        return sheet_read.get("values", [])


    def update_values(self, range: str, values):
        body = {"values": values}

        self.__sheet.values().update(
            spreadsheetId=self.__sheet_id,
            range=range,
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()


    def type_arrow_down(self, index: int):
        requests = [{
            "updateDimensionProperties": {
                "range": {
                    "dimension": "ROWS",
                    "startIndex": index - 1,
                    "endIndex": index
                },
                "properties": {
                    "pixelSize": 20
                },
                "fields": "pixelSize"
            }
        },
        {
            "updateCells": {
                "rows": [
                    {
                        "values": [
                            {
                                "userEnteredValue": {
                                    "stringValue": "↓"
                                },
                                "userEnteredFormat": {
                                    "horizontalAlignment": "CENTER",
                                    "verticalAlignment": "MIDDLE"
                                }
                            }
                        ]
                    }
                ],
                "fields": "userEnteredValue,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment",
                "start": {
                    "rowIndex": index - 1,
                    "columnIndex": 0
                }
            }
        }]

        self.__sheet.batchUpdate(
            spreadsheetId=self.__sheet_id,
            body={'requests': requests}
        ).execute()


    def clear_value(self, row: int, column: int):
        requests = [{
            "repeatCell": {
                "range": {
                    "startRowIndex": row - 1,
                    "endRowIndex": row,
                    "startColumnIndex": column - 1,
                    "endColumnIndex": column
                },
                "cell": {
                    "dataValidation": None
                },
                "fields": "dataValidation"
            }
        },
        # Очищаем содержимое ячейки (сбрасываем значение)
        {
            "updateCells": {
                "range": {
                    "startRowIndex": row - 1,
                    "endRowIndex": row,
                    "startColumnIndex": column - 1,
                    "endColumnIndex": column
                },
                "rows": [
                    {
                        "values": [
                            {
                                "userEnteredValue": None
                            }
                        ]
                    }
                ],
                "fields": "userEnteredValue"
            }
        }]

        self.__sheet.batchUpdate(
            spreadsheetId=self.__sheet_id,
            body={"requests": requests}
        ).execute()


    def create_checkbox(self, index: int):
        requests = [
            {
                "updateCells": {
                    "range": {
                        "startRowIndex": index - 1,
                        "endRowIndex": index,
                        "startColumnIndex": 3,
                        "endColumnIndex": 4
                    },
                    "rows": [
                        {
                            "values": [
                                {
                                    "userEnteredValue": {
                                        "boolValue": False
                                    },
                                    "dataValidation": {
                                        "condition": {
                                            "type": "BOOLEAN"
                                        },
                                        "strict": True,
                                    }
                                }
                            ]
                        }
                    ],
                    "fields": "userEnteredValue,dataValidation"
                }
            }
        ]

        self.__sheet.batchUpdate(
            spreadsheetId=self.__sheet_id,
            body={'requests': requests}
        ).execute()

