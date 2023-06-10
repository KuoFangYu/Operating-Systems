HW1 程式須實現以下四種方法

1.將N個數目字直接進行BubbleSort,並顯示CPU執行之時間。

2.將個數目字切成K份,並由K個threads分别進行BubbleSort之後,再用thread(s)作MergeSort,並顯示CPU執行之時間。

3.將個數目字切成K份,並由K個processes分别進行BubbleSort之後,再用process(es)作MergeSort並顯示CPU執行之時間。

4.將個數目字切成K份,在一個process內對K份資料進行BubbleSort之後,再用同一個process作MergeSort,並顯示CPU執行之時間


HW2 程式須實現以下五個處理原則

1.處理原則一FCFS
  a.依ArrivalTime先後次序進行排程;
  b.若Arrival Time相同時,則依ProcessID由小至大依序處理。

2.處理原則一RR
  a.依ArrivalTime先後次序進行排序,時候未到的Process不能執行;
  b.若Arrival Time相同時,則依ProcessID由小至大依序處理;
  c.当Timeout時,從佇列尾端開始排序,若有新來的Process,則讓新來的Poce排在前面;
  d.若Process的Time Slice用完就結束時,必須讓下一個Proces執行,擁有完整的timeslice

3.處理原則-SRTF
  a.由剩餘CPUBurst最小的Process先排序;
  b.若剩餘的CPUBurst相同,則依ArrivalTim小的先處理;
  c.若剩餘CPUBurst相里Arrival Time相同,則依ProcessID由小至大依序處理。

4.處理原則一PPRR (Preemptive Priority + Round Robin)
  a.依Priority大小依序處理,Prioritym小的Process代表優先處理;
  b.若Priority相同的Proces不只一個,採用RR原則進行排程:
    1.若有Priority相同的process正在執行中,須等待其時間片段用馨
    2.當Timeout或被Preemptive時,從佇列尾端開始依Priority大小排序,若有新來的Process,則讓新來的Process排在前面

5.處理原則-HRRN (Highest Response Ratio Next)
  a.反應時間比率(Responseatio愈高的Proce優先處理;
  b.若Ratio相的Proces不只一個,則依ArlTime小的先處理;
  c.若Ratio相同里Arrival Time相,依Prce由小至大依序處理。
