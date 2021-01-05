import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2, "mango":0}
print(sorted(fruit.items()))

print(sorted(fruit.items(), key=operator.itemgetter(0))) # by key
print(sorted(fruit.items(), key=operator.itemgetter(1))) # by value
