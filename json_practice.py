import json

def gen_parsetree(st_list):
    res = ['RLO']
    for i in range(0,len(st_list)):
        params = st_list[i]
        op = st_list[i][0]
        if(op=='A'):
            if(len(res)!=1):
                res = [res]
            res.extend(['*',params[1]])
        elif(op=='='):
            if(len(res)!=1):
                res = [res]
            res.extend(['=',params[1]])
        elif(op=='O'):
            if(len(res)!=1):
                res = [res]
            res.extend(['or',['RLO','*',params[1]]])
    return res;

def Parser(text, begin, end, data_split,remove_indent) :
    instructions = []
    lines = text.split("\n")
    isTarget = -1
    for x in lines :
        x = x.strip()
        instructions.append(x[:-1].split(" "))
    return instructions[1:-1]

text = '''
A "Data_block_1".m2;
O "Data_block_1".m4;
O "Data_block_1".m6;
O "Data_block_1".m8;
= "Data_block_1".m5;
'''

print (text)
parsed =  Parser(text,"TITLE=","NETWORK",";",True)
print(parsed)
print(len(parsed))
print(json.dumps(gen_parsetree(parsed),indent=2))
