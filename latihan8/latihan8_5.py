'''function generator function deskripsi grade'''

def buat_deskirpsi(grade):
    def inner():
        mapping = {
            "A" : "sangat baik",
            "B" : "baik",
            "C" : "cukup",
            "D" : "kurang",
            "E" : "sangat kurang"
        }
        return mapping.get(grade, "tidak falid")
    return inner

f = buat_deskirpsi("B")
print(f())