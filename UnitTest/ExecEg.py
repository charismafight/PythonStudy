from queue import PriorityQueue
from PythonStudy import *
import re

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
text = r"""wo the fu.
attr{{{abc}}}}}}}}}}}}
.\l\ssflja rleiwj
 fd j f{{ssss}}.{{sdfdsf}}dfdsf"""
s = re.split(r'({{.*?}}|{%.*?%}|{#.*?#})', text)
s1 = re.split(r'(?s)({{.*?}}|{%.*?%}|{#.*?#})', text)
print(s)
print(s1)
#
# a = TemplateEngine.CodeBuilder(40)
# print(a.indent_level)
