from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


filename = "token.json"
id = "1R_Fn8pZjGBPLyNb-2PogOoJexma0ASICCq-5sJir-Ec"


class SheetAPI:
    __creds = None
    __service = None
    __sheet = None


    def __init__(self, creds_file_name: str = filename, sheet_id: str = id):
        self.__creds = Credentials.from_authorized_user_file(filename=creds_file_name)
        self.__service = build("sheets", "v4", credentials=self.__creds)
        self.__sheet = self.__service.spreadsheets()


    def get_values(self, sheet_id: str, range: str):
        sheet_read = self.__sheet.values().get(
            spreadsheetId=sheet_id,
            range=range
        ).execute()

        return sheet_read.get("values", [])


    def update_values(self, sheet_id: str, range: str, values):
        body = {"values": values}

        self.__sheet.values().update(
            spreadsheetId=sheet_id,
            range=range,
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()


    def update_note_value(self, sheet_id: str, row: int, value: str):
        requests = [{
            "updateCells": {
                "rows": [
                    {
                        "values": [
                            {
                                "note": value
                            }
                        ]
                    }
                ],
                "fields": "note",
                "start": {
                    "rowIndex": row,
                    "columnIndex": 4
                }
            }
        }]

        self.__sheet.batchUpdate(
            spreadsheetId=sheet_id,
            body={"requests": requests}
        ).execute()


    def clear_value(self, sheet_id: str, row: int, column: int):
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
                                "userEnteredValue": None,
                                "note": None
                            }
                        ]
                    }
                ],
                "fields": "userEnteredValue,note"
            }
        }]

        self.__sheet.batchUpdate(
            spreadsheetId=sheet_id,
            body={"requests": requests}
        ).execute()


    def create_checkbox(self, sheet_id: str, row: int):
        requests = [
            {
                "updateCells": {
                    "range": {
                        "startRowIndex": row - 1,
                        "endRowIndex": row,
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
            spreadsheetId=sheet_id,
            body={'requests': requests}
        ).execute()