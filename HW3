import string
import numpy as np

def Readfile():
    filename = input("輸入檔名 : ")
    filename += ".txt"
    with open(filename) as f:
        data = f.read().splitlines()
        size = int(data[0])
        page = list(map(int,data[1]))
    
    return size, page, filename



def Change(data) :
    result = []
    for letter in data :
        result.append(letter)
    
    return result



def Reverse(data):
    
    for i in range(len(data)) :
        data[i].reverse()

    return data



def FIFO(page,size):
    execution = []
    process = []
    fault = []
    replace = 0
    isreplace = False
    
    for num in page :
        isreplace = False
        if len(execution) != 0 :
            for i in range(len(execution)) :
                if execution[i] == num :
                    isreplace = True
                    fault.append('T')
                    temp = Change(execution)
                    process.append(temp)
                    break
        
        
        if isreplace == False :
            if len(execution) == size :    
                replace += 1
                execution.append(num)
                del execution[0]
                fault.append('F')
                temp = Change(execution)
                process.append(temp)
                    
            elif len(execution) < size :
                fault.append('F')
                execution.append(num)
                temp = Change(execution)
                process.append(temp)
        
            else:
                print('error')
            
    return process, fault, replace
            


def LRU(page,size):
    execution = []
    process = []
    fault = []
    replace = 0
    isreplace = False
    
    for num in page :
        isreplace = False         
        if len(execution) != 0 :
            for i in range(len(execution)) :
                if execution[i] == num :
                    isreplace = True
                    fault.append('T')
                    del execution[i]
                    execution.append(num)
                    temp = Change(execution)
                    process.append(temp)
                    break
                    
        if isreplace == False :
            if len(execution) == size : 
                replace += 1
                execution.append(num)
                del execution[0]
                fault.append('F')
                temp = Change(execution)
                process.append(temp)
                    
            elif len(execution) < size :
                fault.append('F')
                execution.append(num)
                temp = Change(execution)
                process.append(temp)
    
            else:
                print('error')
            
        
            
    return process, fault, replace







def LFU_FIFO(page,size):
    tnum = 0
    execution = []
    process = []
    fault = []
    frequece = []
    replace = 0
    isreplace = False
    
    for num in page :
        isreplace = False
        if len(execution) != 0 :
            for i in range(len(execution)) :
                if execution[i] == num :
                    isreplace = True
                    fault.append('T')
                    temp = Change(execution)
                    process.append(temp)
                    frequece[i] += 1
                    break
                    
        if isreplace == False :
            if len(execution) == size :
                replace += 1
                tnum = frequece.index(min(frequece))
                del frequece[tnum]
                del execution[tnum]
                execution.append(num)
                fault.append('F')
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            elif len(execution) < size :
                fault.append('F')
                execution.append(num)
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            else:
                print('error')
            
    return process, fault, replace



def MFU_FIFO(page,size):
    tnum = 0
    execution = []
    process = []
    fault = []
    frequece = []
    replace = 0
    isreplace = False
    
    for num in page :
        isreplace = False
        if len(execution) != 0 :
            for i in range(len(execution)) :
                if execution[i] == num :
                    isreplace = True
                    fault.append('T')
                    temp = Change(execution)
                    process.append(temp)
                    frequece[i] += 1
                    break
                   
        if isreplace == False :
            if len(execution) == size : 
                replace += 1
                tnum = frequece.index(max(frequece))
                del frequece[tnum]
                del execution[tnum]
                execution.append(num)
                fault.append('F')
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            elif len(execution) < size :
                fault.append('F')
                execution.append(num)
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            else:
                print('error')
            
    return process, fault, replace



def LFU_LRU(page,size):
    tnum = 0
    execution = []
    process = []
    fault = []
    frequece = []
    replace = 0
    isreplace = False
    
    for num in page :
        isreplace = False
        if len(execution) != 0 :
            for i in range(len(execution)) :
                if execution[i] == num :
                    execution.append(num)
                    frequece[i] += 1
                    frequece.append(frequece[i])
                    del execution[i]
                    del frequece[i]
                    isreplace = True
                    fault.append('T')
                    temp = Change(execution)
                    process.append(temp)
                    break
                    
        if isreplace == False :
            if len(execution) == size : 
                replace += 1
                tnum = frequece.index(min(frequece))
                del frequece[tnum]
                del execution[tnum]
                execution.append(num)
                fault.append('F')
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            elif len(execution) < size :
                fault.append('F')
                execution.append(num)
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            else:
                print('error')
            
    return process, fault, replace



