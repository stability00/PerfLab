import sys

def count_path(n, m):
    i = 1
    answer = [1]
    if m == 1:
        answer = [elem + 1 for elem in range(n)]
    else:
        while True:
            elem = (1 + i * (m - 1)) % n
            if elem == 0:
                elem = n
            if elem == 1 :
                break
            else:
                answer.append(elem)
            i += 1
    return answer
            
if(len(sys.argv) != 5):
    print('Используйте: "python task4.py <value of n1> <value of m1> <value of n2> <value of m2>')
    sys.exit(1)

n1, m1, n2, m2 = [int(item) for item in sys.argv[1:]]
path = count_path(n1, m1) + count_path(n2, m2)
answer = "".join([str(elem) for elem in path])
print(answer)