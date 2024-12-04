import re
#variables
pattern = r"mul\(\d{1,3},\d{1,3}\)"
dopattern = r"(do\(\)|don't\(\))"
matches = []
entries = []
domatches = []
doentries = []
predoentries = []

with open('day3\day3_input.txt', 'r') as file:
    plaintext = file.read()

matches = re.findall(pattern, plaintext)

for match in matches:
    values = tuple(map(int, re.findall(r"\d+", match)))
    result = values[0] * values[1]
    entries.append(result)

blocks = re.split(dopattern, plaintext)

collect = True
firstBlockDone = False

for block in blocks:
    block = block.strip()

    if block == "do()":
        enabled = True
        firstBlockDone = True
    elif block == "don't()":
        enabled = False
        firstBlockDone = True
    else:
        if not firstBlockDone or enabled:
            domatches = re.findall(pattern, block)
            for match in domatches:
                values = tuple(map(int, re.findall(r"\d+", match)))
                result = values[0] * values[1]
                if not firstBlockDone:
                    predoentries.append(result)
                else:
                    doentries.append(result)

print(sum(doentries + predoentries))
print(sum(entries))



