'''
concept: Encapsulation (Read only attribute)
'''
from Item import Item

intem1 = Item("MyItem", 760)

# seting an attribute
intem1.name = "change"
 
#  Getting an attribute
print(intem1.name)