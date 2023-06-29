import string
import numpy as np
import queue as Q
from operator import itemgetter, attrgetter


def Readfile(data, t_slice, command):
    filename = input("輸入檔名:")
    filename += ".txt"
    with open(filename) as f:
        while True :
            temp = f.readline()
            if len(temp) == 0 :
                break
            else :
                temp = str(temp).split()
                if len(temp) != 0 :
                    data.append(temp)
                
                
        methon = data[0][0]
        t_slice = data[0][1]

        
        # print(data)
        del data[0]
        del data[0]
        for i in range(len(data)) :
            data[i] = list(map(int,data[i]))
            data[i].append(False) 
        

    return int(t_slice), int(methon), filename


def WriteFile(data, WTL, TTL, GCL, name, col_name):
    name += "_Output.txt"
    GCL = Converse(GCL)
    with open(name, 'w') as outfile:
        outfile.write(col_name[1]+'\n')
        for i in range(len(GCL)):
            outfile.write(str(GCL[i]))
        outfile.write("\n===========================================================\n"+"\nWaiting Time\n")
        for i in range(len(col_name)):
            outfile.write(col_name[i]+'\t')
        outfile.write("\n===========================================================\n")
        for i in range(len(data)):
            outfile.write(str(data[i][0])+'\t'+str(WTL[i])+'\n')
        outfile.write("===========================================================\n"+"\nTurnaround Time\n")
        for i in range(len(col_name)):
            outfile.write(col_name[i]+'\t')
        outfile.write("\n===========================================================\n")
        for i in range(len(data)):
            outfile.write(str(data[i][0])+'\t'+str(TTL[i])+'\n')
        


def WriteFileALL(data, WTL, TTL, GCL, WTL2, TTL2, GCL2, WTL3, TTL3, GCL3, WTL4, TTL4, GCL4, WTL5, TTL5, GCL5, name, col_name):
    name += "_Output.txt"
    GCL = Converse(GCL)
    GCL2 = Converse(GCL2)
    GCL3 = Converse(GCL3)
    GCL4 = Converse(GCL4)
    GCL5 = Converse(GCL5)

    with open(name, 'w') as outfile:
        outfile.write('All\n')
        outfile.write("==\t   "+col_name[1]+"=="+'\n')
        for i in range(len(GCL)):
            outfile.write(str(GCL[i]))
        outfile.write("\n==\t   "+col_name[2]+"=="+'\n')
        for i in range(len(GCL2)):
            outfile.write(str(GCL2[i]))
        outfile.write("\n==\t   "+col_name[3]+"=="+'\n')
        for i in range(len(GCL3)):
            outfile.write(str(GCL3[i]))
        outfile.write("\n==\t   "+col_name[4]+"=="+'\n')
        for i in range(len(GCL4)):
            outfile.write(str(GCL4[i]))
        outfile.write("\n==\t   "+col_name[5]+"=="+'\n')
        for i in range(len(GCL5)):
            outfile.write(str(GCL5[i]))

        outfile.write("\n===========================================================\n"+"\nWaiting\n")
        for i in range(len(col_name)):
            outfile.write(col_name[i]+'\t')
        outfile.write("\n===========================================================\n")
        for i in range(len(data)):
            outfile.write(str(data[i][0])+'\t'+str(WTL[i])+'\t'+str(WTL2[i])+'\t'+str(WTL3[i])+'\t'+str(WTL4[i])+'\t'+str(WTL5[i])+'\n')
        outfile.write("===========================================================\n"+"\nTurnaround Time\n")
        for i in range(len(col_name)):
            outfile.write(col_name[i]+'\t')
        outfile.write("\n===========================================================\n")
        for i in range(len(data)):
            outfile.write(str(data[i][0])+'\t'+str(TTL[i])+'\t'+str(TTL2[i])+'\t'+str(TTL3[i])+'\t'+str(TTL4[i])+'\t'+str(TTL5[i])+'\n')
        outfile.write("===========================================================")


