full_volume = 1.44 * 1024 * 1024 #объем в байтах
pages = 100
line = 50
simbols = 25
size_simbol = 4 #объем одного символа в байтах

volume = size_simbol * simbols * line * pages
rez = int(full_volume // volume)

print("Количество книг, помещающихся на дискету:", rez)
