#!/usr/bin/env python
import shutil
from string import ascii_uppercase

import click
import paraview.simple as pv


def fix_line(line, imports):
    for attr in imports:
        #  if attr in line:
        try:
            idx = line.index(attr)
            # Check if the subsitution was already made
            # And only write if either:
            # - attr is in the beginning of the line
            # - or is preceded by a space
            if line[idx - 3: idx] != "pv." and (
                idx == 0 or line[idx - 1] == " "
            ):
                line = line.replace(attr, f"pv.{attr}")
        except ValueError:
            pass

    return line


@click.command()
@click.argument("script")
def rm_pv_imports(script):
    """
    Fixes imports of SCRIPT as a result of

    >>> from paraview.simple import *

    """

    shutil.copy2(script, script + ".orig")
    imports = [
        attr
        for attr in dir(pv)
        if any(attr[0] == upper_case for upper_case in ascii_uppercase)
    ]
    imports.sort(key=lambda word: len(word))

    with open(script + ".orig", "r") as fp, open(script, "w") as new_fp:
        for line in fp.readlines():
            if not line.startswith("#"):
                if line == "from paraview.simple import *":
                    line = "import paraview.simple as pv"
                else:
                    line = fix_line(line, imports)

            new_fp.write(line)


if __name__ == "__main__":
    rm_pv_imports()
