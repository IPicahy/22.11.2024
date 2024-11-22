import random
string_massive = "Дана строка состоящая из нескольких слов 9 слова разделены пробелами".strip(" ")
result = random.randint(1,68)
max = result
min = result-1
print(string_massive[min:max])

