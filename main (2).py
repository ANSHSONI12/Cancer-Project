import random 
smoker = input('Are you a smoker? ').casefold()
A = "U"
T = "A"
C = "G"
G = "C"

insertation = 0 
deleation = 0
substitution= 0

DNA_sequence =[A,T,C,G]
DNA_sequence_2 = ["A","T","C","G"]
list = []
list_2 = []
gen = 0
mutation_chance = 0
mutation = 0
deleation = 0
for i in range(20):
  anything = random.randint(0,3)
  list.append(DNA_sequence[anything])
  list_2.append(DNA_sequence_2[anything])

for i in range(10):
  if smoker == "yes":
    mutation_chance = 8
  else:
    mutation_chance = 2
  print('DNA Sequence:', list_2)
  anything2 = random.randint(1,10)
  if mutation_chance > anything2:
    anything3 = random.randint(1,3)
    if anything3 == 1:
      print()
      anything4 = random.randint(0,19)
      list.pop(anything4)
      pop=list_2.pop(anything4)
      mutation+=1
      deleation+=1
      print('Deletion of', pop, 'at position', anything4)
    elif anything3 == 2:
      print()
      anything4 = random.randint(1,19)
      anything5 = random.randint(0,3)
      list.insert(anything4,DNA_sequence[anything5])
      list_2.insert(anything4,DNA_sequence_2[anything5])
      mutation+=1
      insertation+=1
      print('Insertion of ',DNA_sequence_2[anything5], ' at position', anything4)
    elif anything3 == 3:
      anything6 = random.randint(1,9)
      anything7 = random.randint(0,3)
      list_2.pop(anything6)
      list.insert(anything6, DNA_sequence[anything7])
      print('Substituded', list_2[anything6] ,'with' ,DNA_sequence[anything7])
      print('')
      mutation +=1
      substitution +=1
      print('Substitution')

print()
print()
print('Total Number of Mutations: ' +str(mutation))
if mutation > 4:
  print('Outlook: We ran the test and unfortuantly you have gotten cancer.')
else:
  print('You dont have Cancer!')
print()
print('Total substitution:' + str(substitution))
print('total Deleation:' + str(deleation))
print('total Insertation:' + str(insertation))
