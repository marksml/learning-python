import casino

print("Deck() shuffle and then deal 3 times:")    
deck = casino.Deck()
deck.shuffle()
print(deck.deal())
print(deck.deal())
print(deck.deal())

print("Die(6) rolls:")    
d = casino.Die(6)
print(d.roll())
print(d.roll())

print("Die(20) rolls:")    
d2 = casino.Die(20)
print(d2.roll())
print(d2.roll())
print(d2.roll())
print(d2.roll())