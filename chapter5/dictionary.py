# Dictionary is a collection of key value pairs
myDict = {
    "Fast":"In a Quick Manner",
    "Manifest": "to show something clearly, through signs or actions",
    "Marks": [1, 2, 5],
    1: 2
}
#Dictionary methods
print(myDict["Fast"])
print(myDict["Manifest"])
print(myDict["Marks"])
print(type(myDict.keys())) # print the keys of the dictionary
print(list(myDict.values()))# print the values of the dictionary
print(myDict.items)
print(myDict)
#update dictionary by adding key- value pairs from updateDict
updateDict = {
    "Lovish" : "Friend",
    "Python" : "Language"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("Python"))

