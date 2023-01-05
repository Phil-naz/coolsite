a = [1,2,3]
b = [*a,4,5,6]
print(b)

def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
printScores("Jonathan",100, 95, 88, 92, 99)

def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")