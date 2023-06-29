import threading as td
import multiprocessing as mp
from multiprocessing import Pool
import time
from queue import Queue
from datetime import datetime


def bubblesort(data):
    for i in range(0, len(data) - 1):
        quit = False
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j + 1]:
                quit = True
                data[j], data[j + 1] = data[j + 1], data[j]
        if(quit == False):
            break


def Readfile(data):
    filename = input("輸入檔名:")
    filename += ".txt"
    with open(filename) as f:
        data = f.read().splitlines()
    data = list(map(int, data))
    
    return data, filename



def bubblejob(data, begin, end, queue):
    temp = data[begin:end]
    bubblesort(temp)
    for i in range(len(temp)) :
        queue.put(temp[i])
        
def bubblejob2(data, begin, end, cut):
    long = len(data)
    thds_cut = len(data) // cut
    lis = []
    for i in range(cut):
        temp = data[begin:end]
        bubblesort(temp)
        begin = end
        end = end + thds_cut
        if (long - end) <= (thds_cut // 2):
            end = long
        lis = lis + temp
    return lis

def bubblejob3(data, begin, end):
    temp = data[begin:end]
    bubblesort(temp)
    return temp



def mergejob(data, begin, end, queue):
    temp = data[begin:end]
    merge_sort(temp, 0, (end - begin))
    for i in range(len(temp)) :
        queue.put(temp[i])
    
    
def mergejob2(data, begin, end, cut):
    long = len(data)
    thds_cut = len(data) // cut
    lis = []
    for i in range(cut):
        temp = data[begin:end]
        merge_sort(temp, 0, (end - begin))
        begin = end
        end = end + thds_cut
        if (long - end) <= (thds_cut // 2):
            end = long
        lis = lis + temp
    return lis
    
def mergejob3(data, begin, end):
    temp = data[begin:end]
    merge_sort(temp, 0, (end - begin))
    return temp





def K_Thread_Bubble(data, cut):
    threads = []
    bdata = []
    queue = Queue()
    long = len(data)
    thds_cut = len(data) // cut
    begin = 0
    end = thds_cut

    for i in range(cut):
        threads.append(td.Thread(target=bubblejob, args=(data, begin, end, queue,)))
        threads[i].start()
        begin = end
        end = end + thds_cut
        if (long - end) <= (thds_cut // 2):
            end = long
    for i in range(cut):
        threads[i].join()
    for i in range(len(data)):
        bdata.append(queue.get())


    return bdata




def thread_merge(data, cut):
    threads = []
    b = 0
    num = len(data) // cut
    while( num < len(data) ):
        begin = 0
        end = 0
        for i in range(0,cut,2):
            begin = end
            end = end + num*2
            threads.append(td.Thread(target=merge2, args=(begin, end, data)))
            threads[b].start()
            b = b + 1
            
        num = num *2
        cut = cut // 2

    return data




def One_Process(data, cut):
    data2 = data
    pool = mp.Pool(processes=1)
    long = len(data)
    thds_cut = len(data) // cut
    begin = 0
    end = thds_cut

    mStart = time.time()
    for i in range(cut):
        pool.apply_async(mergejob, (data, begin, end,))
        begin = end
        end = end + thds_cut
        if (long - end) <= (thds_cut // 2):
            end = long
    mEnd = time.time()

    begin = 0
    end = thds_cut
    tStart = time.time()
    for i in range(cut):
        pool.apply_async(bubblejob, (data2, begin, end,))
        begin = end
        end = end + thds_cut
        if (long - end) <= (thds_cut // 2):
            end = long
    tEnd = time.time()
    return (tEnd - tStart), (mEnd - mStart)


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):

    left_copy = array[left_index:middle + 1]
    right_copy = array[middle + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index


    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1

        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1


        sorted_index = sorted_index + 1


    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

def merge2(begin, end, array):

    right_index = 0;
    left_index = 0;
    merged_index = 0;
    mid = (begin + end) // 2
    right_array = array[begin:mid]
    left_array = array[mid:end]
    
    while right_index < len(right_array) and left_index < len(left_array):
        if(right_array[right_index] < left_array[left_index]):
            array[merged_index+begin] = right_array[right_index]
            right_index = right_index + 1
        else:
            array[merged_index+begin] = left_array[left_index]
            left_index = left_index + 1
    
        merged_index = merged_index + 1
    
    while right_index < len(right_array):
        array[merged_index+begin] = right_array[right_index]
        right_index = right_index + 1
        merged_index = merged_index + 1
    
    while left_index < len(left_array):
        array[merged_index+begin] = left_array[left_index]
        left_index = left_index + 1
        merged_index = merged_index + 1





if __name__ == "__main__":
    data = []
    data, name = Readfile(data)
    command = int(input("輸入數字選擇任務1~4 "))
    
    if command == 1:
        Start = time.time()
        bubblesort(data)
        End = time.time()
    

        outname =  name[0:len(name)-4] + "_output1.txt"
        f = open(outname, 'w')
        f.write('Sort : \n')
        for number in data:
            f.write(str(number)+'\n')
        date = str(datetime.now()).split()
        
        f.write("CPU Time : %f" % (End - Start) + '\n')
        f.write("Output Time : " + date[0] + ' ' +  date[1] + '+8:00' )
        f.close()
        
    elif command == 2:
        cut = input("請輸入Thread數量:")
        cut = int(cut)
        Start = time.time()
        fdata =  K_Thread_Bubble(data, cut)
        fdata = thread_merge(fdata, cut)
        End = time.time()
    
        outname =  name[0:len(name)-4] + "_output2.txt"
        f = open(outname, 'w')
        f.write('Sort : \n')
        for number in fdata:
            f.write(str(number)+'\n')
        date = str(datetime.now()).split()
        
        f.write("CPU Time : %f" % (End - Start) + '\n')
        f.write("Output Time : " + date[0] + ' ' +  date[1] + '+8:00' )
        f.close()
        
    elif command == 3:
        cut = input("請輸入Process執行數量:")
        cut = int(cut)
        pool = Pool(processes=cut)
        p_fd = []
        processes1 = []
        long = len(data)
        thds_cut = len(data) // cut
        begin = 0
        end = thds_cut
        tStart = time.time()
        for i in range(cut):
            processes1.append(pool.apply_async(bubblejob3, args=(data, begin, end,)))
    
            begin = end
            end = end + thds_cut
            if (long - end) <= (thds_cut // 2):
                end = long
        pool.close()
        pool.join()

        for i in processes1:
            p_fd = p_fd + i.get() 
        p_fd.sort()
        tEnd = time.time()
    
        cut = cut-1
        p_md = []
        mpool = Pool(processes=cut)
        processes2 = []
        Max = len(data)
        thds_k = (data.__len__() // cut)
        begin = 0
        end = thds_k
        mStart = time.time()
        for i in range(cut):
            processes2.append(mpool.apply_async(mergejob3, args=(data, begin, end,)))
    
            begin = end
            end = end + thds_k
            if (long - end) <= (thds_k // 2):
                end = Max
        mpool.close()
        mpool.join()
    
        for _ in processes2:
            p_md = p_md + _.get() 
        
        mEnd = time.time()

        outname =  name[0:len(name)-4] + "_output3.txt"
        f = open(outname, 'w')
        f.write('Sort : \n')
        for number in p_fd:
            f.write(str(number)+'\n')
        date = str(datetime.now()).split()
        
        f.write("CPU Time : %f" % (tEnd - tStart) + '\n')
        f.write("Output Time : " + date[0] + ' ' +  date[1] + '+8:00' )
        f.close()
    
    elif command == 4:
        cut = input("請輸入檔案分割份數(K):")
        cut = int(cut)
        pool = Pool(processes=1)
        data2 = data
        fdata = []
        mdata = []
    
        Start = time.time()
        thds_k = len(data) // cut
        begin = 0
        end = thds_k
        one = pool.apply_async(bubblejob2, args=(data, begin, end, cut,))
        
        fdata = one.get()
        merge_sort(fdata, 0, len(fdata))
        End = time.time()
        
    
        outname =  name[0:len(name)-4] + "_output4.txt"
        f = open(outname, 'w')
        f.write('Sort : \n')
        for number in fdata:
            f.write(str(number)+'\n')
        date = str(datetime.now()).split()
        
        f.write("CPU Time : %f" % (End - Start) + '\n')
        f.write("Output Time : " + date[0] + ' ' +  date[1] + '+8:00' )
        f.close()

