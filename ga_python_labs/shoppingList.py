#Create new shopping list (the new list should have a title)
#Edit list's name
#See all items
#Add new item
#Exit

class ShoppingList():
    def __init__(self):
        self.items = []
        print('Add an item to your grocery list!')

    def add(self, new):
        self.items.append(new)


list = ShoppingList()

list.add(input())

print(list.items)
