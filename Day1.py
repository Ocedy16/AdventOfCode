file_url = 'https://raw.githubusercontent.com/Ocedy16/AdventOfCode/main/AoC_Day1'
import urllib.request

f =  urllib.request.urlopen(file_url)
lines = f.readlines()
f.close()

total = 0
for line in lines : 
    line = line.decode('utf-8')
    for letter in line : 
        if letter in "0123456789":
            total += int(letter)*10
            break
    for letter in line [::-1]:
        if letter in "0123456789":
            total += int(letter)
            break
print(total)