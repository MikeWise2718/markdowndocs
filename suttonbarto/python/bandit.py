import numpy as np
import pandas as pd
import time

from random import seed,random
from enum import Enum
from numpy.random import normal

import seaborn as sns
import matplotlib.pyplot as plt

seed(1234)

ntotsteps = 0

class banditstep:
    epsilonGreed = 1
    ucb = 2


class bandit:

    def __init__(self,narms):
        self.narms = narms
        self.nstep = 0
        self.vhistory = []
        self.mu = []
        self.sg = []
        self.emu = []
        self.sumemu = []
        for i in range(narms):
            mui = random()*10
            self.mu.append(mui)
            self.sg.append(1.0)
            self.emu.append(0)
            self.sumemu.append(0)

    def argmaxemu(self):
        max = -1
        maxi = -1
        for i in range(self.narms):
            if self.emu[i]>max:
                max = self.emu[i]
                maxi = i
        return i

    def sample(self,q):
        v = self.mu[q] + normal(0,self.sg[q])
        return v

    def update(self,q,v):
        self.sumemu[q] += v
        self.emu[q] = self.sumemu[q]/self.nstep
        self.vhistory.append(v)
        return v

    def step(self,bstep,parm):
        global ntotsteps
        ntotsteps += 1
        self.nstep += 1
        if (bstep==banditstep.epsilonGreed):
            ran = random()
            if (ran<parm):
                q = int(random()*self.narms)
            else:
                q = self.argmaxemu()
            v = self.sample(q)
            self.update(q,v)
        else:
            print("{} not implemented".format(bstep))

    def getvhistory(self):
        npv = np.asarray(self.vhistory)
        return npv

class banditman:


    def __init__(self,nbandits,narms):
        self.nbandits = nbandits
        self.narms = narms
        self.bandit = []
        for i in range(nbandits):
            b = bandit(narms)
            self.bandit.append(b)

    def step(self,bstep,eps):
        for i in range(self.nbandits):
            self.bandit[i].step(bstep,eps)

    def run(self,nsteps,bstep,eps=0.1):
        for i in range(nsteps):
            bman.step(bstep,eps)

    def getvhistory(self):
        vsum = None
        for i in range(self.nbandits):
            if (i==0):
                vsum = self.bandit[i].getvhistory()
            else:
                v1 = self.bandit[i].getvhistory()
                vsum = vsum + v1
        vhist = vsum / self.nbandits
        return vhist



if __name__ == "__main__":
    bman = banditman(2000,10)
    start = time.time()
    bman.run(400,banditstep.epsilonGreed,0.1)
    elap = time.time()-start
    print("Total steps:{} took {:.3f} secs".format(ntotsteps,elap))
    vhist = bman.getvhistory()
    nrow = vhist.shape[0]
    print("vhist has {} rows".format(nrow))
    steps = range(1,nrow)

    # df = pd.DataFrame(data = vhist,index = idx,columns="vhist")
    df = pd.DataFrame(data = zip(steps,vhist),columns=["step","vhist"])
    print(df)

    sns.lineplot(x="step",y="vhist",data=df )
    plt.show()