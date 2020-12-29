def hyperconway(raw:set, G=100,N=2):    
    raw = set(raw)
    if N < 2 or G < 1: raise ValueError()
    
    adj_coords = list(filter(any, itertools.product((-1, 0, 1), repeat=N)))
    print(f"Gen 0, count={len(raw)}")

    for g in range(1,G+1):
        neighbours = Counter(tuple(v+dv for v,dv in zip(V,dV)) for dV in adj_coords for V in raw)
        raw={p for p in neighbours if neighbours[p]==3 or (p in raw and neighbours[p]==2)}
        print(f"Gen {g}, count={len(raw)}")

    return len(raw)