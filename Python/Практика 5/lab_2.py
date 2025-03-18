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
    parser.add_argument(
        "--files",
        nargs="*",
    )
    args = parser.parse_args()

    dir_path = args.dirpath
    if not os.path.isdir(dir_path):
        print(f"Папка '{dir_path}' не существует.")
        sys.exit(1)

    files_to_check = args.files

    if files_to_check:
        present_files = []
        missing_files = []
        for file in files_to_check:
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                present_files.append(file)
            else:
                missing_files.append(file)

        present_file_path = os.path.join(dir_path, "present_files.txt")
        missing_file_path = os.path.join(dir_path, "missing_files.txt")
        with open(present_file_path, "w", encoding="utf-8") as f:
            for file in present_files:
                f.write(file + "\n")
        with open(missing_file_path, "w", encoding="utf-8") as f:
            for file in missing_files:
                f.write(file + "\n")

        print("Файлы, присутствующие в папке:")
        if present_files:
            print("\n".join(present_files))
        else:
            print("Нет файлов, которые присутствуют.")

        print("\nФайлы, отсутствующие в папке:")
        if missing_files:
            print("\n".join(missing_files))
        else:
            print("Нет отсутствующих файлов.")

        print(f"\nСписки сохранены в файлы:\n{present_file_path}\n{missing_file_path}")
    else:
        total_files = 0
        total_size = 0
        for entry in os.listdir(dir_path):
            full_path = os.path.join(dir_path, entry)
            if os.path.isfile(full_path):
                total_files += 1
                total_size += os.path.getsize(full_path)
        print(f"Информация о папке '{dir_path}':")
        print(f"Количество файлов: {total_files}")
        print(f"Общий размер файлов: {total_size} байт")

if __name__ == '__main__':
    main()

# python lab_2.py --dirpath "C:\Users\Cuperliminal\Desktop\Практика 5" --files file1.txt file2.txt 
