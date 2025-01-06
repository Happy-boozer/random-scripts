import os # библиотека для работы с системой

kolvo = 0

way = f"H:\CD07"#путь до папки
for filename in os.listdir(way): #читаем имена файлов
    f = os.path.join(way, filename)# соединяем имя файла и путь к нему
    r = f[-3:]# записываем расширение файла
    kolvo += 1

    if kolvo < 100 and filename[0] != "0":
        new_name = "H:\CD07\\"
        new_name += "0"
        new_name += str(kolvo)
        new_name += "."
        new_name += r
        os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)# переименовываем файл
        print(filename)
        print(new_name)
    elif kolvo >= 100 and filename[0] != "0":
        new_name = f"H:\CD07\{kolvo}.{r}"# новое имя файла вместе с путём к нему
        os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)# переименовываем файл
        print(filename)
        print(new_name)
