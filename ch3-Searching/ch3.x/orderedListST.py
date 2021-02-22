# This is a client implementation to test symbol tables
import re # for regular expression
import time
class node: 
    def __init__(self,key,value):
        super().__init__()
        self.key=key
        self.value=value
class bsST:
    def __init__(self):
        super().__init__()
        self.arr=[]
    def size(self):
        return len(self.arr)
    def isEmpty(self):
        return True if len(self.arr)==0 else False
    def min(self):
        if(not self.isEmpty()):
            return self.arr[0].key
    def max(self):
        if(not self.isEmpty()):
            return self.arr[-1].key
    def get(self,key):
        idx=self.rank(key)
        if(idx<self.size() and self.arr[idx].key==key):
            return self.arr[idx].value
        return None
    def contains(self,key):
        idx=self.rank(key)
        if(idx<self.size() and self.arr[idx].key==key):
            return True
        return False
    def rank(self,key):
        lo=0
        hi=len(self.arr)-1
        while(lo<=hi):
            #calculo el mid
            mid=lo+(hi-lo)//2
            if key<self.arr[mid].key: hi=mid-1
            elif key>self.arr[mid].key: lo=mid+1
            else: return mid
        return lo
    def select(self,idx):
        if(idx>0 and idx<len(self.arr)):
            return self.arr[idx].key
    def put(self,key,value):
        idx=self.rank(key)
        if(idx<len(self.arr) and self.arr[idx].key==key): 
            self.arr[idx].value=value
            return
        self.arr.insert(idx,node(key,value))
    def delete(self,key):
        idx=self.rank(key)
        if (idx<len(self.arr) and self.arr[idx].key==key):
            self.arr.pop(idx)
    def keys(self):
        keys=[]
        for obj in self.arr:
            keys.append(obj.key)
        return keys
    def print(self):
        chain=""
        for obj in self.arr:
            chain+=str(obj.key)+":"+str(obj.value)+";"
        return chain

def findMax(arr):
    keys=arr.keys()
    maxNode=node("",0)
    for key in keys:
        curV=arr.get(key)
        if(curV>maxNode.value):
            maxNode.key=key
            maxNode.value=curV
    return maxNode

prg=bsST()
print(prg.print(),prg.size(),prg.isEmpty())
file1=open("tinyTale.txt","r") # length 1
file1=open("Tale.txt","r") 
file1=open("leipzig1M.txt","r")
minLen=10
start_time=time.time()
lines=file1.readlines()
for line in lines:
    pq=re.findall(r"[\w']+", line)
    if(len(pq)>0):
        # print(pq)
        for word in pq:
            w=word.lower()
            if(len(w)>=minLen):
                if not prg.contains(w):
                    prg.put(w,1)
                else:
                    prg.put(w,prg.get(w)+1)
print("Ordered binary search --- %s seconds ---" % (time.time() - start_time))
tempN=findMax(prg)

print(prg.size())
print("Max:",tempN.key,":",tempN.value)

# tale.txt 0.42s 1828 Max: monseigneur : 104
# leipzig1M 45.9s
