import re
from .CodeBuilder import CodeBuilder


class Templite(object):
    def __init__(self, text, *context):
        """Construct a templite with the ginven 'text'
        context are dictionaries of values to use for future rendering
        These are good for filters and global values
        """
        self.context = {}
        self.context.update(context)

        self.all_vars = set()
        self.loop_vars = set()

        code = CodeBuilder()

        code.add_line("def render_function(context,do_dots):")
        code.indent()
        vars_code = code.add_section()
        code.add_line("result=[]")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")

        buffered = []

        def flush_output():
            """Force buffered to the code builder."""
            if len(buffered) == 1:
                code.add_line("append_result(%s)", buffered[0])
            elif len(buffered) > 1:
                code.add_line("extend_result(%s)", ",".join(buffered))
            else:
                del buffered[:]

        ops_stack = []
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
