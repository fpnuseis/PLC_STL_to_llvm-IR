import re

# TODO Network, Label
# TODO Input handling

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

# def CodeExtractor(filename) :
    

text = ''' a1:      A(;
      A(;
      O(;
      L "Data_block_1".test_Dint;
      L "Data_block_1".test_Dint1;
      +D;
      T "Data_block_1".test_Dint;
      AN OV;
      SAVE;
      CLR;
      A BR;
      );
      O(;
      L "Data_block_1".test_Dint;
      L "Data_block_1".test_Dint1;
      /D;
      T "Data_block_1".test_Dint;
      AN OV;
      SAVE;
      CLR;
      A BR;
      );
      );
      JNB Label_0;
      L "Data_block_1".test_Dint;
      L "Data_block_1".test_Dint1;
      -D;
      T "Data_block_1".test_Dint;
      AN OV;
      SAVE;
      CLR;
Label_0:      A BR;
      );
      JNB Label_1;
      L "Data_block_1".test_Dint;
      L "Data_block_1".test_Dint1;
      *D;
      T "Data_block_1".test_Dint;
Label_1:      NOP 0;'''

print ( Parser(text) )
