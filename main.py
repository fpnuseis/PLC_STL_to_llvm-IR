# mapper

# preprocessing
import Mapper
import Parser

register = {
    # general register
    'BR' : 0,
    'CC1' : 0,
    'CC0' : 0,
    'OV' : 0,
    'OS' : 0,
    'OR' : 0,
    'STA' : 0,
    'RLO' : 0,
    'FC' : 0,
    # counter register
    'C' : 0,
}

class Stack :
    stack = []

    def Loader (self, input_) :
        self.stack.append(input_)

    def ClearStack (self) :
        self.stack = []

    def StackViewer (self) :
        print ('## StackViewer')
        print ('num : ' + str(len(self.stack)))
        for i in self.stack :
            print (i)
    def getStack (self) :
        return self.stack

def run(input_):
    operator = ''
    a = Stack()
    # Stack Excution Test
    count = 0
    for i in input_ :
        if i[0] == 'L' :
            a.Loader(i[1])
            a.StackViewer()

        elif i[0] == 'T' :
            temp = []
            temp.append(operator)
            temp.append(a.getStack())
            temp.append(i[1])
            
            print(Mapper.Mapper(temp))
            a.ClearStack()
        else :
            a.StackViewer()
            print (i)
            if len(a.stack) == 0 :
                print(Mapper.Mapper(i))
            else :
                a.StackViewer()
                print(i)
                operator = i[0]


    a.ClearStack()
    a.StackViewer()

#run([['L','value1'], ['L','value2'], ['L','value3'], ['+D'], ['T','output1'], ['JU', 'label1'], ['JC', 'label2']])

res, block_name = Parser.CodeExtractor('./math.txt')
for i in range(0,len(res)):
  run(Parser.Parser(res[i]))
  print('\n')
