import re
from .CodeBuilder import CodeBuilder


class Templite(object):
    def __init__(self, text, *context):
        """Construct a templite with the given 'text'
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

        for token in tokens:
            if token.startswith('{#'):
                continue
            if token.startswith('{{'):
                # a expression for evaluate
                expr = self._expr_code(token[2:-2].strip())
                buffered.append("to_str(%s)" % expr)
            elif token.startswith('{%'):
                # action tag;split into words and parse further.
                flush_output()
                words = token[2:-2].strip().split()
                if words[0] == 'if':
                    if len(words) != 2:
                        self._syntax_error("don't understand if", token)
                    ops_stack.append('if')
                    code.add_line('if %s:' % self._expr_code(words[1]))
                    code.indent()
                elif words[0] == 'for':
                    if len(words) != 3:
                        self._syntax_error("don't understand for", token)
                    ops_stack.append('for')
                    self._variable(words[1], self.loop_vars)
                    code.add_line('for c_% in %s:' % (words[1], self._expr_code(words[3])))
                    code.indent()
                elif words[0] == 'end':
                    if len(words) != 1:
                        self._syntax_error("don't understand end", token)
                    end_what = words[0][3:]
                    if not ops_stack:
                        self._syntax_error("has no if or for before end", token)
                    start_what = ops_stack.pop()
                    if start_what != end_what:
                        self._syntax_error("start is different of the end", end_what)
                    code.dedent()
                else:
                    self._syntax_error("error tag", words[0])

