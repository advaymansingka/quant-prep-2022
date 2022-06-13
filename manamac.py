import random

all_strings = []
for_each = 10
count = 0

while count < 4*for_each:

    n1 = random.randint(2, 100)
    n2 = random.randint(2, 100)

    if count < for_each:
        st = f'{n1} + {n2} = {n1+n2}'
    elif count < 2*for_each:
        st = f'{n1+n2} - {n1} = {n2}'
    elif count < 3*for_each:
        st = f'{n1} x {n2} = {n1*n2}'
    else:
        st = f'{n1*n2} / {n1} = {n2}'

    all_strings.append(st)
    count += 1
    
random.shuffle(all_strings)

textfile = open("outfile.txt", "w")
for element in all_strings:
    textfile.write(element + "\n\n")
textfile.close()
