import csv
import os.path
from datetime import datetime


def read(filename: str) -> list:
    path = f"data/{filename}"
    if os.path.exists(path=path):
        with open(file=path, mode="r", encoding="UTF-8") as file:
            return list(csv.reader(file))
    return []


def write(filename: str, data: list, mode: str = "a") -> None:
    path = f"data/{filename}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(file=path, mode=mode, encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        if mode == "w":
            writer.writerows(data)
        else:
            writer.writerow(data)


def generate_id(data: list) -> int:
    return len(data) + 1


def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
