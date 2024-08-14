""" 
problem: 
1) First create a list, where it will be ["Audi","BMW","Ford"].
2) Then print for all input one by one by elements of list . You can use foreach. 
3) After that you take a input from user . If user take an input for example "toyota" print also for that. 
4) In addition please add constructor/init all class. You can print a normal message like "Auto production". But please use a constructor which is important
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

new_carbrand = input()

car_list.append(new_carbrand)

print(car_list)

foreach x in car_list:
    {
        print(x)
        
        """p1 = Auto(x)
        p1.func_engine()
        p1.func_wheel()
        p1.func_brake()
        p1.func_accelerator()"""
    }




"""p1 = car_list(0)
p2 = car_list(1)
p3 = car_list(2)
p4 = car_list(3)

p1.func_engine()
p1.func_wheel()
p1.func_brake()
p1.func_accelerator()

p2.func_engine()
p2.func_wheel()
p2.func_brake()
p2.func_accelerator()

p3.func_engine()
p3.func_wheel()
p3.func_brake()
p3.func_accelerator()

p4.func_engine()
p4.func_wheel()
p4.func_brake()
p4.func_accelerator()"""