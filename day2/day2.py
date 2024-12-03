#variables
entries = []
allascendingordescending = []
allunder3 = []
only1badvalue = []
spreadsWithOneError = []
#make the list

with open('day2\day2_input.txt', 'r') as file:
    plaintext = file.read()

for line in plaintext.strip().split("\n"):
    entries.append(list(map(int, line.split())))

#print(entries)
#find out the spread between the values of each entry
#collect all entries that are either all ascending or descending in value
for entry in entries:
    spreads = [entry[i+1] - entry[i] for i in range(len(entry) - 1)]
    if all(spread > 0 for spread in spreads) or all(spread < 0 for spread in spreads):
        allascendingordescending.append(entry)


#now take all these and make sure the change rate between values is at least 1 and not more then 3
for item in allascendingordescending:
    spreads = [abs(item[i+1] - item[i]) for i in range(len(item) - 1)]
    if all(spread <= 3 for spread in spreads) and all(spread >= 1 for spread in spreads):
        allunder3.append(item)
print(len(allunder3))

#now do the same thing, but let only 1 value be bad
for item in allascendingordescending:
    spreads = [abs(item[i+1] - item[i]) for i in range(len(item) - 1)]
    spreadErrorCount = sum(1 for spread in spreads if 1 <= spread <= 3)
    if spreadErrorCount <= 1:
        spreadsWithOneError.append(item)

print(len(spreadsWithOneError))
