import math_
# import counter
import controller_
# import bitlogic

InstructionList = {
    # Math Libarary
    "+I" : "math",
    "-I" : "math",
    "*I" : "math",
    "/I" : "math",
    "+D" : "math",
    "-D" : "math",
    "*D" : "math",
    "/D" : "math",
    "MOD" : "math",
    "+R" : "math",
    "-R" : "math",
    "*R" : "math",
    "/R" : "math",
    "ABS" : "math",
    "SQR" : "math",
    "LN" : "math",
    "SIN" : "math",
    "COS" : "math",
    "==D" : "math",
    "<>D" : "math",
    ">=D" : "math",
    "<=D" : "math",
    ">D" : "math",
    "<D" : "math",
    # BitLogic Library
    "AND" : "bitlogic",
    "OR" : "bitlogic",
    "=" : "bitlogic",
    # Controller Library
    "JU" : "controller",
    "JL" : "controller",
    "JC" : "controller",
    "JCN" : "controller",
    "JBI" : "controller",
    "JNBI" : "controller",
    "JO" : "controller",
    "JOS" : "controller",
    "CC" : "controller",
    "UC" : "controller"
    # Counter Library
}

def Mapper (input_) :
    instruction = input_[0]

    if instruction in InstructionList:
        if InstructionList[instruction] == 'math' :
            result = math_.convert(input_)

        elif InstructionList[instruction] == 'bitlogic' :
            result = bitlogic.convert(input_)

        elif InstructionList[instruction] == 'controller' :
            result = controller_.convert(input_)

    #    elif InstructionList[instruction] == 'counter' :
    #        result = counter.convert(input_)
    else :
        error = "error:non-defined instruction"
        return error

    return result
