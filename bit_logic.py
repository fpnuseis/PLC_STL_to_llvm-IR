import json

# TODO code fixing

result = ""
tmp_count = 1

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
    print (instructions[1:-1])
    print ("====")
    return instructions[1:-1]

def dfs(res, Table) :
    global result
    global tmp_count
    for i in range(1,len(res)):
        if(type(res[i])==type([])):
            sub =  dfs(res[i], Table)
            if(type(sub)==type('a')):
                res[i] = sub
            if(i==len(res)-1):
                tmp_count=1
    if(len(res)>3):
        for i in range(1,len(res)-1):
            if(i==1):
                result+=Table[res[0]][0]%('%TEMP'+str(tmp_count),res[i],res[i+1])+'\n'
            else:
                result+=Table[res[0]][0]%('%TEMP'+str(tmp_count),'%TEMP'+str(tmp_count-1),res[i+1])+'\n'
            tmp_count+=1
    elif(len(res)==3):
        if(Table[res[0]][1]==3):
            result+=Table[res[0]][0]%('%TEMP'+str(tmp_count),res[1],res[2])+'\n'
            tmp_count+=1
        elif(Table[res[0]][1]==2):
            result+=Table[res[0]][0]%(res[1],res[2])+'\n'

    return '%TEMP'+str(tmp_count-1)

def Converter(tree) :
    with open('new_rule.json') as data_file:
        table = json.load(data_file)
    dfs(tree, table)

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
gen_parsetree(parsed)
res = gen_parsetree(parsed)
print(json.dumps(res,indent=8))
Converter(res)

print (result)
