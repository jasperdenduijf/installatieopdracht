#Je kunt acties herhalen met verschillende elementen uit een lijst met een for-loop.

boodschappen = ["ei", "appel", "koek", "melk", "brood"]

for element in boodschappen:
    print(element)
    
#Je kunt for-loops ook gebruiken om berekeningen te doen. Bijvoorbeeld de tafel van 7.
#Met de range-function kun je eenvoudig een lijst krijgen van een bepaalde lengte.

counter = 7
for i in range(10):
    print(counter)
    counter = counter + 7
