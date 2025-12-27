'''detik sejak awal hari'''
import datetime

x = datetime.datetime.now().strftime("%X")
print(f"sekarang pukul {x}")
h, m, s = map(int, x.split(':'))
detik = h * 3600 + m * 60 + s
print(f"total detik dari jam 00:00 = {detik}")
