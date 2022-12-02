lines = open(f'C:\\Users\\hayde\\Desktop\\Repos\\Advent_of_Code\\Year22\\Day2file.txt').read().splitlines()

total = 0
DINNER_TABLE = ["ZXY","XYZ","YZX"]
for line in lines:
    them,us = line.split(' ')
    total += DINNER_TABLE[ord(them)-65].find(us)*3+ord(us)-87
print(total)

total = 0
DINNER_TABLE = ["BCA","ABC","CAB"]
for line in lines:
    them,result = line.split(' ')
    total += DINNER_TABLE[ord(result)-88].find(them)+1+(ord(result)-88)*3
print(total)