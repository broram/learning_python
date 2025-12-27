'''seorang siswa dianggap lulus jika nilai ujian labih dari atau sama
dengan 70 dan nilai absensi lebih dari 75'''

# menginput data
nilaiUjian = int(input("masukan nilai ujian:"))
nilaiAbsen = int(input("masukan nilai absen:"))

lulus = (nilaiUjian >= 70) and (nilaiAbsen >= 75)

print(f"status kelulusan: {'lulus' if lulus else 'tidak lulus'}")