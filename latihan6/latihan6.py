#membuat dictionary
pak_tani = {
    "nama": "puput",
    "umur": "19",
    "hobi": ["main tiktok", "menonton", "jalan-jalan"],
    "punya cowo": True,
    "sosmed" : {
        "facebook":"putrinamora",
        "twitter":"@putrinamora"
    }
}
pak_bos = {
    "nama": "ramdan",
    "umur": "21",
    "hobi": ['gitar', 'futsal', 'ngoding'],
    "punya cewe": True,
    "sosmed" : {
        "facebook":"ikan",
        "twitter":"@ramdan"
}
    
}
print("nama saya adalah %s" % pak_tani["nama"])
print("twitter: %s" % pak_bos["sosmed"]["twitter"])