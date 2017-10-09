import re

# hardcoded
reg_expr = ".+#.+"
p = re.compile(reg_expr)

# input_ is array of parameters
def detection (block_name, network, input_) :
    for i in input_ :
        # !!
        if p.match(i) != False :
            print ("false")

        print ("true")
        return block_name, network, i, True

    return block_name, network, input_, False


a,b,c,d = detection ('block1', 'network1',["sdsd", "asda", "fgsd", "DINT#11", "efqf"])

print(a)
print(b)
print(c)
print(d)
