""" 
problem: 
1) Create a class named "PowerSource". Where will be a function named "engine". 
2) Create a class named "Auto" where three functions "wheel", "brake", and "accelerator" will be there. 
3) Then inherit the class "PowerSource" to class "Auto". So basically engine func will come from "PowerSource" to "Auto". There will be no "engine" function in the "Auto" class.
4) Then show the output.
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

p1 = Auto("BMW")
p2 = Auto("Toyota")
p3 = Auto("Audi")

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