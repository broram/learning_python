'''mangunakan try-except-else'''
try:
    ramdan = lambda x, y: x / y
    result = ramdan(4, 5)
    # result = ramdan(4, 0)
    # result = ramdan(4, y = "jhiavrv")
    
except (ValueError, ZeroDivisionError):
    print('ada yang salah ituu')
    
else:
    print(result)
    
