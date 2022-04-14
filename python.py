x = int(input("Inter length of the array: "))
n = 0
array = {}
for n in range(x):
    array[n] = int(input("Input an array of numbers:"))

for n in range(x):
    if (array[n] % 2) == 0:
        print(array[n], ": Is even")
    else:
        print(array[n], ": Is ood")