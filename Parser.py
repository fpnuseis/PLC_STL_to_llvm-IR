import re

def Parser(text) :
    instructions = []
    
    lines = text.split("\n")

    isTarget = -1
    for x in lines :
        # processing string
        x = x.strip()
        pat = re.compile('\s+')
        x = pat.sub(' ',x) 

        # remove last ; & append to instructions
        if (x[-1]==";") :
            instructions.append(x[:-1].split(" "))
            
        
    return instructions

text = '''A(;
ON      "Data_block_1".m2;
O "Data_block_1".m4;
);
A "Data_block_1".m6;
A(;
ON "Data_block_1".m7;
O "Data_block_1".m8;
);
= "Data_block_1".m5;'''

print ( Parser(text) )
