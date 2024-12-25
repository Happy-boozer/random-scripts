import os # библиотека для работы с системой

file = open("kolvo.txt", "w+")
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
    file.writelines(str(kolvo)+"\n")# записываем посчитанное в каждой папке в файлик
    #f = os.path.join(way, filename)# соединяем имя файла и путь к нему
file.close()

with open("kolvo.txt", mode="r") as f:# открываем файлик с количествами по каждой папке
    s = f.readlines()
    #print(s)
    for i in s:
        #print(i.split("\n")[0])
        itogo += int(i.split("\n")[0])# суммируем числа считанные из файлика

print(itogo)
