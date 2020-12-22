from collections import deque
from itertools import islice

def parse_data(raw):
    data = [list(map(int,lines.split("\n")[1:])) for lines in raw.split("\n\n")]
    return data

def one(raw):
    A,B = parse_data(raw)

    while A and B:
                
        if A[0] > B[0]:
            A.append(A.pop(0))
            A.append(B.pop(0))
        else:
            B.append(B.pop(0))
            B.append(A.pop(0))

    winner = A if A else B
    return sum(a*i for i,a in enumerate(reversed(winner),1))

def recursive_game(A,B):
    prevA, prevB = set(),set()
    while A and B:

        tA = tuple(A)
        tB = tuple(B)
        if tA in prevA and tB in prevB:
            return True, 0
        else:
            prevA.add(tA)
            prevB.add(tB)
        
        a = A.popleft()
        b = B.popleft()

        winner = (a>b) if len(A) < a or len(B) < b else recursive_game(deque(islice(A,0,a)), deque(islice(B,0,b)))

        if winner:
            A.append(a)
            A.append(b)
        else:
            B.append(b)
            B.append(a)
    
    return bool(A)

def two(raw):
    Aori,Bori = parse_data(raw)
    winner = recursive_game(deque(Aori), deque(Bori))
    return sum(a*i for i,a in enumerate(reversed(A if winner else B),1))