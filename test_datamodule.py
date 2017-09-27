import copy

result_ = ['', '', '', '', '']

def loop_ (var_, count) :
    print (count)

    var_[count] = True
    var_t = copy.copy(var_)
    var_[count] = False
    var_f = copy.copy(var_)

    result_t = (var_t[0] | var_t[1] | var_t[2]) & ( (var_t[1] | var_t[3]) & var_t[0] ) & var_t[4]
    result_f = (var_f[0] | var_f[1] | var_f[2]) & ( (var_f[1] | var_f[3]) & var_f[0] ) & var_f[4]

    st_t = str(var_t[0]) + " " + str(var_t[1]) + " " + str(var_t[2]) + " " + str(var_t[3]) + " " + str(var_t[4]) + " : " + str(result_t) 
    st_f = str(var_f[0]) + " " + str(var_f[1]) + " " + str(var_f[2]) + " " + str(var_f[3]) + " " + str(var_f[4]) + " : " + str(result_f) 

    result_[count] = result_[count] + st_t + '\n' + st_f + '\n'

    count = count + 1

    if len(var_) == count :
        return
    
    loop_(var_t, count)
    loop_(var_f, count)

    return

loop_([True, True, True, True, True], 0)


print (result_)


print ( '=====' )


for i in range(0,5) :
    print (i)

    print (result_[i])
    
