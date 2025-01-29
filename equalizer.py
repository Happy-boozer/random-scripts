import os
import counting
import shutil

def equalization(bol,men,mk):
    for filename in os.listdir(bol):
        if int(filename[0:3]) > mk:
            shutil.copy2(f"{bol}/{filename}", f"{men}/{filename}")#копируем файл из одной папки в другую


way1 = "L:"
way2 = "G:"

def equalizer(way1, way2):
    for i in range(1, 9):
        new_way_1 = f"{way1}/CD0{i}"
        new_way_2 = f"{way2}/CD0{i}"
        kolv01 = counting.counting_one_dir(new_way_1)#подсчитываем количество файлов в папке
        kolv02 = counting.counting_one_dir(new_way_2)#подсчитываем количество файлов в папке
        if kolv01 == kolv02:
            continue
        elif kolv01 > kolv02:
            equalization(new_way_1, new_way_2, kolv02)
        elif kolv01 < kolv02:
            equalization(new_way_2, new_way_1, kolv01)
