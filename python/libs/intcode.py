from collections import deque
from collections.abc import Iterable
from copy import deepcopy

class NeedsInput(Exception):
    pass

CLEAR_OUTPUT = 1
CLEAR_INPUT = 2
HALT_ON_LACKING_FEED = 3

class IntCodeMachine:

    def __init__(self, script = "99", mem_length=1000):
        """
        IntCodeMachine or IMC.
        """

        # Basic attributes
        self.script = list(map(int,script.split(",")))
        self.script += [0]*(mem_length-len(self.script))
        self.pc  = 0
        self.base = 0

        # Input and output
        self.feed = deque()
        self.out = deque()

        # Flags
        self.empty=False

        # Switches
        self.inst = {
            1:self.inst_add,
            2:self.inst_mul,
            3:self.inst_feed,
            4:self.inst_out,
            5:self.inst_jit,
            6:self.inst_jif,
            7:self.inst_lt,
            8:self.inst_eq,
            9:self.inst_ptr,
            99:self.leave
        }
        self.ptr_mode = [
            lambda n : self.script[n],
            lambda n : n,
            lambda n : self.base+self.script[n]
        ]

        # A copy of the script
        self.__copy_script = deepcopy(self.script)
    
    def __process_pointer(self, k):
        if isinstance(k, tuple):
            pc, md = k
        else:
            pc = k
            md = 1

        return self.ptr_mode[md](pc)

    def __getitem__(self, k):
        ptr = self.__process_pointer(k)
        return self.script[ptr]

    def __setitem__(self, k, v):
        ptr = self.__process_pointer(k)
        self.script[ptr] = v

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)
    
    def __lshift__(self, o):
        if isinstance(o, deque):
            while o:
                self.append(o.popleft())
        elif isinstance(o, Iterable):
            for e in o:
                self.append(e)
        elif isinstance(o, IntCodeMachine):
            while o.out:
                self.append(o.pop())
        else:
            self.append(o)

    def __bool__(self):
        return self.done()

    def __call__(self, *args):
        self.run(*args)
        return self

    def __str__(self):
        feed = "["
        for _ in range(len(self.feed)):
            x = self.feed.pop()
            feed += " " + str(x)
            self.feed.appendleft(x)
        feed += " ]"

        out = "["
        for _ in range(len(self.out)):
            x = self.out.popleft()
            out += " " + str(x)
            self.out.append(x)
        out += " ]"
        
        return f"IntCode Machine at <{hex(id(self))}> \n{out} <<[OUT]<< ICM <<[IN]<< {feed}"

    def copy(self):
        res = IntCodeMachine()
        res.__copy_script = deepcopy(self.__copy_script)
        res.script = deepcopy(self.script)
        res.pc = self.pc
        res.base = self.base
        res.feed = deepcopy(self.feed)
        res.out = deepcopy(self.out)
        return res

    def reset(self, *flags):
        self.pc = 0
        self.base = 0
        self.script.clear()
        self.script = deepcopy(self.__copy_script)
        if CLEAR_INPUT in flags:
            self.feed.clear()
        if CLEAR_OUTPUT in flags:
            self.out.clear()
    
    # Flags
    def needs_input(self):
        return self.empty
    
    def done(self):
        return self.pc == -1
    
    # Operations
    def pop(self):
        return self.out.popleft()

    def append(self, v):
        self.empty = False
        self.feed.append(v)

    def feedclear():
        self.feed.clear()
    
    def outclear():
        self.out.clear()

    # IntCode's core
    def run(self, *flags, halt_on=-1):
        if self: 
            return []

        if CLEAR_INPUT in flags:
            self.feed.clear()
        if CLEAR_OUTPUT in flags:
            self.out.clear()

        m3,m2,m1,op = 0,0,0,0

        while 0 <= self.pc < len(self.script) and not self:
            cmd = f"{self[self.pc]:>05}"
            m3,m2,m1 = map(int, cmd[:3])
            op = int(cmd[3:])

            if self.inst[op](self.pc, m1, m2, m3):
                if halt_on > 0:
                    halt_on -= 1
                if halt_on == 0:
                    break

                if op == 3:
                    if HALT_ON_LACKING_FEED in flags:
                        break
                    else:
                        raise NeedsInput()
                
        return self.out
    
    """
    Instructions
    """

    def inst_add(self, ptr, m1, m2, m3):
        self[ptr+3,m3] = self[ptr+2,m2] + self[ptr+1,m1]
        self.pc += 4

    def inst_mul(self, ptr, m1, m2, m3):
        self[ptr+3,m3] = self[ptr+2,m2] * self[ptr+1,m1]
        self.pc += 4
    
    def inst_feed(self, ptr, m1, *_):
        if len(self.feed) == 0:
            self.empty=True
            return True
        res = self.feed.popleft()
        self[ptr+1,m1] = res
        self.pc += 2
    
    def inst_out(self, ptr, m1, *_):
        self.out.append(self[ptr+1,m1])
        self.pc += 2
        return True

    def inst_jit(self, ptr, m1, m2, _):
        self.pc = self.pc+3 if not self[ptr+1, m1] else self[ptr+2,m2]

    def inst_jif(self, ptr, m1, m2, _):
        self.pc = self.pc+3 if self[ptr+1, m1] else self[ptr+2,m2]

    def inst_lt(self, ptr, m1, m2, m3):
        self[ptr+3,m3] = int(self[ptr+1,m1] < self[ptr+2,m2])
        self.pc += 4

    def inst_eq(self, ptr, m1, m2, m3):
        self[ptr+3,m3] = int(self[ptr+1,m1] == self[ptr+2,m2])
        self.pc += 4
    
    def inst_ptr(self, ptr, m1, *_):
        self.base += self[ptr+1,m1]
        self.pc += 2

    def leave(self, *_):
        self.pc = -1