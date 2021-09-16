#fruits=['apple', 'orange', 'tomatoes', 'bananas']
#names = ['david', 'blake', 'mike']
#for fruit in fruits:
#    print(f"\n{fruit.title()} is fruit")
#    print(f"This is the second line for {fruit}")
#    for name in names:
##
#print("Thank you")

cube = [number ** 3 for number in range(1,11)]
print(cube)

a = list(range(1,10000))
for number in a[0:500:5]:
    print(number.sort())
