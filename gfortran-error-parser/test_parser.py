import pytest
from pathlib import Path
from parser import exp_py_com as exp


@pytest.fixture
def datadir():
    return Path.cwd()


# TODO: Pretty print with rich.traceback.Traceback + rich.console.Console.print

def print_match(match):
    if match['level'] == "Error":
        print(match['level'], end=": ")
        print(
            f"{match['file']}:{match['line_nb']}:{match['col']}\n  ",
            match.group(match.lastindex), "\n",
            match['source']
        )



@pytest.mark.parametrize("log_file", ("warnings_oneline.log", "warnings_error_twoline.log"))
def test_gfortran(datadir, log_file):
    log = (datadir / log_file).read_text()

    for match in exp.finditer(log):
        print_match(match)

    #  print(match[0])
    assert log.endswith(str(match.group(0)) + "\n")
