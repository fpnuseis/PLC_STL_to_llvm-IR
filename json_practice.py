import json

def gen_parsetree(st_list):
    res = ['RLO']
    for i in range(0,len(st_list)):
        if(st_list[i][0]=='A('):
            idx = 0
            for j in range(i+1,len(st_list)):
                if(st_list[j][0]==')'):
                    idx = j
                    break
            tmp = ['or']
            for j in range(i+1,idx):
                tmp.extend([st_list[j][1]])
            res.extend(['and',tmp])
        if(st_list[i][0]=='='):
            res = ([res] ,'=',st_list[i][1])
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
if(parsed[0][0]=='A' and parsed[1][0]=='O'):
    parsed = [parsed[0]] + [['O',parsed[0][1]]] + parsed[1:len(parsed)]
    parsed[0] = ['A(']
    for i in range(1,len(parsed)):
        if(parsed[i][0]!='O'):
            parsed = parsed[0:i] + [[')']] + parsed[i:len(parsed)]

print(parsed)
gen_parsetree(parsed)
print(json.dumps(gen_parsetree(parsed),indent=2))
