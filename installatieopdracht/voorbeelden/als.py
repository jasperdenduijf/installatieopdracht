#Je kunt altijd controleren of een statement waar is of niet met een if-statement:

a = 9

if a > 9:
    print("a is groter dan 9")
elif a < 9:
    print("a is kleiner dan 9")
else:
    print("a is gelijk aan 9")
    
    
    
# Ook gehele strings kunnen worden gecontroleerd, met dubbele ==
#Let op, met één = voeg je een nieuwe variabele toe.
woord = "JCI"

if woord == "JCI":
    print("Dit is JCI!")
    
#Tot slot kun je dingen combineren met 'or' of 'and'.
#Zo kun je twee of meer dingen tegelijkertijd combineren.
b = 7

if a == 7 or b == 7:
    print("a of b is 7")
    
if a==7 and b==7:
    print("a en b zijn 7")
