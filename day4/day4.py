import re
pattern = "XMAS"

with open('day4\input.txt', 'r') as file:
    plaintext = file.read()

matches = re.findall(pattern, plaintext)

print(len(matches))