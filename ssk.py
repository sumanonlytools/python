"""# import modules
import tkinter as tk

# object of tkinter
# and background set for light grey
master = tk.Tk()
master.configure(bg='light grey')

# create label
l = tk.Label(master,
             text="vi",
             bg="red")

# apply cget()
print("Label text: ", l.cget("text"))

l.pack()
master.mainloop()

def greet(func): # higher-order function 
    return func("Hello")

def uppercase(text): # function to be passed
    return text.upper()

print(greet(uppercase))


def green(func):
    return func("hello")

def uppercase(text):
    return text.upper()

print(green(uppercase))



a=int(input ("Enter your number: "))
b=int(input ("Enter your number: "))
x=int(input("Enter your choice 1.add 2.sub 3.mul 4.div: "))

if(x==1):
  print( "your sum is ",(a+b))
elif(x==2):
  print("your subtraction is ",(a-b))
elif(x==3):
   print("your multiplication is ",(a*b))
elif(x==4):
   print("your division is ",(a/b))


mylist=[]
mylist.append("hello")



mylist.append("hello, hi")
mylist.append("hello hi, there")



for x in mylist:
  print(x)



from tkinter import *
import tkinter as tk
root=Tk()
root.geometry("400x400")
root.title("calculator")
one=tk.StringVar()


def osaka():
  name=one.get()
  print(name)
  global osaka1
  osaka1=one.set(one)

 
 


label = tk.Label(root,textvar=osaka1)
label.pack()
entry = tk.Entry(root,textvar=one)
entry.pack()

Button(root,text='submit',command=osaka).pack()





root.mainloop()



# Program to make a simple 
# login screen  


import tkinter as tk
 
root=tk.Tk()

# setting the windows size
root.geometry("600x400")
 
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()

 
# defining a function that will
# get the name and password and 
# print them on the screen
def submit():

    name=name_var.get()
    password=passw_var.get()
    
    print("The name is : " + name)
    print("The password is : " + password)
    
    
    
    
# creating a label for 
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
 
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
 
# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
 
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
 
# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)
 
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
 
# performing an infinite loop 
# for the window to display
root.mainloop()



x = []
y= ["osaka","tokiyo","kyoto"]



x.extend([20,25,30])

sum1=sum(x)

print(sum1)

def sum():
  print("the result is", a+c)

def sub():
  print("the result is ", a-c)


def operate():

   pass



a=int(input("type the 1 st number:"))

b=input("enter the operator:")

c=int(input("typer the 2nd number:"))

d=input("type = to calculate:")

if d=='=':

      if b=='-':
        sub()

a=[]

 


val=(input("enter the string}"))
hola=val.split()
a.append(hola)

for i in a:
    print(i)

print(hola[1])
print(a[0])

if '+' in hola:
    print("hi there")

a=[6,2,3]
b=[4,5,6]
for i in a:

 for j in b:

   while i==j:

    print("sk")


class calculator:
 def init (self,addition, substruction):


 
class calc:
  def  __init__(self,name,number):
    self.name=name
    self.number=number

calc1=calc("suraj",123)

print(calc1.name)
print(calc1.number)

class Dog:
    

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
dog2= Dog("mickey", 6)
print(dog1.name) 
print(dog2.name) 
dog1.name="sand"
print(dog1.name) 


dog3=Dog("chilly",8)

print(dog3.age)


import tkinter as tk

def get_entry_value():
    value = entry.get()
    print("Entry value:", value)

# Create the Tkinter window
window = tk.Tk()
window.title("Entry Widget Value Retrieval")

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger value retrieval
button = tk.Button(window, text="Get Entry Value", command=get_entry_value)
button.pack()

# Start the Tkinter event loop
window.mainloop()

1.gui window for calculator
2.buttons
3.show input output
4.take input and calculate 
5.show output in gui
"""
