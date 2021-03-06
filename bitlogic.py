def convert (input_) :
    operand_num = len(input_)

    operator = input_[0]
    param = input_[1:operand_num]
    
    llvm_operator = operation_mapper(operator)

    llvm = llvm_operator%tuple(param)
    return llvm


def operation_mapper (operation) :
    # TODO llvm operation mapper
    table = {
        # 16-bit int math function
        "AND" : "%s = AND i1 %s, %s",
        "OR" : "%s = OR i1 %s, %s",
        "=" : "i1 %s = i1 %s",
        "NOT" : "i1 %s = XOR i1 %s 1"
    }
    return table[operation]

# test code
convert(['=','TAG_1','TAG_2'])