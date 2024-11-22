import random
for i in range(10):
    result = str(random.uniform(0.001,5))
    swith = random.randint(0,1)
    if swith > 0:
        print(result[:5])
    else:
        print("-" + result[:5])
