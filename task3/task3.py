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
        
if(len(sys.argv) != 4):
    print('Используйте: "python task3.py <file with values> <file with tests> <file with report')
    sys.exit(1)
    
values = (open_file(sys.argv[1]))["values"]
tests = (open_file(sys.argv[2]))["tests"]
for elem in values:
    fillInValue(tests, elem["id"], elem["value"])
with open(sys.argv[3], "w") as f:
    json.dump(tests, f, indent=4, ensure_ascii=False)