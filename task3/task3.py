import sys
import json

def open_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
    return data

def fillInValue(tests, id, value):
    for test in tests:
        if test["id"] == id:
            test["value"] = value
            break
        if "values" in test:
            fillInValue(test["values"], id, value)
        
if(len(sys.argv) != 3):
    print('Используйте: "python task3.py <file with tests> <file with values>')
    sys.exit(1)
    
tests = (open_file(sys.argv[1]))["tests"]
values = (open_file(sys.argv[2]))["values"]
for elem in values:
    fillInValue(tests, elem["id"], elem["value"])
with open("report.json", "w") as f:
    json.dump(tests, f, indent=4, ensure_ascii=False)