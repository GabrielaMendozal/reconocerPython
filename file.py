num1 = 42 #Numbers
num2 = 2.3# Numbers
boolean = True #Boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tupla
print(type(fruit))  #type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #access value
person['name'] = 'George' #add value
person['eye_color'] = 'blue' #add value
print(fruit[2]) # tupla access value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")   #conditional if else

if len(string) < 5:        #conditional if elif else
    print("It's a short word!")
elif len(string) > 15:    #length check
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):   #for
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0  #while loop start
while(x < 5):   #while loop
    print(x)
    x += 1  #increment

pizza_toppings.pop() #eliminar ultimo elemento del arreglo 
pizza_toppings.pop(1)# eliminar el valor indice 1 del arreglo