def Converse(num) :
    letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(num)):
        if num[i] != '-' and num[i] > 9 :
            num[i] = letter[num[i]-10]
    return num   



def FCFS(data):
    data.sort(key = itemgetter(2, 0)) #use arrival time sorted
    # print(data)
    time = 0 
    num = 0
    WT = 0
    TT = 0
    WTL = list()
    TTL = list()
    GCL = list()
    while num in range(len(data)) :
        if time >= data[num][2] :
            WT = time - data[num][2]
            time = time + data[num][1]
            TT = WT + data[num][1]
            data[num].append(WT)
            data[num].append(TT)
            for i in range(data[num][1]) :
                GCL.append(data[num][0])
            num += 1
        else: 
            GCL.append('-')
            time = time + 1
    ## 寫檔操作
    data.sort(key = itemgetter(0)) #use arrival time sorted
    for i in range(len(data)):
        WTL.append(data[i][5])
        TTL.append(data[i][6])
        
    # print(data)
    return WTL, TTL, GCL


def SRTF(data, t_slice):
    num = 0
    time = 0 
    wait_time = 0
    turn_time = 0
    count = 0
    cball = 0
    time = 0
    temp_brust = 0
    wait = list()
    do = list()
    gantt_chart = list()
    done = list()
    WTL = list()
    TTL = list()
    mdata = list()
    
    for i in range(len(data)):
        temp = [data[i][0], data[i][1], data[i][2], data[i][3], False] #list 才不會被覆蓋
        mdata.append(temp)
        
    for i in range(len(mdata)) :
        cball = cball + mdata[i][1]
        a = mdata[i][1]
        mdata[i].append(a)
           
    while time <= cball+100 :
        for i in range(len(mdata)):  #時間到了丟進來
            if time == mdata[i][2]:
                num = num +1 
                # print('time =', time, 'and No', data[i][0], 'put into wait')
                wait.append(mdata[i])
                
        # if time == 0 and len(wait) == 0 :
        #     gantt_chart.append('-')          
            
        wait.sort(key = itemgetter(1, 2, 0)) #按照burst time > arrivaltime > id
        
        if len(do) == 0 and len(wait) != 0 :   #空了丟到作業list
            # print('time =', time, 'and No', wait[0][0], 'put into do', len(wait))
            do.append(wait[0])
            temp_brust = wait[0][1]
            del(wait[0])
        
            
        if len(do) != 0 :
            if temp_brust > t_slice :   # brust > slice
            
                if count < t_slice :   # 做slice次

                    gantt_chart.append(do[0][0])  #甘特圖
                    do[0][1] = do[0][1] - 1   #burst
                    # print(do[0][0],'burst', do[0][1])
                    count = count + 1             #計錄跑幾次
                if count == t_slice :   #做完slice次,未做完丟回等待區
                    # print(do[0][0],'burst', do[0][1],'else')
                    wait.append(do[0])
                    count = 0
                    del(do[0])

            else:   # brust <= slice
                if count < temp_brust :   # 做brust次

                    gantt_chart.append(do[0][0])  #甘特圖
                    do[0][1] = do[0][1] - 1   #burst
                    count = count + 1             #計錄跑幾次
                if count == temp_brust :
                    turn_time = time - do[0][2] +1 
                    # print( turn_time, wait_time,'------')
                    # print( wait_time, time, do[0][2])
                    # print('time =', time, 'id', do[0][0], 'wait', wait_time)
                    for i in range(len(mdata)):
                        if do[0][0] == mdata[i][0] :
                            # print( turn_time, wait_time, data[i][5],'+++1') 
                            wait_time = turn_time - mdata[i][5]
                            # print( turn_time, wait_time, data[i][1],'+++2') 
                            
                    do[0][4] = True
                    do[0].append(wait_time)
                    do[0].append(turn_time)
                    done.append(do[0])
                    count = 0
                    del(do[0])
        else :
            if num < len(data) :
                gantt_chart.append('-')
                    
        time = time + 1
    
    done.sort(key = itemgetter(0))

    for i in range(len(done)):
        WTL.append(done[i][6])
        TTL.append(done[i][7])
        
    return WTL, TTL, gantt_chart


