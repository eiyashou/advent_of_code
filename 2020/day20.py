import sys, os, re, math, hashlib, itertools, functools, string
from collections import namedtuple, defaultdict, Counter
import numpy as np
from scipy.signal import convolve2d


MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
MONSTER_COUNT = "".join(MONSTER).count("#")
MONSTER = np.matrix([[int(_=="#") for _ in __] for __ in MONSTER])
edge2bin = lambda n : sum(2**i for i,bit in enumerate(n) if bit)


get_edge = [
    lambda IMG : IMG[0,:].tolist()[0],
    lambda IMG : IMG[:,0].transpose().tolist()[0],
    lambda IMG : IMG[-1,:].tolist()[0],
    lambda IMG : IMG[:,-1].transpose().tolist()[0]
]


def parse_data(raw):

    res = dict()
    for lines in raw.split("\n\n"):
        if lines == "":
            continue
        
        img = lines.splitlines()

        ID  = int(re.search(r"(\d+)",img[0]).group(0))
        IMG = np.matrix([list(int(_=="#") for _ in __) for __ in img[1:]])

        res[ID] = IMG

    return res


def to_edges(imgs):

    edges_d = dict()

    test = []

    for ID,IMG in imgs.items():
        edges_d[ID] = list(map(lambda n : min(edge2bin(n),edge2bin(reversed(n))), [x(IMG) for x in get_edge]))

    return edges_d, [v for edges in edges_d.values() for v in edges]


def match_imgs(src,match,ori_src):

    bin2match = edge2bin(get_edge[ori_src](src))
    ori_match = (ori_src+2)%4
    
    m = np.matrix(match)

    for _ in range(2):
        for _ in range(4):
            if bin2match == edge2bin(get_edge[ori_match](m)):
                return m
            m = np.rot90(m, k=1,axes=(0,1))
        m = np.flip(m,axis=0)


def mount_img(raw):
    imgs = parse_data(raw)
    edges_d, edges = to_edges(imgs)

    for ID,EDGES in edges_d.items():
        if all(edges.count(edge)==1 for edge in EDGES[:2]):
            break
    
    first_row = [imgs[ID]]
    del imgs[ID]

    while True:
        for k,img in imgs.items():
            if type(m:=match_imgs(first_row[-1],img,-1)) == np.matrix:
                first_row.append(m)
                del imgs[k]
                break
        else:
            break

    L = len(first_row)
    rows = [first_row]

    while len(imgs) > 0:
        new_row = [None for _ in range(L)]
        del_keys = set()
        for i,ref_img in enumerate(rows[-1]):
            for k,match in imgs.items():
                if type(m:=match_imgs(ref_img,match,-2)) == np.matrix:
                    new_row[i] = m
                    del_keys.add(k)
                    break
        rows.append(new_row)
        
        for k in del_keys:
            del imgs[k]

    return np.concatenate([np.concatenate([x[1:-1,1:-1] for x in row],axis=1) for row in rows],axis=0)

def one(raw):
    imgs = parse_data(raw)    
    
    edges_d, edges = to_edges(imgs)

    res = list()
    edges_aligned = []
    for ID,EDGES in edges_d.items():

        if sum(edges.count(edge)==1 for edge in EDGES) == 2:
            res.append(ID)
    
    return math.prod(res)

def two(raw):
    img = mount_img(raw)
    
    for __ in range(2):
        for _ in range(4):
            if (p:=sum(x==MONSTER_COUNT for x in convolve2d(img, MONSTER).flatten().tolist())):
                return np.sum(img)-MONSTER_COUNT*p
            img = np.rot90(img,k=1,axes=(0,1))
        img = np.flip(img,0)