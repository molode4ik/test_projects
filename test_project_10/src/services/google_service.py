import gspread
from google.oauth2.service_account import Credentials


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class GoogleService:
    def __init__(self, SECRET_PATH: str, sheet_url: str):
        self._credentials = Credentials.from_service_account_file(SECRET_PATH,
                                                                  scopes=[
                                                                      "https://www.googleapis.com/auth/spreadsheets"])
        self._gc = gspread.authorize(self._credentials)
        self._spreadsheet = self._gc.open_by_url(sheet_url)

    def _get_worksheet(self, sheet_index: int) -> gspread.worksheet.Worksheet:
        return self._spreadsheet.get_worksheet(sheet_index)

    def get_worksheet_data(self, sheet_index) -> dict:
        return self._get_worksheet(sheet_index).get_all_records()

    def append_data(self, worksheet_index: int, row_data: list):
        self._get_worksheet(worksheet_index).append_row(row_data)
