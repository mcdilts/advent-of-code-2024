import re
pattern = "XMAS"

with open('day4\day4_input.txt', 'r') as file:
    plaintext = file.read()

matches = re.findall(pattern, plaintext)

print(len(matches))