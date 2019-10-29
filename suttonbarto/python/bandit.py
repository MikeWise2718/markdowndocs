from random import seed,random
from enum import Enum
from numpy.random import normal

seed(1234)

class banditstep:
    epsilonGreed = 1
    ucb = 2


class bandit:

    nstep = 0
    narms = None
    mu = []
    sg = []

    sumemu = []
    emu = []

    def __init__(self,narms):
        self.narms = narms
        self.nstep = 0
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

    def updateemu(self,q,v):
        self.sumemu[q] += v
        self.emu[q] = self.sumemu[q]/self.nstep
        return v

    def step(self,bstep,parm):
        self.nstep += 1
        if (bstep==banditstep.epsilonGreed):
            ran = random()
            if (ran<parm):
                q = int(random()*self.narms)
            else:
                q = self.argmaxemu()
            v = self.sample(q)
            self.updateemu(q,v)
        else:
            print("{} not implemented".format(bstep))


class banditman:

    nbandits = None
    narms = None
    bandit = []

    def __init__(self,nbandits,narms):
        self.nbandits = nbandits
        self.narms = narms
        for i in range(nbandits):
            b = bandit(narms)
            self.bandit.append(b)

    def step(self,bstep):
        for i in range(self.nbandits):
            self.bandit[i].step(bstep,0.01)



if __name__ == "__main__":
    bman = banditman(2,10)
    for i in range(10):
        bman.step(banditstep.epsilonGreed)
