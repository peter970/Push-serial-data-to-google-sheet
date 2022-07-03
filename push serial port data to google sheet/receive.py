import asyncio
import json
import concurrent
from matplotlib.font_manager import json_dump
from serial import Serial
import gspread
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('steam-lock-354906-b57134599474.json',scopes=scopes)
gc = gspread.authorize(credentials)
spreadsheet_key='1NIV2XC5L0vMTOLw4wZEWSCjWqPq9GqLLzlMDiEDJfzo'
sheet=gc.open_by_key(spreadsheet_key).worksheet("sheet1") #"sheet1"位置填寫自己工作表的名稱

port_data = []
def get_byte():
    return s.read(5)
@asyncio.coroutine
def get_byte_async():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        res = yield from loop.run_in_executor(executor, get_byte)
        return res
def get_and_print():
    b = yield from get_byte_async()
    #port_data.append(b)
    c = json.dumps({'message':b.decode('utf-8')})
    print (b)
    port_data.append(c)
    print(port_data)
    sheet.append_row(port_data) #上傳到google sheet

s = Serial("COM2", 19200, timeout=10) #連到COM2
loop = asyncio.get_event_loop()
loop.run_until_complete(get_and_print())