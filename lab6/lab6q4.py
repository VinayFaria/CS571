# @author: vinay
from statistics import mean

def whatever(infilename):
    f = open(infilename, 'r' )
    for line in f:
        alnum_list = line.split()
        dummy = []
        for i in alnum_list:
            try:
                dummy.append(int(i))
            except IOError:
                #errno, strerror = e.args
                #print("I/O error({0}): {1}".format(errno,strerror))
                pass
            except ValueError:
                #print("Not valid integer!")
                pass
        print('Sum {0} and mean {1} of {2} without alphabet '.format(sum(dummy), mean(dummy), line[:len(line)-1]))
print('file input_a')
infilename = 'input_a'
whatever(infilename)
print('file input_b')
infilename = 'input_b'
whatever(infilename)