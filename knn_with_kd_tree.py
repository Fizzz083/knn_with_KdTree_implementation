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
        self.points.sort()
    def size(self):
        return len(self.points)
    def pop(self):
        self.points.remove( len(self.points )-1 )
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
    
    
 
    new = node(point.x,point.y, point.c)
    if(root.head == None):
        root.head = new
        print(str(root.head.x) + " -- " + str(root.head.y))
        return 
    d = (depth)%2
    print(str(root.head.x) + " -- " + str(root.head.y) + " "+ str(point.x)+" " + str(point.y) + " "+ str(k))
    
    
    
    #x check
    if(d==0):
        if(root.head.x < point.x): #left e jabo
        
            if(root.left == None):
                root.left = kdtree()
                print("left")
                root.left.head = new
                return 
            root.cnt_left = root.cnt_left+1
            build(root.left, point, depth+1)
            return 
        
        else:
            if(root.right == None):
                root.right  = kdtree()
                root.right.head = new
                print("right")
                return
               
            root.cnt_right = root.cnt_right +1
            build(root.right, point, depth+1)
            return 
           
        
    else: #y check
        if(root.head.y < point.y): #right e jabo
            if(root.left == None):
                root.left = kdtree()
                root.left.head = new
                print("left")
                return
            
            root.cnt_left = root.cnt_left+1
            build(root.left, point, depth+1)
            return 
            
            
        else:
            if(root.right == None):
                root.right  = kdtree()
                root.right.head = new
                print("right")
                return
            root.cnt_right = root.cnt_right +1
            build(root.right, point, depth+1)
            return 
           
    
    
    
    
    
    
pq  = priorityQ()

#bestDist =  int(1e12)


def search_n(root, point, depth):
    
    if(root == None or root.head == None):
        return 
    
    #global bestDist
    global pq
    global k
    print(str(root.head.x) + " -- " + str(root.head.y) + " "+ str(point.x)+" " + str(point.y) + " "+ str(k))
    distance = dist(point, root.head)
    
    f = 0
    if(pq.size()>0):
        if(dist(pq.last()[1], point) >  distance):
            root.head.dist = distance
            pq.push(root.head, distance)
            f=1
            #bestDist = dist(pq.last(), point)
    if(pq.size()<k and f == 0):
        root.head.dist = distance
        pq.push(root.head, distance)
        #bestDist = min(bestDist, dist(root.head, point))
    
    if(pq.size()>k):
        pq.pop()
        
    d = (depth)%2;
    
    right_dist = int(1e12)
    left_dist = int(1e12)
    
    if(root.right != None):
        right_dist = dist(root.right.head,point)
    if(root.left != None):
        left_dist = dist(root.left.head, point)
    
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



n = int(input())
k = int(input())

p_points = []

kdTree = kdtree()

for i in range(n):
    x, y, c = map(int, input().split())
    q = nn()
    q.x = x
    q.y = y 
    q.c = c
    p_points.append(q)
    build(kdTree, q, 0)
    print("appended..")



#for i in p_points:
#    build(kdTree, i, 0)

print("build done")

x, y = map(int, input().split())


p = nn()
p.x = x 
p.y = y


search_n(kdTree, p, 0)

print(pq.size())
for i in pq.points:
    print(str(i[1].x)+ " " + str(i[1].y) +" "+str(i[1].c)) 



#for i in pq.points:



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
                                          

"""