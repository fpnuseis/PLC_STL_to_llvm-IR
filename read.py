def modifier (input_path) :
    output_ = []
    idx = -1
    f = open(input_path, "r")
    line = f.readline()
    block_name = line.strip().split(" ")[0]
    while(line):
        line = line.strip("\n")
        if( line == "BEGIN" ) :
            while(line):
                line = f.readline()
                line = line.strip("\n")
                if("TITLE" in line):
                    pass
                elif(line=="NETWORK"):
                    idx+=1
                    output_.append('')
                elif(line=="END_"+block_name):
                    break
                else:
                    output_[idx]+=line.strip()+"\n"
        line = f.readline()
    f.close()
    return output_,block_name


res = modifier("./math.txt")
print(res)