import random

filename = 'your_file'

with open(filename, "w") as file:
    for i in range(1024):  #change 1024 to adjust file size
        dna = ''.join(random.choices(['A', 'C', 'G', 'T'], k=250)) #change k to adjust strand length
        file.write(dna + "\n")