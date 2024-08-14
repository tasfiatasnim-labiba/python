""" 
problem: 
1) Create a class named "PowerSource". Where will be a function named "engine". 
2) Create another class named "Auto" where three functions "wheel", "brake", and "accelerator" will be there. 
3) Then inherit the class "PowerSource" to class "Auto". So basically engine func will come from "PowerSource" to "Auto". There will be no "engine" function in the "Auto" class.
4) In addition please add constructor/init to all class. You can print a normal message like "Auto production".
5) Create a list, where it will be ["Audi","BMW","Ford"].
6) Then print all the elements of the list.
7) After that take an input from user. If user take an input for example "Toyota" print also for that.
"""

class PowerSource:
  def __init__(self, name):
    self.name = name

  #defining function to check engine
  def func_engine(abc):
    print(abc.name + " engine is okay.")

class Auto(PowerSource):
  def __init__(self, name):
    self.name = name

  #defining function to check wheel
  def func_wheel(abc):
    print(abc.name + " wheel is okay.")

  #defining function to check brake
  def func_brake(abc):
    print(abc.name + " brake is okay.")

  #defining function to check accelerator
  def func_accelerator(abc):
    print(abc.name + " accelerator is okay.")

car_list = ["Audi", "BMW", "Ford"]

print(car_list)

new_carbrand = input()

#adding new item to the list
car_list.append(new_carbrand)

for x in car_list:
    print(x)
    p1 = Auto(x)
    p1.func_engine()
    p1.func_wheel()
    p1.func_brake()
    p1.func_accelerator()