#variables
entries = []
allascendingordescending = []
allunder3 = []
spreadErrorCount = 0
spreadsWithErrors = []
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


#now do the same thing, get all the ones with errors
for item in allascendingordescending:
    spreads = [abs(item[i+1] - item[i]) for i in range(len(item) - 1)]
    if not all(1 <= spread <=3 for spread in spreads):
        spreadsWithErrors.append(item)

#now get the ones with only 1 error
for item in spreadsWithErrors:
    spreads = [abs(item[i+1] - item[i]) for i in range(len(item) - 1)]
    errorCount = sum(1 for spread in spreads if spread < 1 or spread > 3)
    if errorCount <= 1:
        spreadsWithOneError.append(item)


#count of all
print(len(entries))
#count of under 3
print(len(allunder3))
#count of with errors
print(len(spreadsWithErrors))
#count of one error
print(len(spreadsWithOneError))

