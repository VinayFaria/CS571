# @author: vinay
import subprocess
import sys
# execution of c program
def c_calling():
    try:
        with open(sys.argv[1], encoding="utf8") as file:
            for line in file:
                word_list = line.split()
                for word in word_list:
                    word = alphabet_numbers(word)
                    cmd = BINARY + ' ' + word.strip()
                    #print(cmd)
                    subprocess.run(cmd.split())
    except FileNotFoundError as fnf_error:
        print(fnf_error)
# Removing special character if any
def alphabet_numbers(word):
    if word.isalnum() == True:
        return word
    else:
        dummy = []
        dummy[:0] = word
        list1 = []
        for i in dummy:
            if i.isalnum() == True:
                list1.append(i)
        str1 = ''.join(list1)
    return str1
BINARY = './lab6q1' #Enter your name of c program in place of lab6q1
# check if argument are passed; else exit with message
if len(sys.argv) != 2:
    print('Usage: batchStringProcess inputFile')
    sys.exit(-1)
    
c_calling()