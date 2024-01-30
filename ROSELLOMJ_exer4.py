#Author: Ma. Jazmine P. Rosello
#Program Domain: 
#python program that implements the game titled 6K’s of relationship. 6K’s of relationship is a game named after the acronym: Kaibigan, Kapuso, Kaaway, Kasal, Kilig(crush), Kapatid.

print("\n\tWelcome!\nChildhood won't be complete without having crush on someone,\nNow here's the program for entertainment :>\n ")

#.lower() makes everything user's input to be in the lowercase no matter what so the program will take it as if it is in lower case
name1 = input("Player 1 name: ").lower() 
name2 = input("Player 2 name: ").lower()

#to check if the letter in name 1 is the same is in the name 2,
for i in name1: 
    if i in name2:
        name1 = name1.replace(i, "")
        name2 = name2.replace(i, "")

#Incase user inputs have the non-alphabetical such as period, comma etc...
alphabet = "abcdefghijklmnopqrstuvwxyz" #this alphabet is the basis of what counts     
combine = name1 + name2 #combine is the summation of the 2 updated strings, these are the name1 and name2. Name1 and name2 being combined here are the
                        #two strings that been removed all the same letters they have.

count = 0
for j in combine: 
    if j in alphabet:
        count += 1

#for the look-a-like FLAMES
list_items = [ "K1", "K2", "K3", "K4", "K5", "K6"] #set a list of list_items, consisting the K1-K6
index = 0 #set initial for index
while len(list_items) > 1: #while the count of items in list are greater than 1, it will continue to this loop but if only one item left in the list_item, this while loop, will stop
    for i in range(count): 
        index += 1 
        if index > len(list_items): #but if the index is greater than the count of items in list, it will
            index = 1 #make the index as 1
    list_items.remove(list_items[index-1]) #whenever the index stops on the items in the list, it will be remove until only one item left in the list_items
    index -= 1 #as we remove it, we'll subtract 1 from the index that means we have accomplished the 1 count from it

#to know the meaning of the items in list_items...     
if list_items == ["K1"]:
    result = "Kaibigan" 
elif list_items == ["K2"]: 
    result = "Kapuso"
elif list_items == ["K3"]: 
    result = "Kaaway"
elif list_items == ["K4"]: 
    result = "Kasal"
elif list_items == ["K5"]:
    result = "Kilig(crush)" 
elif list_items == ["K6"]:
    result = "Kapatid" 

print("Relationship Status : ", result) #to tell the user the result, this will be the output


