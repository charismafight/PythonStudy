class CodeBuilder(object):
    """build source code conveniently"""

    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        """add line to the source of the code
        Indentation and new line will be add for you,don't provide them
        """
        self.code.extend([" " * self.indent_level, line, "\n"])

    INDENT_STEP = 4

    def indent(self):
        """Increase the indent for following lines."""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """Decrease the indent for following lines."""
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        """add a section to,a sub-CodeBuilder"""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        return "".join(str(c) for c in self.code)

    def get_global(self):
        """Execute the code,and return a dict of globals  it defined"""
        # A check that the caller really finish all the blocks  they started
        assert self.indent_level == 0
        # Get the python source as a single string
        python_source = str(self)
        # Execute the source,defining globals and return them
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace
