# Chapter 3 - Introducing Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing element in a list by telling Python the position, or index
print(bicycles[0])

#Formatting 'trek' by using title() method
print(bicycles[0].title())

#Index Positions Start at 0, Not 1
#second item has an index of 1. To access fourth item in a list, the item at index 3.
print(bicycles[1])
print(bicycles[3])

#By asking for item at index -1, Python always return the last item in the list.
print(bicycles[-1])

#Create message based on a value from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)