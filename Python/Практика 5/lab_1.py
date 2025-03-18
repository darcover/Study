import os
import sys
import shutil

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

if not os.path.isdir(path):
    print("Ошибка: указанный путь не существует или не является директорией")
    sys.exit(1)

small_files = []

for entry in os.listdir(path):
    full_path = os.path.join(path, entry)
    if os.path.isfile(full_path) and os.path.getsize(full_path) < 2048:
        small_files.append(entry)

if small_files:
    print("Файлы меньше 2KB:")
    for file in small_files:
        print(file)
    small_dir = os.path.join(path, "small")
    if not os.path.exists(small_dir):
        os.mkdir(small_dir)
    for file in small_files:
        shutil.copy(os.path.join(path, file), os.path.join(small_dir, file))
else:
    print("Файлы меньше 2KB не найдены.")