import os # библиотека для работы с системой

way = f"G:"#путь к папкам
def counting(way):
    itogo = 0
    for dirname in os.listdir(way): #читаем имена папок
        kolvo = 0
        if dirname[0:2] == "CD":
            new_way = way #создаём путь в которой будем считать файлы
            new_way += dirname #приклеиваем имя папки
            for filename in os.listdir(new_way):# считываем имена файлов внутри папки
                kolvo += 1#считаем количество фалов внутри папки
        itogo += kolvo
    return itogo

print(counting(way))
