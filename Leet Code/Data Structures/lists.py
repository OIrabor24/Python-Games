expenses = [2200, 2350, 2600, 2130, 2190]

# 1.
diff = expenses[1] - expenses[0]
print(f"in February you spent this much extra compared to January: {diff}")

#2.
q1 = sum(expenses[:3]) 
print(f"The total expenses for the first quarter of the year is", q1)

#3. 2000 in expenses
for month in range(len(expenses)):
    if not month == 2000:
        print("You did not spend 2000 in any given month.")
        break
    else:
        print(month)  

#4. # expenses.append(1980)
expenses.insert(5, 1980) 
print("The additional expense for June is:", expenses[5]) 

#5. 
expenses[3] = expenses[3] - 200 
print("The updated expense for April after processing a refund is:", expenses[3]) 
print("-" * 30) 
print(expenses) 

#Question 2
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

#1.
print("The length of our heros list is", len(heros)) 

#2. 
heros.append("black panther") 
print(heros) 

#3. 
heros.remove("black panther") 
print(heros) 
print("-" * 30) 
heros.insert(3, "black panther")
print(heros) 

#4. 
heros[1:3] = ['doctor strange'] 
print(heros) 

#5. 
heros.sort()
print(heros) 

#Question 3
max_number = int(input("Enter a max number: "))

odd_numbers = []

for i in range(1, max_number):
    if i % 2 == 1:
        odd_numbers.append(i)
print("Odd numbers are: ", odd_numbers) 