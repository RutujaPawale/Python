groupA=[]
groupB=[]
groupC=[]
onlyGroupC=[]

a=int(input("How many students are there in group A:"))
b=int(input("How many students are there in group B:"))
c=int(input("How many students are there in group C:"))

for i in range(a):
    name=input("Enter name of the student:")
    groupA.append(name)
    
print("Group A =",groupA)

for i in range(b):
    name=input("Enter name of the student:")
    groupB.append(name)
        
print("Group B =",groupB)

for i in range(c):
    name=input("Enter name of the student:")
    groupC.append(name)
    
print("Group C =",groupC)


def criAndBad():
    print("\nList of students who plays both cricket and Badminton:")
    for i in groupA:
      if i in groupB:
       print(i)



def criOrBad():
    print("\nList of students who plays either Cricket or Badminton but not Football :")
    for i in groupA:
        if i not in groupB:
            print(i)


    for i in groupB:
        if i not in groupA:
            print(i)


def numNCriNBad():
    print("\nNumber of students who neither play cricket nor Badminton:")

    for i in groupC:
        if i not in groupA:
          if i not in groupB:
              onlyGroupC.append(i)
    print(len(onlyGroupC))

def numCriBad(groupC):
    print("\nNumber of students who plays both Cricket and Football but not Badminton :")

    for i in groupC :
     if i in groupA:
      print(len(i))

criAndBad()
criOrBad()
numNCriNBad()
numCriBad(groupC)
