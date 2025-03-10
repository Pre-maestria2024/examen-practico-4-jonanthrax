from queue import PriorityQueue
from queue import Queue

def main():

    n, k = map(int, input().split())
    edges = []
    for i in range(n-1):
        u,v = map(int,input().split())
        edges.append((u,v),)
        pass
    
    print("n:{} | k: {}".format(n,k))
    print("edges: ", edges)
    pass

if __name__  == '__main__':
    main()
    pass
