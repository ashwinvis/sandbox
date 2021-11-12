import re


# FIXME:
pattern_regex_comments = r"""
(?#Filename and location)([^:^\n]+):(\d+):(\d+):\n{,3}
(?#Source code)(\s*?(\d+?)\ \|(.*?)$\n\s*?\|(.*?\d)\n)
(?#Reason)^(Warning|Error):\ (.*)$
"""

exp_re_com = re.compile(pattern_regex_comments, re.MULTILINE)

# NOTE: This works!

pattern_python_comments = r"""
(?P<file>[^:^\n]+):(?P<line_nb>\d+):(?P<col>\d+):\n{,3}              # Filename and location: file, line_nb, col
(?P<L>\s*?(\d+?)\ \|(?P<source>.*?)$\n\s*?\|(?P<mark>.*?\d)\n\.*?)*  # Source code: L, source, mark
^(?P<level>Warning|Error):\ (?P<msg>.*)                              # Reason: level, msg
"""

exp_py_com = re.compile(pattern_python_comments, re.MULTILINE | re.VERBOSE)