def HRRN(data, t_slice):
    time = 0 
    wait_time = 0
    turn_time = 0
    count = 0
    cball = 0
    time = 0
    temp_brust = 0
    response = 0
    num = 0 
    wait = list()
    do = list()
    gantt_chart = list()
    done = list()
    WTL = list()
    TTL = list()
    mdata = list()

    for i in range(len(data)):
        temp = [data[i][0], data[i][1], data[i][2], data[i][3], False] #list 才不會被覆蓋
        mdata.append(temp)

    # data.sort(key = itemgetter(0))
    for i in range(len(mdata)) :
        cball = cball + mdata[i][1]
        a = mdata[i][1]
        mdata[i].append(a)
        mdata[i].append(response)
        
    while time <= cball+100 :
        for i in range(len(mdata)):  #時間到了丟進來
            if time == mdata[i][2]:
                num = num +1 
                # print('time =', time, 'and No', data[i][0], 'put into wait')
                wait.append(mdata[i])
                
            
        wait.sort(key = itemgetter(2, 0)) #按照arrivaltime > id
    
        if len(do) == 0 and len(wait) != 0 :   #空了丟到作業list
            # print('time =', time, 'and No', wait[0][0], 'put into do', len(wait))
            for i in range(len(wait)) :   # 算response
                response = (time - wait[i][2] + wait[i][1] ) / wait[i][1] # ((time - arrival) + brust) /brust
                wait[i][6] = response


                    
            wait.sort(key = itemgetter(2))    
            wait.sort(reverse=True, key = itemgetter(6))
            # for i in range(len(wait)):
                # print(time,'i am list for wait', wait[i][0])
                
            do.append(wait[0])
            # print( 'do = ', do[0][0])
            temp_brust = wait[0][1]
            del(wait[0])
            
        if len(do) != 0 :
            if count < temp_brust :   # 做brust次
                gantt_chart.append(do[0][0])  #甘特圖
                do[0][1] = do[0][1] - 1   #burst
                count = count + 1             #計錄跑幾次
            if count == temp_brust :
                turn_time = time - do[0][2] +1 
                # print( turn_time, wait_time,'------')
                # print( wait_time, time, do[0][2])
                # print('time =', time, 'id', do[0][0], 'wait', wait_time)
                for i in range(len(mdata)):
                    if do[0][0] == mdata[i][0] :
                        # print( turn_time, wait_time, data[i][5],'+++1') 
                        wait_time = turn_time - mdata[i][5]
                        # print( turn_time, wait_time, data[i][1],'+++2') 
                        
                do[0][4] = True
                do[0].append(wait_time)
                do[0].append(turn_time)
                done.append(do[0])
                count = 0
                del(do[0])

        else:
            if num < len(data):
                gantt_chart.append('-')
            
        time = time + 1
    
    done.sort(key = itemgetter(0))

    for i in range(len(done)):
        WTL.append(done[i][7])
        TTL.append(done[i][8])
        

        
    return WTL, TTL, gantt_chart


