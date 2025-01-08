import os # библиотека для работы с системой

way = f"H:"#путь к папкам
for dirname in os.listdir(way): #читаем имена папок
    kolvo = 0
    if dirname[0:2] == "CD":
        #print(dirname)
        new_way = "H:\\"#создаём путь в которой будем считать файлы
        new_way += dirname #приклеиваем имя папки
        print(new_way)
        for filename in os.listdir(new_way):# считываем имена файлов внутри папки
            kolvo += 1 #считаем количество фалов внутри папки
            f = os.path.join(way, filename)  # соединяем имя файла и путь к нему
            r = f[-3:]  # записываем расширение файла
            kolvo += 1

            if kolvo < 100 and filename[0] != "0":
                #new_name = "H:\CD07\\"
                new_way += "0"
                new_way += str(kolvo)
                new_way += "."
                new_way += r
                os.rename(f, new_way, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл
                print(filename)
                print(new_way)
            elif kolvo >= 100 and filename[0] != "0":
                new_name = f"{new_way}\{kolvo}.{r}"  # новое имя файла вместе с путём к нему
                os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл
                print(filename)
                print(new_name)
