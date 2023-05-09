#Author: Andre Costa

from contextlib import redirect_stdout
import traceback
import io
import os
import fileinput
from mooshak_helper import MooshakHelper
import builtins
from glob import glob

#import main
import importlib



use_colors = True
try:
    from colorama import Fore
    from colorama import Style
except ImportError:
    use_colors  = False


orig_print = builtins.print
orig_input = builtins.input

passedAllTests = True
firstTest = True

for file in sorted(os.listdir("testes/in")):
    print("Testing", file)

    input_lines=[]
    with fileinput.input(files=('testes/in/' + file)) as f:
        for line in f:
            input_lines.append(line)

    mh = MooshakHelper(input_lines)
    builtins.input = mh.input

    f = io.StringIO()

    diff=False

    try:
        with redirect_stdout(f):
            if firstTest:
                main = importlib.import_module("main")
                firstTest = False
            else:
                main.main()

    except Exception as e:
        #Get exception info
        err = traceback.format_exc()
        if use_colors:
            print(f"{Fore.RED}ERROR:", err, f"{Style.RESET_ALL}",end="")
        else:
            print("ERROR:", err, end="")

        error_line, cmmnd =  mh.get_last_cmmnd()
        print("Failed on test", file, \
              "on command:", "\"" + cmmnd.strip() + "\"", ", line:", error_line, end="\n")

        diff=True
        passedAllTests=False

    s = f.getvalue()
    output_lines = s.split("\n")
    if "" in output_lines:
        output_lines.remove("")

    #Add \n to every line
    aux = []
    for l in output_lines:
        aux.append(l + "\n")
    output_lines = aux

    expected_lines = []
    teste_out = file.replace("in","out")
    with fileinput.input(files=('testes/out/' + teste_out)) as f:
        for line in f:
            expected_lines.append(line)


    if len(output_lines) != len(expected_lines):
        print("Expecting", len(expected_lines), "lines, got", len(output_lines))
        diff=True
        passedAllTests=False

    else:
        for i in range(len(expected_lines)):
            if(output_lines[i] != expected_lines[i]):
                print("Line", i, "is different")
                print("Expecting:\n", [expected_lines[i]])
                print("Got:\n", [output_lines[i]])

                diff=True
                passedAllTests=False

    if not diff:
        if use_colors:
            print(f"{Fore.GREEN}Passed test!{Style.RESET_ALL}")
        else:
            print("Passed test!")
    print("\n")

if passedAllTests:
    if use_colors:
        print(f"{Fore.GREEN}Passed all tests!{Style.RESET_ALL}")
    else:
        print("Passed all tests!")



builtins.input = orig_input 
