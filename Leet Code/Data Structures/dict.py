from audioop import avg
from unicodedata import name


def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

print(get_hash('march 22'))

class HashTable:
    def __init__(self):
        self.MAX = 100 
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX


    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False 
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                print(idx, element) 
                self.arr[h] [idx] = (key, val)
                found = True 
                break 
        if not found:
            self.arr[h].append(key, val)

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1] 

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index] 


t = HashTable()
t['march 6'] = 130 
t['march 1'] = 20 
t['dec 17'] = 27 

print(t['march 6']) 

# 1. The best data structure to use here was a list because all 
# we wanted was access of temperature elements
arr = []

with open("nyc_weather.csv", "r") as sheet:
    for line in sheet:
        lines = line.split(',')
        try:
            temperature = int(lines[1])
            arr.append(temperature)
        except:
            print("Invalid temperature")
print(arr) 

#i.
avg_temp = sum(arr[0:7]) / len(arr[0:7])

#ii.
max_temp = max(arr[0:10]) 

#2. The best data structure to use here was a dictionary (internally a hash table) 
# because we wanted to know temperature for specific day, requiring key, value pair 
# access where you can look up an element by day using O(1) complexity
weather = {}

with open("nyc_weather.csv", "r") as sheet:
    for line in sheet:
        lines = line.split(',')
        days = lines[0] #key 
        try:
            temperature = int(lines[1])
            weather[days] = temperature # value is temperature 
        except:
            print("Invalid temperature") 

#i.
print("The temperature on January 9th was,", weather['Jan 9']) 

#ii.
print("The temperature on January 4th was,", weather['Jan 4'])

#3. 
with open("poem.txt") as poem:
    for line in poem:
        print(line) 

word_count = {}

with open("poem.txt", "r") as poem:
    for line in poem:
        lines = line.split(' ')
        for char in lines:
            char = char.replace('\n', '')
            if char in word_count:
                word_count[char] += 1 
            else:
                word_count[char] = 1 


mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict["name"] 

try:
    mydict["lastname"]
except:
    print("Error")

for value in mydict.values():
    print(value)  

for key, value in mydict.items():
    print(key, value) 

my_dict_2 = dict(name="Mary", age=27, city="Boston") 
print(my_dict_2)

