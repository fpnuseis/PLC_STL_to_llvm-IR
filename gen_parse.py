import Parser
import json

res, block_name = Parser.CodeExtractor('./math.txt')

input = Parser.Parser(res[1])
bit_table = ['A','A(','O','O(',')','=','AN']

def gen_tree(input_):
	inst = []
	res = 'RLO'
	#remove label name
	for i in range(0,len(input_)):
		if(input_[i][0][-1:]!=':'):
			inst.append(input_[i])
		else:
			inst.append(input_[i][1:])
	#check bit operation
	for i in range(0,len(inst)):
		if(inst[i][0] in bit_table):
			if(inst[i][0]=='A'):
				res = ['AND']+[res]+[inst[i][1]]
				print(json.dumps(res,indent=4))


gen_tree(input)