'''buat file laporan nilai'''

datasiswa = []

def inputan_data_ke_dictonary():
    n = int(input("masukan berapa banyak data dimasukan: "))
    
    for _ in range(n):
        
        nama = input("masukan nama : ")
        nilai = int(input("masukan nilai : "))
        
        siswa = {
            "nama" : nama,
            "nilai" : nilai
        }
        datasiswa.append(siswa)
    
def list_ke_file():
    with open('D:/ramdan/projek/python/2bulan/filesemua/'+ file +'.txt', 'w') as f:
        for item in datasiswa:
            for key, val in item.items():
                f.write("%s : %s\n" % (key, val))
             
if __name__=="__main__":
    while True:
        print("pilih")
        print("1. masukan data siswanya ")    
        print("2. kirim ke file ")
        pilihan = int(input("masukakan pilihan: "))
        if pilihan == 1:
            inputan_data_ke_dictonary()
        elif pilihan == 2:
            file = input("masukan nama file : ")
            list_ke_file()
            
    
    
        
        
    
