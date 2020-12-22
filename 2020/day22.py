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
    prevA, prevB = set(), set()
    while A and B:

        tA = tuple(A)
        tB = tuple(B)
        if tA in prevA and tB in prevB:
            return True, sum(a*i for i,a in enumerate(reversed(A),1))
        else:
            prevA.add(tA)
            prevB.add(tB)
        
        a = A.popleft()
        b = B.popleft()

        winner = (a>b) if (len(A) < a or len(B) < b) else recursive_game(deque(islice(A,0,a)), deque(islice(B,0,b)))[0]

        if winner:
            A.append(a)
            A.append(b)
        else:
            B.append(b)
            B.append(a)
    
    return bool(A), sum(a*i for i,a in enumerate(reversed(A+B),1))

def two(raw):
    A,B = parse_data(raw)
    winner = recursive_game(deque(A), deque(B))[1]
    return winner