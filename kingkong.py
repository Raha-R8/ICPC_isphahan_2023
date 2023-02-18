n = int(input())

instructions = []
for index in range(n):
    inp = input() + "E"
    instructions += [inp]
for i in range(n):
    #current instruction
    instruc = instructions[i]
    impossible = False
    seconds = 0 
    count = 0
    # check each instruction
    for j in range(len(instruc)):
        found = False
        # change starting point and create string
        strn = ""
        for k in range(j,len(instruc)):
            indistinctive = False
            strn += instruc[k]

            # check to see if string exists in other strings;

            # if it does, the string is not distinctive
            # if it doesn't then seconds = len
            # an instruction is impossible only when it is not distinctive if King Kong wakes up at a particular position that makes strn from that char to E indistinctive.
            for h in range(n):
                if h != i:
                    if strn in instructions[h]:
                        indistinctive = True
                        if "E" in strn and "E" != strn:
                            impossible = True

                        break

            if not indistinctive:
                seconds+= len(strn)
                count+=1
                found = True
                break
    
    if impossible:
        print("Impossible")
    else:
        print("%.6f" %float(seconds/count))