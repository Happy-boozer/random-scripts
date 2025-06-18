import os


def remove_all_digits(text):
    #Удаляет все цифры из строки.
    return ''.join([c for c in text if not c.isdigit()])


def main(folder_path):
    folder_path = os.path.normpath(folder_path)  # Исправляем путь для Windows/Linux

    file_count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)  # Полный путь к файлу

        if not os.path.isfile(file_path):  # Пропускаем папки
            continue

        file_count += 1

        # Разделяем имя и расширение (например, "1a2b3.txt" → "1a2b3", ".txt")
        name_part, ext = os.path.splitext(filename)

        # Удаляем ВСЕ цифры из имени
        name_without_digits = remove_all_digits(name_part)

        # Если после удаления цифр имя стало пустым, используем просто номер
        if not name_without_digits:
            new_name = f"{file_count:03d}{ext}"  # Формат: 001.txt, 002.jpg и т. д.
        else:
            # Добавляем нумерацию в формате "001имя", "002имя"...
            new_name = f"{file_count:03d}{name_without_digits}{ext}"

        # Полный путь к новому имени
        new_file_path = os.path.join(folder_path, new_name)

        # Переименовываем файл
        try:
            os.rename(file_path, new_file_path)
            print(f"✅ Переименовано: {filename} → {new_name}")
        except Exception as e:
            print(f"❌ Ошибка при переименовании {filename}: {e}")


# Пример использования:
folder = r"F:\CD08"  # Путь к папке (можно изменить)
main(folder)
