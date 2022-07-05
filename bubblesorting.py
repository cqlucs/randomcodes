from random import shuffle

nlistrange = int(input("Range of the list:"))
nlist = [*range(1, nlistrange + 1, 1)]
shuffle(nlist)
print("Shuffled list:", nlist)

notperfect = True

while notperfect == True:
    for nterm in range(0, nlistrange - 1, 1):
        if nlist[nterm] > nlist[nterm + 1]:
            tempn = nlist[nterm]
            nlist[nterm] = nlist[nterm + 1]
            nlist[nterm + 1] = tempn
            notperfect = False
    for eachn in range(0, nlistrange - 1, 1):
        if nlist[eachn] > nlist[eachn + 1]:
            notperfect = True
print("PERFECT list", nlist)