import numpy as np
import pandas as pd
def getData():
    file = open("Propuski_zanyatiy.csv","r", encoding='utf-8')
    data=file.read()
    file.close()

    x=y=count=0

    trayning=[[]]
    answ=[]

    data=data[data.find('\n')+1:]

    while(True):
        y=data.find('\n',x)
        if y==-1:
            break
        string=data[x:y]
        x=y+1
        x1=y1=0
        while True:
            y1=string.find(',',x1)
            if y1==-1:
                answ.append(int(string[y1:]))
                trayning.append([])
                count+=1
                break
            trayning[count].append(int(string[x1:y1]))
            x1=y1+1

    trayning.pop()
    test=trayning[::]
    answ_test=answ[::]

    trayning=trayning[:len(trayning)-100]
    answ=answ[:len(answ)-100]

    # for i in range(len(test)):
    #     print(test[i],"|",answ_test[i])

    # print("\n\n",trayning[len(trayning)-1])
    # print(len(test))
    # print(len(trayning))

    trayning_np=np.zeros((len(trayning),len(trayning[0])))
    answ_np=np.zeros((len(answ)))
    test_np=np.zeros((len(test),len(test[0])))
    answ_test_np=np.zeros((len(answ_test)))

    for i in range(len(trayning)):
        for j in range(len(trayning[0])):
            trayning_np[i][j]=trayning[i][j]

    for i in range(len(test)):
        for j in range(len(test[0])):
            test_np[i][j]=test[i][j]

    for i in range(len(answ)):
        answ_np[i]=answ[i]

    for i in range(len(answ_test)):
        answ_test_np[i]=answ_test[i]
    return trayning_np, answ_np, test_np, answ_test_np
getData()
def get_data_wanted():
    file = open("New_f.csv", "r", encoding='utf-8')
    data = file.read()
    file.close()

    x = y = count = 0

    trayning = [[]]
    answ = []

    data = data[data.find('\n') + 1:]

    while (True):
        y = data.find('\n', x)
        if y == -1:
            break
        string = data[x:y]
        x = y + 1
        x1 = y1 = 0
        while True:
            y1 = string.find(',', x1)
            if y1 == -1:
                answ.append(int(string[y1:]))
                trayning.append([])
                count += 1
                break
            trayning[count].append(int(string[x1:y1]))
            x1 = y1 + 1

    trayning.pop()
    numbers = []
    for i in range(len(trayning)):
        numbers.append(trayning[i][0])
    print (numbers)
    trayning_np= np.zeros((len(trayning), len(trayning[0])))
    answ_np = np.zeros((len(answ)))

    for i in range(len(trayning)):
        for j in range(len(trayning[0])):
            trayning_np[i][j]=trayning[i][j]
    for i in range(len(answ)):
        answ_np[i]=answ[i]

    return numbers

get_data_wanted()

