import random
alphabet = [chr(i) for i in range(65, 90)]
for i in range(10):
    result = random.choice(alphabet)
    print(result)