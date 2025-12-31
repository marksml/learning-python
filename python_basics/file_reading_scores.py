f = open("scores.txt","r")

print("\n Participant | Score ")
print("--------------------")

for line in f:
    line = line.strip()
    record = line.split(",")
    name = record[0]
    score = record[1]
    name = " "+ name.ljust(12,' ')
    score = " "+score.ljust(7,' ')
    print(name + "|" + score)

print("\n")