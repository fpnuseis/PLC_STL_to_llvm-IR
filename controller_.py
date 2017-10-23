def convert (input_) :
    operator = input_[0]
    label = input_[1]
    print(input_)
    print ('label : ' + str(label))

    llvm_operator, register, status = operation_mapper(operator)

    if register == 'none' :
        llvm = llvm_operator + ' ' + label + '\n'
    else :
        llvm = ''
        llvm += '%cond = icmp eq i32 ' + register + ', ' + str(status) + '\n'
        llvm += 'br i1 %cond, label %IfEqual, label %IfUnEqual\n'
        llvm += 'IfEqual :\n'
        llvm += llvm_operator + ' ' + label + '\n'

    return llvm

def operation_mapper (operator) :
    table = {
         # jump function
        'JU' : ['jmp', 'none', 0],    # jump
        'JL' : ['jmp', 'none', 0],    # jump
        'JC' : ['jmp', 'RLO', 1],    # jump if RLO = 1
        'JCN' : ['jmp', 'RLO', 0],   # jump if RLO = 0
        'JBI' : ['jmp', 'BR', 1],   # jump if BR = 1
        'JNBI' : ['jmp', 'BR', 0],  # jump if BR = 0
        'JO' : ['jmp', 'OV', 1],    # jump if OV = 1
        'JOS' : ['jmp', 'OS', 1],   # jump if OS = 1
        # call function
        'CC' : ['call', 'RLO', 1],
        'UC' : ['call', 'none', 0]
    }

    return table[operator][0], table[operator][1], table[operator][2]
