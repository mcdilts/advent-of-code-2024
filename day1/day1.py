#variables
leftlist = []
rightlist = []
differences = []
similarities = []
#make the lists
with open('day1\day1_input.txt', 'r') as file:
    plaintext = file.read()


for line in plaintext.strip().split("\n"):
        sides = line.split()
        if len(sides) >= 2:
              leftlist.append(sides[0])
              rightlist.append(sides[1])

#sort the lists

leftlist.sort()
rightlist.sort()

#for each item in the left list get its matching right list item and find the difference

for index, leftitem in enumerate(leftlist):
      item1 = int(leftitem)
      item2 = int(rightlist[index])
      #add the difference to the list of differences
      differences.append(abs(item1 - item2))
     
#add up all the differences
print(sum(differences))

#look for the current item in the other list and how many times it occurs
for item in leftlist:
      occurances = [i for i, x in enumerate(rightlist) if x == item]
      #multiply the current item by how many times it occurs
      similarity = int(item) * int(len(occurances))
      #add that value to the list of similarities
      similarities.append(similarity)

#add up all the similarities
print(sum(similarities))