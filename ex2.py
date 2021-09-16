
#fruits=['apple', 'orange', 'tomatoes', 'bananas']
#names = ['david', 'blake', 'mike']
#for fruit in fruits:
#    print(f"\n{fruit.title()} is fruit")
#    print(f"This is the second line for {fruit}")
#    for name in names:
##
#print("Thank you")

colors = (1, 2, 3, 4, 5)


for color in colors:
    print(f"My favorite color is: ", color)

my_food = ['honey', 'chocolate', 'egg']
friend_food = my_food[:]

print("My favorite food is ")
print(my_food)

friend_food.append('caramel')
print("My friend's favorite food is ")
print(friend_food)

cube = [number ** 3 for number in range(1,11)]
print(cube)

a = list(range(1,10000))
for number in a[0:500:5]:
    print(number.sort())

