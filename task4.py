import random
score = 0
answer = 0
for i in range(20):
    result = random.randint(-100,100)
    if result > 0:
        print(result)
        answer = answer+result
    else:
        print(result)
        answer = answer + result
        score = score + 1
print("Сумма:",answer," Кол-во отрицательных значений:",score)