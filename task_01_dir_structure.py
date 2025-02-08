import os
import shutil
import sys

def copy_files_recursively(src_dir, dest_dir):
    try:
        # Ініціалізація директорія призначення
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Перебір всіх елементів у директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо елемент є директорією, викликати функцію рекурсивно
            if os.path.isdir(item_path):
                copy_files_recursively(item_path, dest_dir)

            # Якщо елемент є файлом, обробити його
            elif os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1].lower()  # Отримання розширення файлу
                subdir = os.path.join(dest_dir, file_extension[1:] if file_extension else "no_extension")

                # Ініціалізація піддиректорії для розширення
                if not os.path.exists(subdir):
                    os.makedirs(subdir)

                # Копіювання файлу до відповідної піддиректорії
                shutil.copy2(item_path, subdir)
                print(f"Файл {item} скопійовано до {subdir}")

    except Exception as e:
        print(f"Помилка при обробці {src_dir}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    source_dir = os.path.abspath(sys.argv[1])
    destination_dir = os.path.abspath(sys.argv[2]) if sys.argv[2] else "dist"

    if not os.path.exists(source_dir):
        print(f"Директорія {source_dir} не існує.")
        sys.exit(1)
    if not os.path.isdir(source_dir):
        print(f"Директорія {source_dir} не є директорією.")
        sys.exit(1)

    print(f"Копіювання файлів із {source_dir} до {destination_dir}...")
    copy_files_recursively(source_dir, destination_dir)
    print("Копіювання завершено!")

if __name__ == "__main__":
    main()