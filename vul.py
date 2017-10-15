# IF vulnerability is detected return True for all Function
# False mean nice!

import os
import re

# Hardcoded
reg_expr = '.+#.+'
p = re.compile(reg_expr)

# Fucking Hell I didn't have any idea about that...
def ExternDetector (block_list, call_block) :
    for i in block_list :
        if i == call_block :
            print ('False')
            return False

    print ('True')
    return True

def HardcodedDetector (block_name, network, input_) :
    for i in input_ :
        if p.match(i) != False :
            print ('false')

        print ('true')
        return block_name, network, i, True

    return block_name, network, input_, False

# ExternDetector Test Code
test = 'CALL EXTERN' # TODO UC, CC, ...
block_list_ = ['OB1', 'FC1', 'FC2', 'FB1', 'FB2']

para = test.split(' ')
print (para[1])

ExternDetector(block_list_, para[1])

print('===')
# HardcodedDetector Test Code
a,b,c,d = HardcodedDetector ('block1', 'network1',["sdsd", "asda", "fgsd", "DINT#11", "efqf"])

print(a)
print(b)
print(c)
print(d)
