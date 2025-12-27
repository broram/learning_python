'''nested function'''

def luar():
    print("ini fungsi luar")
    def dalam():
        print("ini fungsi dalam")
        return "saya belajar python"
    print(dalam())
luar()