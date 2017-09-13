def mapper (input_, operation, output_) :
    input_num = len(input_)
    param = ''
    for i in range(0,len(input_)):
        param+=str(input_[i])
        if(i!=len(input_)-1):
            param+=' '

    llvm = (
        output_ + ' = ' +
        operation_mapper(operation) + ' ' + 
        param
    )
    
    return llvm

# depreciated
def data_mapper (input_) :
    # TODO using data block extract data block
    return "i32"

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
        "==D" : "icmp eq",
        "<>D" : "icmp ne",
        ">=D" : "icmp sge",
        "<=D" : "icmp sle",
        ">D" : "icmp sgt",
        "<D" : "icmp slt"
    }
    return table[operation]

mapper([1,2], "MOD", "temp")
