""" 
problem: 
1) Create a class named "PowerSource". Where will be a function named "engine". 
2) Create a class named "Auto" where three functions "wheel", "break", and "accelerator" will be there. 
3) Then inherit the class "PowerSource" to class "Auto". So basically engine func will come from "PowerSource" to "Auto". There will be no "engine" function in the "Auto" class.
4) Then show the output.
"""


class PowerSource:
  def __init__(self, name):
    self.name = name

  def func_engine(abc):
    print(abc.name + " engine is okay.")

class Auto(PowerSource):
  def __init__(self, name):
    self.name = name

  def func_wheel(abc):
    print(abc.name + " wheel is okay.")

  def func_break(abc):
    print(abc.name + " break is okay.")

  def func_accelerator(abc):
    print(abc.name + " accelerator is okay.")

p1 = Auto("BMW")
p2 = Auto("Toyota")
p3 = Auto("Audi")

p1.func_engine()
p1.func_wheel()
p1.func_break()
p1.func_accelerator()

p2.func_engine()
p2.func_wheel()
p2.func_break()
p2.func_accelerator()

p3.func_engine()
p3.func_wheel()
p3.func_break()
p3.func_accelerator()