def MFU_LPR(page,size):
    tnum = 0
    execution = []
    process = []
    fault = []
    frequece = []
    replace = 0
    isreplace = False
    
    for num in page :
        isreplace = False
        if len(execution) != 0 :
            for i in range(len(execution)) :
                if execution[i] == num :
                    execution.append(num)
                    frequece[i] += 1
                    frequece.append(frequece[i])
                    del execution[i]
                    del frequece[i]
                    isreplace = True
                    fault.append('T')
                    temp = Change(execution)
                    process.append(temp)
                    break
                    
        if isreplace == False :
            if len(execution) == size :
                replace += 1
                tnum = frequece.index(max(frequece))
                del frequece[tnum]
                del execution[tnum]
                execution.append(num)
                fault.append('F')
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            elif len(execution) < size :
                fault.append('F')
                execution.append(num)
                temp = Change(execution)
                process.append(temp)
                frequece.append(0)
                
            else:
                print('error')
            
    return process, fault, replace


def Writefile(size, page, filename, process, fault, replace, process2, fault2, replace2, process3, fault3, replace3
              , process4, fault4, replace4, process5, fault5, replace5, process6, fault6, replace6):
    
    filename = 'out_' + filename
    with open(filename, 'w') as outfile:
        outfile.write("--------------FIFO-----------------------\n")
        for i in range(len(page)):
            outfile.write(str(page[i]) + '\t')
            for j in range(len(process[i])) :
                outfile.write(str(process[i][j]))
                
            if fault[i] == 'F' :
                outfile.write('\t' + 'F' + '\n')
            else:
                outfile.write('\n')
        
        outfile.write('Page Fault = ' + str(fault.count('F')) + '  Page Replaces = ' + str(replace) + '  Page Frames = ' + str(size) + '\n\n')
        
        outfile.write("--------------LRU-----------------------\n")
        for i in range(len(page)):
            outfile.write(str(page[i]) + '\t')
            for j in range(len(process2[i])) :
                outfile.write(str(process2[i][j]))
                
            if fault2[i] == 'F' :
                outfile.write('\t' + 'F' + '\n')
            else:
                outfile.write('\n')
        
        outfile.write('Page Fault = ' + str(fault2.count('F')) + '  Page Replaces = ' + str(replace2) + '  Page Frames = ' + str(size) + '\n\n')
        
        outfile.write("--------------Least Frequently Used Page Replacement-----------------------\n")
        for i in range(len(page)):
            outfile.write(str(page[i]) + '\t')
            for j in range(len(process3[i])) :
                outfile.write(str(process3[i][j]))
                
            if fault3[i] == 'F' :
                outfile.write('\t' + 'F' + '\n')
            else:
                outfile.write('\n')
        
        outfile.write('Page Fault = ' + str(fault3.count('F')) + '  Page Replaces = ' + str(replace3) + '  Page Frames = ' + str(size) + '\n\n')
        
        outfile.write("--------------Most Frequently Used Page Replacement-----------------------\n")
        for i in range(len(page)):
            outfile.write(str(page[i]) + '\t')
            for j in range(len(process4[i])) :
                outfile.write(str(process4[i][j]))
                
            if fault4[i] == 'F' :
                outfile.write('\t' + 'F' + '\n')
            else:
                outfile.write('\n')
        
        outfile.write('Page Fault = ' + str(fault4.count('F')) + '  Page Replaces = ' + str(replace4) + '  Page Frames = ' + str(size) + '\n\n')
        
        outfile.write("--------------Least Frequently Used LRU Page Replacement-----------------------\n")
        for i in range(len(page)):
            outfile.write(str(page[i]) + '\t')
            for j in range(len(process5[i])) :
                outfile.write(str(process5[i][j]))
                
            if fault5[i] == 'F' :
                outfile.write('\t' + 'F' + '\n')
            else:
                outfile.write('\n')
        
        outfile.write('Page Fault = ' + str(fault5.count('F')) + '  Page Replaces = ' + str(replace5) + '  Page Frames = ' + str(size) + '\n\n')

        outfile.write("--------------Most Frequently Used LRU Page Replacement-----------------------\n")
        for i in range(len(page)):
            outfile.write(str(page[i]) + '\t')
            for j in range(len(process6[i])) :
                outfile.write(str(process6[i][j]))
                
            if fault6[i] == 'F' :
                outfile.write('\t' + 'F' + '\n')
            else:
                outfile.write('\n')
        
        outfile.write('Page Fault = ' + str(fault6.count('F')) + '  Page Replaces = ' + str(replace6) + '  Page Frames = ' + str(size)+ '\n')
        
        
        
if __name__ == "__main__" :
    size, page, filename = Readfile()
    
    process, fault, replace = FIFO(page,size)
    Reverse(process)
    
    process2, fault2, replace2 = LRU(page,size)
    Reverse(process2)
    
    process3, fault3, replace3 = LFU_FIFO(page,size)
    Reverse(process3)
    
    process4, fault4, replace4 = MFU_FIFO(page,size)
    Reverse(process4)
    
    process5, fault5, replace5 = LFU_LRU(page,size)
    Reverse(process5)
    
    process6, fault6, replace6 = MFU_LPR(page,size)
    Reverse(process6)

    Writefile(size, page, filename, process, fault, replace, process2, fault2, replace2, process3, fault3, replace3
              , process4, fault4, replace4, process5, fault5, replace5, process6, fault6, replace6)
              