def RR(data, ts):
    mdata = list()
    stack = list()
    WTL = list()
    TTL = list()
    GCL = list()

    for i in range(len(data)):
        temp = [data[i][0], data[i][1], data[i][2], data[i][3], False] #list 才不會被覆蓋
        mdata.append(temp)

    mdata.sort(key = itemgetter(2, 0))
    data.sort(key = itemgetter(2, 0)) #同步位置

    time = 0 
    cball = 0
    count = 0
    cend = False
    run = [-1, -1, -1, -1, False]
    brun = False
    cbt = 0
    for i in range(len(mdata)) :
        cball += mdata[i][1]
        mdata[i].append(int(0)) #WT
        mdata[i].append(int(0)) #TT

    #q = Q.Queue(maxsize = cball)

    while time in range(cball+100) :
        for k in range(len(mdata)):
            cbt = mdata[k][1]
            if time >= mdata[k][2] and mdata[k][1] > 0 and mdata[k][4] == False :
                mdata[k][4] = True  #已在list內
                for i in range(ts):
                    if run[0] == mdata[k][0]: brun = True
                    elif cbt > 0: 
                        stack.append(mdata[k])
                        cbt -= 1
        if brun: 
            cbt = run[1]
            for h in range(ts):
                if cbt > 0:
                    stack.append(run)
                    cbt -= 1
            brun = False
        if len(stack) != 0 :
            run = stack[0]
            del stack[0] 
            if len(stack) != 0:
                if stack[0][0] != run[0] : run[4] = False #從list拿出
            else: run[4] = False
            run[1] -= 1 # cpu burst time - 1
            run[2] = run[2]+1 # arrival time + 1
            GCL.append(run[0])
            #print(run, end=' ')
            for s in range(len(mdata)):
                if run[0] == mdata[s][0]:

                    if run[1] == 0: 
                        mdata[s][5] = (time+1) - mdata[s][2]
                        mdata[s][6] = mdata[s][5] + data[s][1]
                    mdata[s][1] = run[1]
                    mdata[s][2] = run[2]
                    #print(mdata[s])
                    break
            #for s in range(stack.__len__()):
            #del stack[0]

        else: GCL.append('-')

        i = 0
        while i in range(len(mdata)) :
            if mdata[i][1] == 0:
                count+=1
            i+=1
        if count >= len(mdata): 
            cend = True
        if cend: 
            time = cball+99
            
        count = 0
        time += 1 

    for i in range(len(mdata)):
        data[i].append(mdata[i][5]) #WT
        data[i].append(mdata[i][6]) #TT

    ## 寫檔操作
    data.sort(key = itemgetter(0)) #use arrival time sorted
    for i in range(len(mdata)):
        WTL.append(data[i][5])
        TTL.append(data[i][6])
        
    return WTL, TTL, GCL
    #print(mdata)

def PPRR(data, t_slice):
    time = 0 
    wait_time = 0
    turn_time = 0
    count = 0
    cball = 0
    time = 0
    temp_brust = 0
    change = 0 
    num = 0
    wait = list()
    do = list()
    gantt_chart = list()
    done = list()
    WTL = list()
    TTL = list()
    mdata = list()
    
    for i in range(len(data)):
        temp = [data[i][0], data[i][1], data[i][2], data[i][3], False] #list 才不會被覆蓋
        mdata.append(temp)

    for i in range(len(mdata)) :
        cball = cball + mdata[i][1]
        a = mdata[i][1]
        mdata[i].append(a)
           
    while time <= cball+100 :
        for i in range(len(mdata)):  #時間到了丟進來
            if time == mdata[i][2]:
                num = num +1
                # print('time =', time, 'and No', data[i][0], 'put into wait')
                wait.append(mdata[i])
                
        # if time == 0 and len(wait) == 0 :
        #     gantt_chart.append('-')          
            
       
        wait.sort(key = itemgetter(3, 2, 0)) #按照burst time > arrivaltime > id
    
                
        if len(do) == 0 and len(wait) != 0 :   #空了丟到作業list
            # print('time =', time, 'and No', wait[0][0], 'put into do', len(wait))
            count2 = 0 
            for i in range(len(wait)) :     #計算有幾個一樣
                if wait[0][3] == wait[i][3] :
                    count2 = count2 +1


            # print(time, 'count', count2, 'change', change, 'id', wait[0][0])
            
            if count2 > 1 :
                if wait[0][4] == False :
                    change = 0
                    
                do.append(wait[change])
                temp_brust = wait[change][1]
                del(wait[change])
                change = change +1 
            else :
                # print(time, 'wait' ,wait[0])
                do.append(wait[0])
                temp_brust = wait[0][1]
                del(wait[0])                
                
            if change == count2 and count2 > 1 :
                change = 0 
                
 
            
        
            
        if len(do) != 0 :
            if temp_brust > t_slice :   # brust > slice
                if count < t_slice :   # 做slice次
                    gantt_chart.append(do[0][0])  #甘特圖
                    # print(time, do[0][0])
                    do[0][1] = do[0][1] - 1   #burst
                    count = count + 1             #計錄跑幾次
                if count == t_slice :   #做完slice次,未做完丟回等待區
                    wait.append(do[0])
                    count = 0
                    do[0][4] = True
                    del(do[0])

            else:   # brust <= slice
                if count < temp_brust :   # 做brust次
                    gantt_chart.append(do[0][0])  #甘特圖
                    # print(time, do[0][0])
                    do[0][1] = do[0][1] - 1   #burst
                    count = count + 1             #計錄跑幾次
                if count == temp_brust :
                    turn_time = time - do[0][2] +1 
                    for i in range(len(mdata)):
                        if do[0][0] == mdata[i][0] :

                            wait_time = turn_time - mdata[i][5]
                            
                    do[0][4] = True
                    do[0].append(wait_time)
                    do[0].append(turn_time)
                    done.append(do[0])
                    count = 0
                    del(do[0])

        else:
            if num < len(data) :
                gantt_chart.append('-')  
            
        time = time + 1
    
    done.sort(key = itemgetter(0))

    for i in range(len(done)):
        WTL.append(done[i][6])
        TTL.append(done[i][7])
    

    return WTL, TTL, gantt_chart


