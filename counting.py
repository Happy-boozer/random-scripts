import os # библиотека для работы с системой

itogo = 0
way = f"G:"#путь к папкам
for dirname in os.listdir(way): #читаем имена папок
    kolvo = 0
    if dirname[0:2] == "CD":
        #print(dirname)
        new_way = "G:\\"#создаём путь в которой будем считать файлы
        new_way += dirname #приклеиваем имя папки
        #print(new_way)
        for filename in os.listdir(new_way):# считываем имена файлов внутри папки
            kolvo += 1#считаем количество фалов внутри папки
    itogo += kolvo

print(itogo)
