import random
data = []
alphabet_a= [chr(i) for i in range(97, 122)]
alphabet_A = [chr(i) for i in range(65, 90)]
numbers = [chr(i) for i in range(48, 57)]
special_characters = [chr(i) for i in range(33,47)]
score = random.randint(8,15)

for i in range(score):
    choice = random.randint(1,4)
    if choice == 1:
        data.append(random.choice(alphabet_a))
    if choice == 2:
        data.append(random.choice(alphabet_A))
    if choice == 3:
        data.append(random.choice(numbers))
    if choice == 4:
        data.append(random.choice(special_characters))
result = ''.join(data)
print(result)