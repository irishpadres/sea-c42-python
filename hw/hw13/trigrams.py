import re

f = open('sherlock-small_txt.txt', 'r')
lines = f.readlines()
print(re.split("\W+", lines[0]))
