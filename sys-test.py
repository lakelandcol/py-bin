import sys

a = "Collin"
b = "Alec"
c = "Roger"

list = [a, b, c]

for name in list:
  print name
  if name == b:
	sys.exit(0)

