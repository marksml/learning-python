f = open("countries.txt","r")

countries = []

for line in f:
    line = line.strip()
    #print("type: "+ str(type(line)))
    #print(line)
    countries.append(line)

f.close()

print(countries)

print("Länge der Länderliste: "+ str(len(countries)))

f = open("countries_new.txt","w")

f.write("Test")