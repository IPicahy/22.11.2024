import random
alphabet = [chr(i) for i in range(33,47)]
print(alphabet)
for i in range(15):
    result = random.choice(alphabet)
    print(result)