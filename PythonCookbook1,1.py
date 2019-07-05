# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 23:00:05 2019

@author: HP
"""

# Dalam bagin ini belajar unpack sequence kedalam beberapa variabel

#problem 1

#programmer memiliki N-buah tuple / sequence (deret) yang perlu dipisah menjadi
#kombinasi beberapa variabel

#sequence = iterable
#%%
#contoh1
p = (4,5,6,7,8)
num1,num2,num3,num4,num5 = p
num2


#%%
#contoh2
data = ['wakwaw',50,9032.2,(20,20,1)]
name,num6,num7,kuldat = data
print(kuldat)
#%%
#contoh3
s = 'Wakwawkocak'
s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10 = s
print(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
#%%
#contoh4
data = ['wakwaw',50,9032.2,(20,20,1)]
_, shares, price, _ = data
print(shares)
#%%
#contoh5
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212', '123-456-789')
name,email,*numbers = record
print(numbers)
#%%
#contoh6
current, *trailing = [10,9,8,7,6,5,4,3,2,1]
print(trailing)
print(current)
#%%
#latihan1
wakwaw,*wakwaw1, wakwaw2 = [(20,21,22), (22,23,24), 22,23,23,24, (21,21,21)]
print(wakwaw1)
#fungsi star expression u/ masukin data secara terus menerus
#star expression = dipakai u/ extended iterable unpacking
#%% Discussion 2
records = [
    ('foo',1,2),
    ('bar','hello'),
    ('for',3,4),
   ]

def do_foo (x,y):
    print('foo',x,y)
    
def do_bar (s):
    print('bar',s)
    
for tag, *args in records :
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
#%%
record = ('Wakwaw', 50, 123.45, (12,18,2012))
name, *_, (*_,year) = record
print(year)

#%% praktek line split buat kumpulan string
line = 'wakwaw-lol-watafak'
name,fun,wat = line.split('-')
print (fun)
#%% recursive algorithm
items = [1,2,3,4,5,6,7,8,9]
def sum(items):
    head,*tails = items
    return head + sum(tails) if tails else head

print (sum(items))

#%% Section 1.3 Keeping the last N Items (Soal Susah)
from collections import deque

def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
#%% Deque (Double ended queue) menggunakan deque(maxlen=N) dapat membuat queue dengan ukuran fixed
from collections import deque
q = deque(maxlen=3) #ngasih queue maksimal tiga angka
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4) #jika melebihi kapasitas queue, angka paling kecil dieliminasi
print(q)

#%% masih deque
from collections import deque
q = deque() #membuat queue dengan tidak ada batas jumlah angka
q.append(1)
q.append(2)
q.append(3)
print (q)
q.appendleft(4) #menambah angka 4 ke posisi angka paling kiri
print(q)
q.pop()
print(q)
q.popleft()
print(q)
#%% FInding the Largest or smallest N items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
#%% kode alternatif cheap
def cheap (a):
    return a.price

#%%
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)

#%% contoh lain heap
nums = [1,8,2,23,7,-4,18,23,42,37,2]
import heapq
heapq.heapify(nums)
print(nums)


heap = list(nums)
print (nums[1])
print(heap)
heapq.heapify(heap)
print(heap)

#%% Soal menarik tentang priority queue
import heapq
class PriorityQueue():
    def __init__ (self):
        self._queue = []
        self._index = 0
        
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    
q = PriorityQueue()
q.push(Item('foo'),1)
Item
        