def DEL56data(data):
    for i in range(len(data)):
        del data[i][6]
        del data[i][5]


if __name__ == "__main__" :
    data = list()
    command = int()
    ts = int()
    ts, command, name = Readfile(data, ts, command)
    
    WT = list()
    TT = list()
    GanntChart = list()
    col_name = list()

    if command == 1:
        col_name = ["ID", "FCFS"]
        WT, TT, GanntChart = FCFS(data)
        WriteFile(data, WT, TT, GanntChart, name, col_name)
    elif command == 2:
        col_name = ["ID", "RR"]
        WT, TT, GanntChart = RR(data, ts)
        WriteFile(data, WT, TT, GanntChart, name, col_name)
    elif command == 3:
        col_name = ["ID", "SRTF"]
        WT, TT, GanntChart = SRTF(data,1)
        WriteFile(data, WT, TT, GanntChart, name, col_name)
    elif command == 4:
        col_name = ["ID", "PPRR"]
        WT, TT, GanntChart = PPRR(data, ts)
        WriteFile(data, WT, TT, GanntChart, name, col_name)
    elif command == 5:
        col_name = ["ID", "HRRN"]
        WT, TT, GanntChart = HRRN(data, 1)
        WriteFile(data, WT, TT, GanntChart, name, col_name)
    elif command == 6:
        WT2 = list()
        TT2 = list()
        GanntChart2 = list()
        WT3 = list()
        TT3 = list()
        GanntChart3 = list()
        WT4 = list()
        TT4 = list()
        GanntChart4 = list()
        WT5 = list()
        TT5 = list()
        GanntChart5 = list()
        col_name = ["ID", "FCFS", "RR", "SRTF", "PPRR", "HRRN"]
        WT, TT, GanntChart = FCFS(data)
        DEL56data(data)
        WT2, TT2, GanntChart2 = RR(data, ts)
        DEL56data(data)
        WT3, TT3, GanntChart3 = SRTF(data, 1)

        WT4, TT4, GanntChart4 = PPRR(data, ts)

        WT5, TT5, GanntChart5 = HRRN(data, 1)

        WriteFileALL(data, WT, TT, GanntChart, WT2, TT2, GanntChart2, WT3, TT3, GanntChart3, WT4, TT4, GanntChart4, WT5, TT5, GanntChart5, name, col_name)
