squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares = list(map(lambda x:x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

squares = [(x, y) for x in[1,2,3] for y in[3, 1, 4] if x != y]
print(squares)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vecResult = [x * 2 for x in vec]
print(vecResult)

# filter the list to exclude negative numbers
vecResult2 = [x for x in vec if x >= 0]
print(vecResult2)

# apply a function to all the elements
vecResult3 = [abs(x) for x in vec]
print(vecResult3)

# call a methond on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])