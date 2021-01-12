import math


# change function if given
def formula(x):
  return math.sin(x)

def trap(b1,b2,h):
  area = h*(b1+b2)/2
  return area


# enter manually if values are given
xs = []
ys = []


# total area starts at 0
total_area = 0

# no manually entered x values
if not xs:
  begin = float(input('Enter the x startpoint: '))
  end = float(input('Enter the x endpoint: '))

  # no values for x or y were entered
  if not ys:
    number = int(input('Enter the number of segments: '))
    length = (end-begin)/number

    # store x values
    xs = [begin]
    for i in range(1,number+1):
      xs.append(begin+(length*i))

    # calculate y values
    for x in xs:
      ys.append(formula(x))
  
  # no x values, but y values were entered
  elif ys:
    number = len(ys)-1
    length = (end-begin)/number

  # regular x value lengths
  for i in range(number):
    total_area += trap(ys[i],ys[i+1],length)


# manually entered x values
elif xs:
  # calculate y values if none were entered
  if not ys:
    for x in xs:
      ys.append(formula(x))

  # both x and y values were entered
  elif ys:
    if len(xs) != len(ys):
      raise Exception('number of x values does not equal number of y values')

  number = len(xs)-1

  # irregular x value lengths
  for i in range(number):
    total_area += trap(ys[i],ys[i+1],xs[i+1]-xs[i])


print(total_area)
