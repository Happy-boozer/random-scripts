import os  # библиотека для работы с системой


way = r"L:"  # путь к папкам

def main(way):


    for dirname in os.listdir(way):  # читаем имена папок
        kolvo = 0
        if dirname[0:2] == "CD":
            new_way = way + "\\"  # создаём путь в которой будем считать файлы
            new_way += dirname  # приклеиваем имя папки
            for filename in os.listdir(new_way):
                # считываем имена файлов внутри папки
                kolvo += 1  # считаем количество фалов внутри папки
                f = os.path.join(new_way, filename)  # соединяем имя файла и путь к нему
                r = f[-3:]  # записываем расширение файла

                if kolvo < 100 and filename[0].isdigit() is False:
                    if kolvo < 10:
                        nn = "00"
                        new_name = f"{new_way}\{nn}{kolvo}{filename}"
                        os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл
                    else:
                        new_name = new_way
                        n = "0"
                        new_name = f"{new_way}\{n}{kolvo}{filename}"
                        os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл

                elif kolvo >= 100 and filename[0].isdigit() is False:
                    new_name = f"{new_way}\{kolvo}{filename}"  # новое имя файла вместе с путём к нему
                    os.rename(f, new_name, src_dir_fd=None, dst_dir_fd=None)  # переименовываем файл
main(way)
