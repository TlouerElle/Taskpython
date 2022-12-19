def func(filename):
    try:
        stream = open(filename, 'r', encoding='utf-8')
        print(stream.read())
        stream.close()
    except Exception:
        print('出错')


func(r'E:\mypro\Python\text13.txt')
