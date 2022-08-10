
import requests

# Boundaries. 
value = input(f"Please enter the number of activities from 1-100 : ")
x = int(value)
#if x: 
# BOUNDS = (1,100)
while x < 1 or x > 100:
    value = input("Not between 1-100. Please enter the number of activities from 1-100 : ")
    x = int(value)


url = "http://www.boredapi.com/api/activity/"

# Part 1. 
def generateact(x):
    list_key = []
    list_type = []
    list_data = []
    list_participants = []
    list_price = []
    list_link = []
    list_access = []
    #masterlist = [list_key, list_data, list_type, list_participants, list_price, list_link, list_access]

    for i in range(x):
        Data = requests.get(url)
        json_data = Data.json()
        activity_Key = json_data["key"]
        activity_Type = json_data["type"]
        activity_Data = json_data["activity"]
        activity_Participants = json_data["participants"]
        activity_Price = json_data["price"]
        activity_Link = json_data["link"]
        activity_Accessibility = json_data["accessibility"]
        list_key.append(activity_Key)
        list_type.append(activity_Type)
        list_data.append(activity_Data)
        list_participants.append(activity_Participants)
        list_price.append(activity_Price)
        list_link.append(activity_Link)
        list_access.append(activity_Accessibility)
        
    print(list_key)
    print(list_type)
    print(list_data)
    print(list_participants)
    print(list_price)
    print(list_link)
    print(list_access)
    print("\n")
    longestCharacter(list_data)
    print("\n")
    mostParticipants(list_data, list_participants)
    print("\n")
    checkDups (list_data) 

#Part 2A. Most Participants 
def mostParticipants(list_data, list_participants):
    count = 0
    for i in list_participants:
        if i > count:
            count = i
            activity = list_participants.index(i)
    print(f"Most Participants: " + list_data[activity] + " (participants: " + str(count) + ")")

#Part 2B. Check for Duplicates
def checkDups(list_data):
    notDups = []
    dups = []
    for i in list_data:
        if i not in notDups:
            notDups.append(i)
        else:
            dups.append(i)
    if len(dups) == 0:
        print("-")
    else:
        print(f"Duplicate Activities: " , dups)  

#Part 2C. Most characters in Activity
def longestCharacter(list_data):
    count = 0
    for i in list_data:
        if len(i) > count:
            count = len(i)
            word = i
    print(f"Most characters in Activity: " + word + " (characters: " + str(count) + ")")

#main
generateact(x)
