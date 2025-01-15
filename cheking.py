import os # библиотека для работы с системой

way = r"H:" #путь к папкам
for dirname in os.listdir(way): #читаем имена папок
    kolvo = 0
    if dirname[0:2] == "CD":
        files = []
        #print(dirname)
        new_way = way + "\\" #создаём путь в которой будем считать файлы
        new_way += dirname #приклеиваем имя папки
        for filename in os.listdir(new_way):
            # считываем имена файлов внутри папки
             #считаем количество фалов внутри папки

            if int(filename[0:3]) == kolvo:
                print(filename[0:3], kolvo)
                continue
            else:
                print(filename[0:3], kolvo)
                print(new_way, "  ", filename)
                break

