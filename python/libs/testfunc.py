from collections.abc import Iterable
import time

def timeit(func, *args, print_res=True, **kwargs):
    print(f"[[Python]] Executing function '{func.__name__}' ... ")
    t = time.time()
    try:
        data=func(*args, **kwargs)
        t = time.time()-t
        print("Done!!")
    except KeyboardInterrupt:
        data = None
        t = time.time()-t
        print("Function was intterupted.")
    print(f"Time elapsed for {func.__name__}:", f"{int(t)%60:02}s {int(t*1000)%1000:03}ms {int(t*10**6)%1000:03}Ms {int(t*10**9)%1000:03}ns")
    if data and print_res: print("Result:", data)
    print()
    return data