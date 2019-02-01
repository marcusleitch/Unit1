num1 = input("enter a number")
num1 = int(num1)
num2 = input("enter a number")
num2 = int(num2)

total = num1 * num1
if total >= 25:
    print ("true")
if total <= 24:
    print ("false")

f = open("Review.txt", "w")
f.write("1\n3\n5\n7\n9\n")

f = open("Review.txt", "r")
with open('Review.txt','r') as numbers_file:
    totalnum = 0
    for line in numbers_file:
        if line.strip():
            totalnum += int(line)
print(totalnum)



