import re

# TODO Network, Label
# TODO Input handling

def Parser(text) :
    instructions = []
    
    lines = text.split("\n")
    isTarget = -1
    for x in lines :
        if(x==''):
          continue
        # processing string
        x = x.strip()
        pat = re.compile('\s+')
        x = pat.sub(' ',x) 
        # remove last ; & append to instructions
        if (x[len(x)-1]==";") :
            instructions.append(x[:-1].split(" "))
            
        
    return instructions

def CodeExtractor(filename) :
    output_ = []
    idx = -1
    f = open(filename, "r")
    line = f.readline()
    block_name = line.strip().split(" ")[0]
    while(line):
        line = line.strip()
        if( line == "BEGIN" ) :
            while(line):
                line = f.readline()
                line = line.strip()
                if("TITLE" in line):
                    pass
                elif(line=="NETWORK"):
                    idx+=1
                    output_.append('')
                elif(line=="END_"+block_name):
                    break
                else:
                    output_[idx]+=line.strip()+"\n"
        line = f.readline()
    f.close()
    return output_,block_name

res, block_name = CodeExtractor('./math.txt')

for i in range(0,len(res)):
  print(Parser(res[i]))