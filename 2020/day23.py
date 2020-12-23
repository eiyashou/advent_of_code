
def parse(raw):
    data=list(map(int,list(raw)))
    return data

class LinkedList:

    def __init__(self, l):

        self.indexes = {}
        self.start = Node(l[0])
        end = self.start
        self.indexes[l[0]] = self.start 

        for e in l[1:]:
            end.next = Node(e)
            end = end.next
            self.indexes[e] = end
        
        end.next = self.start
    
    def __getitem__(self, i):
        return self.indexes[i]

class Node:

    def __init__(self, e, _next=None):
        self.e = e
        self.next = _next
    
    def insert(self, n):
        n.next = self.next
        self.next = n

def crabbygame(data,T):
    L = LinkedList(data)
    H = max(data)+1
    PTR = L.start

    for t in range(T):
        
        # Step 1 : Extract three-cups off
        ptr_ori_end = PTR
        cups = [ptr_ori_end.e for _ in range(3) if (ptr_ori_end:=ptr_ori_end.next)]
        ptr_ori_start = PTR.next
        PTR.next = ptr_ori_end.next

        # Step 2 : Find destination cup
        dest = PTR.e
        while True:
            dest = (dest-1)%H
            if dest not in cups and dest != 0:
                break
        
        # Step 3 : Assemble back the cups
        ptr_dest_start = L[dest]
        ptr_dest_end = ptr_dest_start.next

        ptr_dest_start.next = ptr_ori_start
        ptr_ori_end.next = ptr_dest_end

        # Step 4 : next cup (DONE)
        PTR = PTR.next

    return L

def one(data):
    ptr = crabbygame(data,100)[1]
    res = ""
    while (ptr:=ptr.next).e != 1:
        res += str(ptr.e)
    return res

def two(data):
    data += list(range(10,10**6+1))

    L = crabbygame(data, 10**7)
    ptr = L[1].next
    return ptr.e * ptr.next.e