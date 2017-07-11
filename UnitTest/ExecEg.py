from queue import PriorityQueue
from PythonStudy import *

pyton_sourc = """\
SEVENTEEN=17

def three():
    return 3
"""
# global_namespace = {}
# exec(pyton_sourc, global_namespace)
# print(global_namespace)
# print(global_namespace['SEVENTEEN'])
# print(global_namespace['three'])
#
# print([global_namespace[y] for x, y in enumerate(global_namespace)])

a = TemplateEngine.CodeBuilder(40)
print(a.indent_level)
