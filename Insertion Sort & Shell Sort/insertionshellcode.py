def insertionSort():
    print("Before sorting:\n", percentage)
    for i in range(1, num):
        key = percentage[i]
        j = i - 1
        while j >= 0 and key < percentage[j]:
            percentage[j + 1] = percentage[j]
            j -= 1
        percentage[j + 1] = key
    print("After sorting:\n", percentage)
    topFiveMarks()

def shellSort():
    print("Before sorting:\n", percentage)
    gap = num // 2
    while gap > 0:
        for i in range(gap, num):
            temp = percentage[i]
            j = i
            while j >= gap and percentage[j - gap] > temp:
                percentage[j] = percentage[j - gap]
                j -= gap
            percentage[j] = temp
        gap //= 2
    print("After sorting:\n", percentage)
    topFiveMarks()

def topFiveMarks():
    print("Top 5 scores are : ")
    for i in range(num-1, 0, -1):
        for j in range(i):
            if percentage[j] < percentage[j+1]:
                percentage[j], percentage[j+1] = percentage[j+1], percentage[j]
    print(percentage[:5])

def repeat():
    choice = int(input("Enter your choice: ").strip())
    if choice == 1:
        shellSort()
    elif choice == 2:
        insertionSort()
    else:
        print("Invalid Input!!\nEnter a valid input!")
        repeat()

percentage = []
num = int(input("Enter number of students: "))
for i in range(num):
    per = float(input(f"Enter percentage of the student {i+1}: "))
    percentage.append(per)

print("Which sort do you want to perform?")
print("1. Shell Sort")
print("2. Insertion Sort")
repeat()
