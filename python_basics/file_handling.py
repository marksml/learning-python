f = open("countries.txt","r")

countries = []

for line in f:
    line = line.strip()
    #print("type: "+ str(type(line)))
    #print(line)
    countries.append(line)

f.close()

print(countries)
print("\nLänge der Länderliste: "+ str(len(countries)))

for country in countries:
    if(country[0] == "T"):
        print(country)


# reverse the countries list
countries.reverse()

# write the countries to the new file
f = open("countries_in_reverse.txt","w")

for country in countries:
    f.write(country + "\n")

f.close()
