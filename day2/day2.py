#variables
entries = []
allascendingordescending = []
allunder3 = []
spreadErrorCount = 0
spreadsWithErrors = []
spreadsWithOneError = []
spreadsWithOneErrorCorrect = []


#make the list

with open('day2\input.txt', 'r') as file:
    plaintext = file.read()

for line in plaintext.strip().split("\n"):
    entries.append(list(map(int, line.split())))

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
    else: spreadsWithErrors.append(item)

#now get the ones with only 1 error
for item in spreadsWithErrors:
    spreads = [abs(item[i+1] - item[i]) for i in range(len(item) - 1)]
    errorCount = sum(1 for spread in spreads if spread < 1 or spread > 3)
    if errorCount > 1:
        spreadsWithOneError.append(item)

#check the ones with one error to make sure they follow the other rules
for item in spreadsWithOneError:
    spreads = [abs(item[i+1] - item[i]) for i in range(len(item) - 1)]
    if any(spread <= 3 for spread in spreads) and any(spread >= 1 for spread in spreads):
        spreadsWithOneErrorCorrect.append(item)

#count of all
print("All Entries: " + str(len(entries)))
#either ascending or descending only
print("Ascending or Descending only: " + str(len(allascendingordescending))) 
#count between 1 and 3
print("between 1 and 3: " + str(len(allunder3)))
#count of with errors
print("with errors: " + str(len(spreadsWithErrors)))
#count of one error
print("with one error: " + str(len(spreadsWithOneError)))
#count of one error correct
print("with one error correct: " + str(len(spreadsWithOneErrorCorrect)))

