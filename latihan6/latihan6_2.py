'''buat dan dan tampilkan dictionary'''

biodata = {
    'nama':'pupu',
    'kelas':'informatika',
    'nilai': 80
}

biodata['nilai'] = 95
biodata.update({"lulus" : True})

for key, val in biodata.items():
    print("%s : %s" % (key, val))
