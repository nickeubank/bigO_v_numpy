class CustomerRecord:
 6  def __init__(self, myid):
 7    self.myid = myid
 8    self.somedata = random.randint(0,999999)
 9    self.otherdata = random.randint(0,999999)
10    pass
11  pass


mydict = {}
17  myvals = [ CustomerRecord(n) for n in range(0,datasize)]
18  for v in myvals:
19    mydict[v.myid] = v
20    pass
21  nparr = np.array(myvals)
22  myvals= []
23  random.shuffle(myvals)
24  #what random ids we are looking for                         
25  find = { random.randrange(datasize) for i in range(0, nfind)}
26  np_time_total = 0
27  dict_time_total = 0

#we’re going to setup our boolean yes/no array first...               
29  yn=[nparr[i] in find for i in range(0, datasize)]
30  np_filter = np.array(yn)

for i in range(ntries):
34    gc.collect()
35    #clear l3 cache out                               
36    l3cache[l3cache ==0]
37    start = time.perf_counter()
38    nparr[np_filter]
39    end = time.perf_counter()
40    np_time_total += end - start
41    gc.collect()
42    #clear l3 cache out                               
43    l3cache[l3cache ==0]
44    start = time.perf_counter()
45    temp = set([])
46    for k in find:
47      temp.add(mydict[k])
48      pass
49    end = time.perf_counter()
50    dict_time_total += end - start
51    pass