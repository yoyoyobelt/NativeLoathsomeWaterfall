# function signature -> tap_open_func
def tap_open_func():
  return 'water'

def tap_close_func():
  return ''

variable = tap_open_func() # function call

print('tap_open_func -->', variable)

variable = tap_close_func()

print('tap_close_func -->', variable)

print('---------------------')

def tap_func(open: bool):
  if open == True:
    return 'water'
  elif open == False:
    return ''


true_variable = tap_func(True)

print("tap_func -->", true_variable)

false_variable = tap_func(False)

print("tap_func -->", false_variable)

'''

what is a function definition
any function has params
any function needs to be called or triggered
every language has its own syntax writing style
  - snake_case
  - kebab-case
  - CamelCase
  - pascalCase
each function has to have a single responsability
if conditions
store what functions returns in a variable and use it

'''

print('---------------------')

def signature(number):
  return 'joe ' + str(number)

number_of_papers = 10

for paper_number in range(number_of_papers):
  print(signature(paper_number))

print('---------------------')

def tap_water(temp : bool, waterintensity):
  if temp == True:
    for i in range(waterintensity):
      print("hot water")
      
  elif temp == False:
    for i in range(waterintensity):
      print("cold water")


tap_water(temp=False, waterintensity=3)

print('---------------------')

def tap_water(temperature, water_intensity):
  if temperature == 'hot' and water_intensity >= 0:
    for i in range(water_intensity):
      print("hot water")
      
  elif temperature == 'cold'and water_intensity >= 0:
    for i in range(water_intensity):
      print("cold water")

  else:
    print("your option is invalid\nPick either 'hot' or 'cold' and a number between 0 and 5")


tap_water(temperature='hot', water_intensity=10000)

