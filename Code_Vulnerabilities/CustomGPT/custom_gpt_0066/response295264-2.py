
user1 = User("Cpt.Fred")
user1.addCard("diamond", 22)
user1.addCard("hearts", 4)
user1.addCard("spades", 3)

user2 = User("Lt.Connor")
user2.addCard("diamond", 43)

print(user1)  # Output: Cpt.Fred: Card scores: [ diamond-22, hearts-4, spades-3 ]
print(user2)  # Output: Lt.Connor: Card scores: [ diamond-43 ]
