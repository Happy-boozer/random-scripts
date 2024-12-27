import os # библиотека для работы с системой
with open("prefixsis.txt", mode="r") as f:
    s = f.readlines()

prefixsis = []
for i in s:
    prefixsis.append(i.rstrip())

way = f"G:\фильмы\Supernatural_S_1_S_4_2005_2009_DVDRip_HDTVRip\Supernatural 2-LostFilm.TV"#путь до папки
for filename in os.listdir(way): #читаем имена файлов
    f = os.path.join(way, filename)# соединяем имя файла и путь к нему
    r = f[-3:]# записываем расширение файла

    new_name = f"G:\фильмы\Supernatural_S_1_S_4_2005_2009_DVDRip_HDTVRip\Supernatural 2-LostFilm.TV\{filename[17:19]}_серия.{r}"# новое имя файла вместе с путём к нему
    os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)# переименовываем файл
    print(filename)
