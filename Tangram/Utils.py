# main contributor: Kennard

import os

def exeParse(arg1, arg2):
    print("start")
    cmd = "./Tangram.exe " + str(arg1) + " " + str(arg2)  # Windows
    #cmd = "./Tangram " + str(arg1) + " " + str(arg2)  # Linux
    data = os.popen(cmd).readlines()

    anslist = []

    for line in data:
        line = line.strip('\n').split()

        graphlist = []
        for graphics in line:
            vertlist = []
            for vert in graphics:
                vertlist.append(int(vert))

            graphlist.append(vertlist)

        anslist.append(graphlist)

    print(anslist)
    return anslist
