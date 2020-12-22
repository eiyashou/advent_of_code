from collections import deque
from itertools import islice

C = deque((-1,))

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

def recursive_game(A,B,i=False):
    prev = set()
    winner = None
    while A and B:

        if (t:=hash(tuple(A)+C+tuple(B))) in prev:
            winner = True
            break
        else:
            prev.add(t)
        
        a = A.popleft()
        b = B.popleft()

        winner = (a>b) if (len(A) < a or len(B) < b) else recursive_game(deque(islice(A,0,a)), deque(islice(B,0,b)),True)

        if winner: 
            A.extend((a,b))
        else: 
            B.extend((b,a))
    
    if not i: winner = sum(i*a for i,a in enumerate(reversed(A if winner else B),1))
    return winner

def two(raw):
    A,B = map(deque,parse_data(raw))
    return recursive_game(A, B)