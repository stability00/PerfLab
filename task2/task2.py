import sys

def open_file(filename):
    try:
        with open(filename, "r") as f:
            data = list(f.read().split("\n"))
            nums = [list(map(float, item.split(" "))) for item in data]
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
    return nums

def check_pos_point(center, radius, point):
    equationOfEllipse = ((point[0] - center[0])**2) / radius[0]**2 + ((point[1] - center[1])**2) / radius[1]**2
    if equationOfEllipse == 1.0:
        return 0
    if equationOfEllipse > 1.0:
        return 2
    else:
        return 1

if(len(sys.argv) != 3):
    print('Используйте: "python task2.py <file with center and radius> <file with point coords>')
    sys.exit(1)
    
center, radius = open_file(sys.argv[1])
pointsCoords = open_file(sys.argv[2])
for point in pointsCoords:
    print(check_pos_point(center, radius, point))