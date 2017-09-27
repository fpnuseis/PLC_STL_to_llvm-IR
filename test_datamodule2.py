import copy

k = []


def loop_ (var_, count, i) :

    if count != i :
        var_[count] = True
        var_t = copy.copy(var_)
        var_[count] = False
        var_f = copy.copy(var_)

        result_t = (var_t[0] | var_t[1] | var_t[2]) & ( (var_t[1] | var_t[3]) & var_t[0] ) & var_t[4]
        result_f = (var_f[0] | var_f[1] | var_f[2]) & ( (var_f[1] | var_f[3]) & var_f[0] ) & var_f[4]

        st_t = str(var_t[0]) + " " + str(var_t[1]) + " " + str(var_t[2]) + " " + str(var_t[3]) + " " + str(var_t[4]) + " : " + str(result_t) 
        st_f = str(var_f[0]) + " " + str(var_f[1]) + " " + str(var_f[2]) + " " + str(var_f[3]) + " " + str(var_f[4]) + " : " + str(result_f) 

        print('-----')
        print(st_t)
        print(st_f)
        print('-----')

        if result_t != result_f :
            k.append(i)
            

    else :
        count = count + 1

        if len(var_) == count :
            return
        
        loop_(var_,count,i)
        return

    count = count + 1

    if len(var_) == count :
        return

    
    loop_(var_t, count, i)
    loop_(var_f, count, i)

    return

var_ = [True, True, True, True, True]

for i in range ( 0, len(var_) ) :
    var_[i] = True
    var_t = copy.copy(var_)
    var_[i] = False
    var_f = copy.copy(var_)

    loop_(var_t, 0, i)
    loop_(var_f, 0, i)
    
    print("=============")

    var_ = [True, True, True, True, True]

print (k)
