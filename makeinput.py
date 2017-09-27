def modifier (input_path) :
    output_ = []
    idx = -1
    f = open(input_path, "r")
    line = f.readline()
    block_name = line.strip().split(" ")[0]

    tmp = []
    flag = 0
    label = ''

    while(line):
        line = line.strip("\n")
        if (line == "BEGIN") :
            while(line):
                line = f.readline()
                line = line.strip("\n")

                if ("TITLE" in line):
                    pass

                elif (line == "NETWORK"):
                    tmp.append({'label' : label, 'code' : output_})

                    # new network
                    flag = 0
                    output_ = ''
                    label = 'none'

                elif (line == "END_" + block_name):
                    break

                elif (flag == 0 and line.count(':') == 1) :
                    label = line.split(':')[0]
                    line = line.split(':')[1]

                    output_ += line.strip() + "\n"

                    flag = 1

                else :
                    if flag == 0 :
                        flag = 1
                    output_ += line.strip() + "\n"

        line = f.readline()
    f.close()
    return tmp, block_name
