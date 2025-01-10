import os # библиотека для работы с системой

kolvo = 0

way = f"G:\фильмы\Slovo.pacana.Krov.na.asfalte.S01.2023.WEB-DL.1080p"#путь до папки
for filename in os.listdir(way): #читаем имена файлов
    f = os.path.join(way, filename)# соединяем имя файла и путь к нему
    r = f[-3:]# записываем расширение файла
    kolvo += 1

    if kolvo < 100 and filename[0] != "0":
        if kolvo < 10:
            nn = "00"
            seri = "_серия"
            new_name = f"{way}\{nn}{kolvo}{seri}.{r}"
            os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл
        else:
            new_name = way
            n = "0"
            seri = "_серия"
            new_name = f"{way}\{n}{kolvo}{seri}.{r}"
            os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл
    elif kolvo >= 100 and filename[0] != "0":
        seri = "_серия"
        new_name = f"{way}\{kolvo}{seri}.{r}"# новое имя файла вместе с путём к нему
        os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)# переименовываем файл
    print(filename)