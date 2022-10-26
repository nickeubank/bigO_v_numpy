import random
import numpy as np
import gc
import time

datasize = 1_000
nfind = 100


class CustomerRecord:
    def __init__(self, myid):
        self.myid = myid
        self.somedata = random.randint(0, 999999)
        self.otherdata = random.randint(0, 999999)

    pass


pass


mydict = {}
myvals = [CustomerRecord(n) for n in range(0, datasize)]
for v in myvals:
    mydict[v.myid] = v
pass

nparr = np.array(myvals)
myvals = []
random.shuffle(myvals)

# what random ids we are looking for
find = {random.randrange(datasize) for i in range(0, nfind)}
np_time_total = 0
dict_time_total = 0

# we’re going to setup our boolean yes/no array first...
yn = [nparr[i] in find for i in range(0, datasize)]
np_filter = np.array(yn)

for i in range(ntries):
    gc.collect()
    # clear l3 cache out
    l3cache[l3cache == 0]
    start = time.perf_counter()
    nparr[np_filter]
    end = time.perf_counter()
    np_time_total += end - start
    gc.collect()
    # clear l3 cache out
    l3cache[l3cache == 0]
    start = time.perf_counter()
    temp = set([])
    for k in find:
        temp.add(mydict[k])
        pass
    end = time.perf_counter()
    dict_time_total += end - start
    pass
