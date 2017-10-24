def convert (input_) :
    operand_num = len(input_)

    operator = input_[0]
    operand = input_[1:operand_num-1]
    output = input_[operand_num-1]

    llvm_operator = operation_mapper(operator)

    # parameter setting
    param = ''
    for i in operand :
        param += str(i)
    param += ' '

    llvm = (
        output + ' = ' +
        llvm_operator + ' ' +
        param
    )

    return llvm


def operation_mapper (operation) :
    # TODO llvm operation mapper
    table = {
        # 16-bit int math function
        "+I" : "add i16",
        "-I" : "add i16",
        "*I" : "add i16",
        "/I" : "add i16",
        # 32-bit int math function
        "+D" : "add i32",
        "-D" : "sub i32",
        "*D" : "mul i32",
        "/D" : "div i32",
        "MOD" : "urem i32",
        # 32-bit float math function
        "+R" : "add f32",
        "-R" : "sub f32",
        "*R" : "mul f32",
        "/R" : "div f32",
        # ....
        "ABS" : "llvm.fabs", # llvm.* is modified llvm languege
        "SQR" : "llvm.powi",
        "LN" : "llvm.log.f32",
        "SIN" : "llvm.sin.f32",
        "COS" : "llvm.cos.f32",
        # comparison function
        "==D" : "icmp eq i32",
        "<>D" : "icmp ne i32",
        ">=D" : "icmp sge i32",
        "<=D" : "icmp sle i32",
        ">D" : "icmp sgt i32",
        "<D" : "icmp slt i32",
        # comparison function        
        "==R" : "icmp slt f32",        
        "<>R" : "icmp slt f32",        
        ">=R" : "icmp slt f32",        
        "<=R" : "icmp slt f32",       
        ">R" : "icmp slt f32",       
        "<R" : "icmp slt f32"
    }
    return table[operation]
