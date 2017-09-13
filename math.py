def mapper (input_, operation, output_) :
    input_num = len(input_)

    if input_num == 1 :
        one_parameter (input_, operation, output_)
    elif input_num == 2 :
        print (double_parameter (input_, operation, output_))
    elif input_num == 3 :
        trip_parameter (input_, operation, output_)

def one_parameter (input_, operation, output_) :
    llvm = (
        output_ + ' = ' +
        operation_mapper(operation) + ' ' +
        str(input_[0])
    )

    return llvm

def double_parameter (input_, operation, output_) :
    d_type = "i1"
    llvm = (
        output_ + ' = ' +
        operation_mapper(operation) + ' ' +
        str(input_[0]) + ' ' +
        str(input_[1])
    )

    return llvm

def trip_parameter (input_, operation, output_) :
    d_type = "i1"
    llvm = (
        output_ + ' = ' +
        operation_mapper(operation) + ' ' +
        str(input_[0]) + ' ' +
        str(input_[1]) + ' ' +
        str(input_[2])
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
