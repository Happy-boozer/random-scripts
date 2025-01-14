import os # библиотека для работы с системой

def counting(way):
    itogo = 0
    for name in os.listdir(way):  # читаем имена папок
        f = os.path.join(way, name)
        if os.path.isdir(f):
            itogo += counting(f)
        elif os.path.isfile(f):
            itogo += 1
    return itogo

print(counting(way=))