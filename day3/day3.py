import re
#variables
pattern = r"mul\(\d{1,3},\d{1,3}\)"
dopattern = r"do\((.*?)don't\)"
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

for domatch in domatches:

    validmatches = domatch.group(1).strip()

    doentryvalues = re.findall(pattern, validmatches)

    for value in doentryvalues:
        values = tuple(map(int, re.findall(r"\d+", value)))
        result = values[0] * values[1]
        doentries.append(result)


print(doentries)
print(len(domatches))
print(sum(doentries))
print(sum(entries))



