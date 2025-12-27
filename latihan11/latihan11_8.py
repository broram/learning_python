'''mapping grade keterangan'''

grade = ["A", "C", "C", "D"]
mapping = {"A": "Sangat Baik", "B": "Baik", "C": "Cukup", "D": "Kurang", "E": "Sangat Kurang"}

grade_m = [mapping[x] for x in grade]
print(grade_m)

