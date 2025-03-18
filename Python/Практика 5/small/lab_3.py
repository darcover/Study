import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
    )
    parser.add_argument(
        "--dirpath",
        default=".",
    )
    args = parser.parse_args()

    dir_path = args.dirpath
    if not os.path.isdir(dir_path):
        print(f"Папка '{dir_path}' не существует.")
        sys.exit(1)

    missing_file_list = os.path.join(dir_path, "missing_files.txt")
    if not os.path.isfile(missing_file_list):
        print(f"Файл '{missing_file_list}' не найден. Убедитесь, что программа 2 создала его.")
        sys.exit(1)

    with open(missing_file_list, "r", encoding="utf-8") as f:
        missing_files = [line.strip() for line in f if line.strip()]

    if not missing_files:
        print("Список отсутствующих файлов пуст.")
        return

    for filename in missing_files:
        file_path = os.path.join(dir_path, filename)
        if os.path.exists(file_path):
            print(f"Файл '{filename}' уже существует, пропускаем.")
        else:
            with open(file_path, "w", encoding="utf-8") as new_file:
                pass  
            print(f"Файл '{filename}' создан.")

if __name__ == '__main__':
    main()
