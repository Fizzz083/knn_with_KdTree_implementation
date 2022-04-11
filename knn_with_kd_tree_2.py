# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 02:04:56 2022

@author: USER
"""



class nn:
    def __init__(self):
        self.x  = 0
        self.y = 0
        self.c = 0
        
class priorityQ:
    def __init__(self):
        self.points = []
    def push(self, p , dist):
        self.points.append((dist, p))
        self.points.sort(key=lambda pair: pair[0])
        #sorted(self.points, key = lambda k: [k[0], k[1].x])
        
        #self.points.sort(cmp=lambda a, b: 0 if a[0] == b[0] else
        #                       +1 if a[0] > b[0] else
        #                       -1 if a[0] < b[0] else 0)
    def size(self):
        return len(self.points)
    def pop(self):
        if(self.size()>0):
            del self.points[-1]
        #self.points.remove( len(self.points )-1 )
    def last(self):
        return self.points[-1]



def dist(p, q):
    return (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y)
    

class node:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.dist = 0
        
        

class kdtree:
    def __init__(self):
        self.head = None
        self.left = None 
        self.right = None
        self.cnt_left = 0
        self.cnt_right = 0
    

k=10

def build(root, point, depth):
    #print(str(root is None) + " ")
    new = node(point.x,point.y, point.c)
    if( root is None):
        root  = kdtree()
        root.head = new
        print(" "+str(root.head.x) + " -- " + str(root.head.y))
        return root
    d = (depth)%2
    print(str(root.head.x) + " -- " + str(root.head.y) + " "+ str(point.x)+" " + str(point.y) + " "+ str(k))
    
    
    
    #x check
    if(d==0):
        if(root.head.x < point.x): #left e jabo
            
            root.cnt_left = root.cnt_left+1
            root.left = build(root.left, point, depth+1)
        else:
            root.cnt_right = root.cnt_right +1
            root.right = build(root.right, point, depth+1)
             
    else: #y check
        if(root.head.y < point.y): #left e jabo
        
            root.cnt_left = root.cnt_left+1
            root.left = build(root.left, point, depth+1) 
        else:
            
            root.cnt_right = root.cnt_right +1
            root.right  = build(root.right, point, depth+1)

    return root
           
    
    
    
    
    
    
pq  = priorityQ()

#bestDist =  int(1e20)


def search_n(root, point, depth):
    
    if( root is None ):
        return 
    
    #global bestDist
    global pq
    global k
    #print(str(root.head.x) + " -- " + str(root.head.y) + " "+ str(point.x)+" " + str(point.y) + " "+ str(k))
    distance = dist(point, root.head)
    
    f = 0
    
        
    d = (depth)%2
    
    right_dist = int(1e20)
    left_dist = int(1e20)
    last_dist = int(1e20)


    if(pq.size()>0):
        last_dist = pq.last()[0]
    if(root.right is not None):
        right_dist = dist(root.right.head,point)
    if(root.left is not None):
        left_dist = dist(root.left.head, point)

    if(d==0):
        if(root.head.x < point.x): #left e jabo
            search_n(root.left, point, depth+1)
            
            #or (((root.head.x-point.x) * (root.head.x - point.x) ) < dist(pq.last()[1], point)
            
            if(pq.size() < k or right_dist < left_dist or right_dist < last_dist):
                search_n(root.right, point, depth+1)
        
        else:
            search_n(root.right, point, depth+1)   
            if(pq.size() < k or left_dist < right_dist or left_dist < last_dist):
                search_n(root.left, point, depth+1)
    else:
        if(root.head.y < point.y): 
            search_n(root.left, point, depth+1)
            if(pq.size() < k or right_dist < left_dist or right_dist < last_dist ):
                search_n(root.right, point, depth+1)
        
        else:
            search_n(root.right, point, depth+1)
                         
            if(pq.size() < k or left_dist < right_dist or left_dist < right_dist):
                search_n(root.left, point, depth+1)
    
    if(pq.size()>0):
        if(pq.last()[0] >  distance):
            #root.head.dist = distance
            pq.push(root.head, distance)
            f=1
            #bestDist = dist(pq.last(), point)
    if(pq.size()<k and f == 0):
        #root.head.dist = distance
        pq.push(root.head, distance)
        #bestDist = min(bestDist, dist(root.head, point))
    
    while(pq.size()>k):
        pq.pop()

    return 


    near = None
    far = None
    if(right_dist < left_dist): #rght nearer
        search_n(root.right,point, depth+1)
        if(pq.size()<k or  last_dist < left_dist):
            search_n(root.left, point, depth+1)
    else:
        search_n(root.left,point, depth+1)
        if(pq.size()<k or  last_dist < right_dist):
            search_n(root.right, point, depth+1)



    


n = int(input())
k = int(input())

p_points = []

kdTree = None

for i in range(n):
    x, y, c = map(int, input().split())
    q = nn()
    q.x = x
    q.y = y 
    q.c = c
    p_points.append(q)

    kdTree = build(kdTree, q, 0)
    print("appended..")
    #print(str(kdTree is None) +" hh " + str(kdTree.head is None))



#for i in p_points:
#    build(kdTree, i, 0)

print("build done")

x, y = map(int, input().split())


p = nn()
p.x = x 
p.y = y


search_n(kdTree, p, 0)

ans = []
cnt = [0]*(k+1)
print(" ------------------- \n")
print(pq.size())
for i in pq.points:
    cnt[i[1].c] = cnt[i[1].c]+1
    ans.append((i[1].x, i[1].y))
    print(str(i[0])+" "+str(i[1].x) + " " + str(i[1].y))
    #print(str(i[1].x)+ " " + str(i[1].y) +" "+str(i[1].c)) 
print(" ------------------- ")
#ans.sort()

for i in ans:
    q.x= i[0]
    q.y = i[1]
    print(str(i[0])+ " " + str(i[1]) + " "+ str(dist(p,q)))

#for i in pq.points:
for i in ans:
    q.x= i[0]
    q.y = i[1]
    print( str(dist(p,q)))

arr = []
for i in range(0,k+1):
    if( cnt[i]!= 0 ):
        arr.append((cnt[i], i))

arr.sort()
print("best class: "+ str(arr[-1][1])  + " cnt: " + str(arr[-1][0]))



"""
class_di = 10
class_cnt = [0]*class_di

