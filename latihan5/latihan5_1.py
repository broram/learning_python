'''jumlah dan rata-rata dari list angka''' 

# kita nge import statistika
import statistics as ss

angka = [7, 5, 3, 8, 10]

jumlahAngka = sum(angka)
rata_rata = ss.mean(angka)

print(f"total : {jumlahAngka}\n",f"rata rata : {rata_rata}")