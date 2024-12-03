import re
#variables
pattern = "mul\(\d{1,3},\d{1,3}\)"
matches = []
entries = []

with open('day3\day3_input.txt', 'r') as file:
    plaintext = file.read()

matches = re.findall(pattern, plaintext)

for match in matches:
    values = tuple(map(int, re.findall(r"\d+", match)))
    result = values[0] * values[1]
    entries.append(result)

print(matches)
print(entries)
print(sum(entries))


