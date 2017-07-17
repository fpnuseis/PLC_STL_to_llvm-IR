import json

def gen_parsetree(st_list):
    res = 'RLO'
    pre_ins = 'none'
    for i in range(0,len(st_list)):
        if(st_list[i][0]=='A'):
            if(pre_ins[0]=='A'):
                res = res+[st_list[i][1]]
            else:
                res = ['and']+[res]+[st_list[i][1]]
        elif(st_list[i][0]=='A('):
            res = ['and']+[res]
        elif(st_list[i][0]=='O('):
            res = ['or']+[res]
        elif(st_list[i][0]=='O'):
            if(len(st_list[i])==2):
                if(pre_ins[0]=='O'):
                    res[len(res)-1] = res[len(res)-1]+[st_list[i][1]]
                elif(pre_ins=='A('):
                    res = res+[['or']+[st_list[i][1]]]
                else:
                    res = ['or']+[res]+[['or']+[st_list[i][1]]]
        elif(st_list[i][0]=='='):
            res = ['=']+[res]+[st_list[i][1]]
        pre_ins = st_list[i][0]
        
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
A "Tag_1";
A "Tag_2";
A "Tag_3";
O "Tag_2";
O "Tag_3";
= %L20.0;
A %L20.0;
BLD 102;
= "Tag_3";
A %L20.0;
A(;
O "Tag_1";
O "Tag_2";
O "Tag_3";
O "Tag_3";
);
= "Tag_2";
'''

print (text)
parsed =  Parser(text,"TITLE=","NETWORK",";",True)
'''if(parsed[0][0]=='A' and parsed[1][0]=='O'):
    parsed = [parsed[0]] + [['O',parsed[0][1]]] + parsed[1:len(parsed)]
    parsed[0] = ['A(']
    for i in range(1,len(parsed)):
        if(parsed[i][0]!='O'):
            parsed = parsed[0:i] + [[')']] + parsed[i:len(parsed)]'''

print(parsed)
gen_parsetree(parsed)
print(json.dumps(gen_parsetree(parsed),indent=5))
