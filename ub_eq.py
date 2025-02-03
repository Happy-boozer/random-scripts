import os
import counting
import shutil

def equalization(bol,men,mk):
    for filename in os.listdir(bol):
        if int(filename[0:3]) > mk:
            shutil.copy2(f"{bol}/{filename}", f"{men}/{filename}")#копируем файл из одной папки в другую


way1 = "L:"
way2 = "G:"


def un_eq(way1, way2):
    for i in os.listdir(way1):
        f = os.path.join(way1, i)
        if os.path.isdir(f):
            un_eq(way1 + "\\" + i, way2 + "\\" + i)
        else:
            kolv01 = counting.counting_one_dir(way1)  # подсчитываем количество файлов в папке
            kolv02 = counting.counting_one_dir(way2)
            if kolv01 == kolv02:
                continue
            elif kolv01 > kolv02:
                equalization(way1, way2, kolv02)
            elif kolv01 < kolv02:
                equalization(way2, way1, kolv01)

un_eq("G:", "L:")