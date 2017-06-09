import argparse

p = argparse.ArgumentParser(description='this is my description of py file,consider this file as a command')
p.add_argument('integers',type=int,help='this is a gorgeous language')
myargs = p.parse_args()
print(myargs.integers**2)
