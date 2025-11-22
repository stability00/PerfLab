import sys

def open_file(filename):
    try:
        with open(filename, 'r') as f:
            data = list(f.read().split("\n"))
            nums = [int(item) for item in data]
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
    return nums

def count_mean(nums):
    sum = 0
    for num in nums:
        sum += num
    return int(sum / len(nums))

def count_moves(nums, mean):
    moves = 0
    for num in nums:
        moves += abs(mean - num)
    return moves

if(len(sys.argv) < 2):
    print('Используйте: "python task4.py <filename>.txt"')
    sys.exit(1)
    
filename = sys.argv[1]
nums = open_file(filename)
mean = count_mean(nums)
moves = count_moves(nums, mean)
if(moves > 20):
    print("20 ходов недостаточно")
else:
    print(f"Минимальное количество ходов: {moves}")