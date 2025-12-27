'''CEK KEY DI DICTIONARY'''
puput = {
    "nama": "puput",
    "umur": "19",
    "hobi": ["main tiktok", "menonton", "jalan-jalan"],
    "punya cowo": True,
    "sosmed" : {
        "facebook":"putrinamora",
        "twitter":"@putrinamora"
    }
}

#kita mencari apakah di dictionary ada email memakai if/else statement
if 'email' in puput:
    print(True)
else:
    print(False)
