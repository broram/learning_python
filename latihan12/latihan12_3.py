'''cek tanggal hari'''
import datetime

data_tgl = [
    "2005-10-31",
    "2008-08-07",
    "1975-08-17"
]
for items in data_tgl:
       data = datetime.datetime.strptime(items, "%Y-%m-%d")
       print(f"{items} adalah hari {data.strftime('%A')}")
