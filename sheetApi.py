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
            valueInputOption="RAW",
            body=body
        ).execute()


# SheetAPI().update_values("D3:D3", [["test"]])


# sheet_read = sheet.values().get(spreadsheetId=sheet_id, range="A1:C4").execute()
#
# values = sheet_read.get("values", [])

# for row in values:
#     print(row)
#
# body = {"values": [[1, 2], [3, 4]]}

# sheet_write = sheet.values().update(spreadsheetId=sheet_id, range="A1:B2", valueInputOption="RAW", body=body).execute()
# sheet_read = sheet.values().get(spreadsheetId=sheet_id, range="A1:C4").execute()
#
# values = sheet_read.get("values", [])
#
# for row in values:
#     print(row)
#
# body = {"properties": {"title": "test"}}
# new_sheet = sheet.create(body=body, fields="spreadsheetId").execute()
# print(f"Spreadsheet ID: {(new_sheet.get('spreadsheetId'))}")

