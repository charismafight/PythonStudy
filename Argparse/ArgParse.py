import argparse

p = argparse.ArgumentParser(description='this is my description of py file,consider this file as a command')
p.add_argument('integers', type=int, help='this is a gorgeous language', nargs=2)
p.add_argument('--foo', action='store_const', const=42)
myargs = p.parse_args('--foo'.split())
print(myargs.integers[0] * myargs.integers[1])