near = []

def search(root, point, depth, remaining_k):
    
    sub_count  = root.cnt_left+ root.cnt_right +1
    
    inner = 0
    if(sub_count <= remaining_k):
        inner = 1
        near.append(root.head)
        search(root.left, point, depth, remaining_k-1)
        search(root.right, point, depth, remaining_k-1)
        return 
    
    d = (depth+1)%2
    
    #x check
    if(d==0):
        if(root.head.x < point[0]): #left e jabo
        
            if(root.left == None):
                return 
            
            search(root.left, point, depth, remaining_k)
            return 
        
        else:
            if(root.right == None):
                return
               
            search(root.right, point, depth, remaining_k)
            return 
           
        
    else: #y check
        if(root.head.y < point[1]): #right e jabo
            if(root.left == None):
                return
      
            search(root.left, point, depth, remaining_k)
            return 
           
            
            
        else:
            if(root.right == None):
               
                return
            
            search(root.right, point, depth, remaining_k)
            return 










 if(d==0):
        if(root.head.x < point.x): #left e jabo
            search_n(root.left, point, depth+1)
            
            #or (((root.head.x-point.x) * (root.head.x - point.x) ) < dist(pq.last()[1], point)
            
            if(pq.size() < k or right_dist <= left_dist ):
                search_n(root.right, point, depth+1)
        
        else:
            search_n(root.right, point, depth+1)   
            if(pq.size() < k or left_dist <= right_dist):
                search_n(root.left, point, depth+1)
    else:
        if(root.head.y < point.y): 
            search_n(root.left, point, depth+1)
            if(pq.size() < k or right_dist <= left_dist ):
                search_n(root.right, point, depth+1)
        
        else:
            search_n(root.right, point, depth+1)
                         
            if(pq.size() < k or left_dist <= right_dist):
                search_n(root.left, point, depth+1)
"""