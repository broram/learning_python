'''buang nilai kosong'''

data = ["ramdan", "pupuy", "", "kamu", "bersinar"]
nilai_kosng = [ x for x in data if x != ""]
print(nilai_kosng)