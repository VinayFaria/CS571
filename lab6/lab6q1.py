# @author: vinay
import subprocess
import sys

BINARY = './lab6q1' #Enter your name of c program in place of lab6q1

# check if argument are passed; else exit with message
if len(sys.argv) != 2:
    print('Usage: batchStringProcess inputFile')
    sys.exit(-1)
    
try:
    with open(sys.argv[1]) as file:
        inpstr = file.read()
        foo = inpstr.split()
        for x in foo:
            cmd = BINARY + ' ' + x.strip()
            #print(cmd)
            subprocess.run(cmd.split())
except FileNotFoundError as fnf_error:
    print(fnf_error)