import argparse
import shutil
from pathlib import Path

def parse_argv():
    parser = argparse.ArgumentParser(description="Сортування файлів по піддиректоріях на основі розширень")
    parser.add_argument("-S", "--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("-O", "--output", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy(item, dst)
        else:
            file_extension = item.suffix[1:]
            if file_extension:
                folder = dst / file_extension
                try:
                    folder.mkdir(exist_ok=True, parents=True)
                except OSError as e:
                    print(f"Помилка при створенні піддиректорії {folder}: {e}")
                    continue  # Пропускаємо поточний файл і продовжуємо з наступним
                
                try:
                    shutil.copy2(item, folder)
                except OSError as e:
                    print(f"Помилка при копіюванні файлу {item} до {folder}: {e}")
            else:
                no_extension_folder = dst / "no_extension"
                try:
                    no_extension_folder.mkdir(exist_ok=True, parents=True)
                except OSError as e:
                    print(f"Помилка при створенні піддиректорії для файлів без розширення: {e}")
                    continue
                
                try:
                    shutil.copy2(item, no_extension_folder)
                except OSError as e:
                    print(f"Помилка при копіюванні файлу без розширення {item} до {no_extension_folder}: {e}")

def main():
    args = parse_argv()
    print(f"Вхідні аргументи: {args}")
    if not args.source.exists():
        print(f"Джерельна директорія {args.source} не існує.")
        return
    if not args.output.exists():
        try:
            args.output.mkdir(parents=True)
        except OSError as e:
            print(f"Помилка при створенні директорії призначення {args.output}: {e}")
            return
    recursive_copy(args.source, args.output)

if __name__ == "__main__":
    main()