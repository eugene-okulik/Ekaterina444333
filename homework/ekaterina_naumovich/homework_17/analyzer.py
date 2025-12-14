import argparse
import os
from colorama import init, Fore, Style

init(autoreset=True)


parser = argparse.ArgumentParser(description="Log analyzer")

parser.add_argument(
    "path",
    help="Полный путь к файлу или папке с логами"
)

parser.add_argument(
    "--text",
    help="Текст для поиска",
    required=True
)

args = parser.parse_args()


log_files = []

if os.path.isfile(args.path):
    log_files.append(args.path)

elif os.path.isdir(args.path):
    for name in os.listdir(args.path):
        full_path = os.path.join(args.path, name)
        if os.path.isfile(full_path):
            log_files.append(full_path)

else:
    print("Указанный путь не существует")
    exit()


for log_file in log_files:
    blocks = {}
    current_time = None
    current_block = []

    with open(log_file) as file:
        for line in file:
            line = line.strip()

            if line[:4].isdigit():
                if current_time:
                    blocks[current_time] = " ".join(current_block)

                parts = line.split()
                current_time = f"{parts[0]} {parts[1]}"
                current_block = [line]
            else:
                current_block.append(line)

        if current_time and current_block:
            blocks[current_time] = " ".join(current_block)

    for time, block in blocks.items():
        if args.text in block:
            words = block.split()

            if args.text in words:
                index = words.index(args.text)
                start = max(index - 5, 0)
                end = index + 6

                snippet = words[start:end]
                snippet[index - start] = (
                    Fore.RED + snippet[index - start] + Style.RESET_ALL
                )

                print("=" * 80)
                print(f"Файл: {log_file}")
                print(f"Время ошибки: {time}")
                print("Фрагмент ошибки:")
                print(" ".join(snippet))
