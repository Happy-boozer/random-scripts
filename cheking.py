import os # библиотека для работы с системой

way = r"H:" #путь к папкам
for dirname in os.listdir(way): #читаем имена папок
    if dirname[0:2] == "CD":
        files = []
        new_way = way + "\\" #создаём путь в которой будем считать файлы
        new_way += dirname #приклеиваем имя папки
        for filename in os.listdir(new_way):
            # считываем имена файлов внутри папки
            files.append(filename[0:3])

        files = sorted(files)
        for i in range(len(files)-1):
            if int(files[i]) < int(files[i+1]):
                continue
            else:
                print("Error")
                print(new_way, files[i], files[i+1])
