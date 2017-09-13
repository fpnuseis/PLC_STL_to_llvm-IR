def modifier (input_path) :
    output_ = ""
    a = 1
    z = 0

    f = open(input_path, "r")
    line = f.readline()
    while line :
        line = line.strip("\n")
        if line == "BEGIN" :
             while line:
                line = f.readline()
                line = line.strip("\n")
                if line == "NETWORK":
                    pass
                elif "TITLE" in line:
                    pass
                elif "END_ORGANIZATION_BLOCK" in line:
                    pass
                elif "a" + str(a) in line:
                    word1,word2 = line.split(" ", 1)
                    if word1 == "a" + str(a) + ":":
                        a = a + 1
                        output_ += word2.strip() + "\n"
                    else:
                        output_ += line.strip() + "\n"
                elif "Label_" + str(z) in line:
                    word1,word2 = line.split(" ",1)
                    if word1 == "Label_" + str(z) + ":":
                        z = z + 1
                        output_ += word2.strip() + "\n"
                    else:
                        output_ += line.strip() + "\n"
                else:
                    output_ += line.strip() + "\n"
        line = f.readline()
    f.close()

    return output_

print(modifier("../math.txt"))
