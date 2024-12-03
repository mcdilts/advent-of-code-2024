import re
#variables
pattern = "mul\(\d{1,3},\d{1,3}\)"
dopattern = "do\((.*?)don't\)"
matches = []
entries = []
domatches = []
doentries = []
dontentries = []
lastend = 0

with open('day3\day3_input.txt', 'r') as file:
    plaintext = file.read()

matches = re.findall(pattern, plaintext)

for match in matches:
    values = tuple(map(int, re.findall(r"\d+", match)))
    result = values[0] * values[1]
    entries.append(result)

domatches = list(re.finditer(dopattern, plaintext, re.DOTALL))

for match in domatches:

    validmatches = match.group(1).strip()

    doentryvalues = re.findall(pattern, validmatches)

    for value in doentryvalues:
        values = tuple(map(int, re.findall(r"\d+", value)))
        result = values[0] * values[1]
        doentries.append(result)

if lastend < len(plaintext):
    dontentries.append(plaintext[lastend:].strip())

print(doentries)
print(sum(doentries))
print(sum(entries))



