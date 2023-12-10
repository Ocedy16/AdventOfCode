
file_url = 'https://raw.githubusercontent.com/Ocedy16/AdventOfCode/main/AoC_Day1'
import urllib.request

f =  urllib.request.urlopen(file_url)
lines = f.readlines()
f.close()

total = 0
convert = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
for line in lines :
    line = line.decode('utf-8')
    index_min = len(line)
    index_max = 0
    number_min = ""
    number_max = ""
    number_names = list(convert.keys())
    for number in number_names:
        if number in line : 
            if line.find(number) < index_min : 
                index_min = line.find(number)
                number_min = number
            if line.find(number) > index_max : 
                index_max = line.find(number)  
                number_max = number
            
    passed = False
    for letter in line[0:index_min] : 
        if letter.isdigit() :
            total += int(letter)*10
            passed = True
            break
    if not passed : 
        total += convert[number_min]*10
    passed = False 
    for letter in line [index_max:] [::-1]:
        if letter.isdigit() :
            total += int(letter)
            passed = True
            break
    if not passed : 
        total += convert[number_max]
print(total)