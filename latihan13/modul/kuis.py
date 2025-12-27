'''modul quiz'''
import time

question = [
    {
        "pertanyaan" : "salah satu yang bukan termasuk berpikir krtis adalah",
        "objektif" : ["percaya diri", "keterbukaan", "ketekunan", "intelektual"],
        "jawaban" : "d"
    },
    {
        "pertanyaan" : "sikap untul berpikir kritis yaitu",
        "objektif" : ["percaya diri", "sombong", "disiplin", "mandiri"],
        "jawaban" : "b"
    }
]
objek = ["a", "b", "c", "d"] 

def kuuis(question, objek):
    score = 0
    total_score = len(question)
    print("selamat datang di quiz python")
    for i, q_data in enumerate(question):
        print(f"\nquestion{i+1} : {q_data['pertanyaan']}")
        for i, j in enumerate(q_data['objektif']):
            print(f"{objek[i]}. {j}")
            
        stars_time = time.perf_counter()
        
        pilihan = input('masukan jawaban anda : ')
        
        if q_data['jawaban'] == pilihan:
            print("jawaban anda benar")
            score += 1
        else:
            print("jawaban anda salah")
        end_time = time.perf_counter()
        
        result_time = end_time - stars_time
        print(f"waktu yang dibutuhkan {result_time:.2f} detik")
    print(f"total score anda: {score}/{total_score}\n")

    

        