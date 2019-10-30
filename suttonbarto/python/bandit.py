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

class BanditStep:
    epsilonGreed = 1
    ucb = 2


class Bandit:

    def __init__(self,narms):
        self.narms = narms
        self.nstep = 0
        self.rhistory = []
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

    def ArgMaxEmu(self):
        max = -1
        maxi = -1
        for i in range(self.narms):
            if self.emu[i]>max:
                max = self.emu[i]
                maxi = i
        return i

    def Sample(self,a):
        r = self.mu[a] + normal(0,self.sg[a])
        return r

    def UpdateHistory(self,a,r):
        self.sumemu[a] += r
        self.emu[a] = self.sumemu[a]/self.nstep
        self.rhistory.append(r)
        return 

    def Step(self,bstep,parm):
        global ntotsteps
        ntotsteps += 1
        self.nstep += 1
        if (bstep==BanditStep.epsilonGreed):
            ran = random()
            if (ran<parm):
                a = int(random()*self.narms)
            else:
                a = self.ArgMaxEmu()
            r = self.Sample(a)
            self.UpdateHistory(a,r)
        else:
            print("{} not implemented".format(bstep))

    def GetRhistory(self):
        npv = np.asarray(self.rhistory)
        return npv

    def AddViolinPlotPoints(self,arms,rews,npts):
        for a in range(self.narms):
            for i in range(npts):
                r = self.Sample(a)
                arms.append(a)
                rews.append(r)
        return

    def ViolinPlot(self):
        arms = []
        rews = []
        self.AddViolinPlotPoints(arms,rews,100)
        df = pd.DataFrame(data = zip(arms,rews),columns=["action","reward"]) 
        print(df)
        sns.violinplot(x="action",y="reward",data=df )       
        plt.show()


class BanditMan:

    def __init__(self,nbandits,narms):
        self.nbandits = nbandits
        self.narms = narms
        self.bandit = []
        for i in range(nbandits):
            b = Bandit(narms)
            self.bandit.append(b)
      #      if i==0:
      #          b.violinplot()

    def Step(self,bstep,eps):
        for iid in range(self.nbandits):
            self.bandit[iid].Step(bstep,eps)

    def ViolinPlot(self):
        ids = []
        arms = []
        rews = []
        nsamples_per_arm = 100
        for iid in range(self.nbandits):
            b = self.bandit[iid]
            b.AddViolinPlotPoints(arms,rews,nsamples_per_arm)
            ilst = [iid for i in range(nsamples_per_arm*self.narms)]
            ids.extend(ilst)

        df = pd.DataFrame(data = zip(ids,arms,rews),columns=["ids","action","reward"]) 
        print(df)
        fg = sns.FacetGrid(df, col="ids",col_wrap=5)
        fg.map(sns.violinplot, "action","reward")
        plt.show()


    def Run(self,nsteps,bstep,eps=0.1):
        for i in range(nsteps):
            bman.Step(bstep,eps)

    def GetRhistory(self):
        vsum = None
        for i in range(self.nbandits):
            if (i==0):
                vsum = self.bandit[i].GetRhistory()
            else:
                v1 = self.bandit[i].GetRhistory()
                vsum = vsum + v1
        vhist = vsum / self.nbandits
        return vhist

if __name__ == "__main__":
    nbandits = 20
    narms = 10
    bman = BanditMan(nbandits,narms)
    bman.ViolinPlot()
    start = time.time()
    bman.Run(400,BanditStep.epsilonGreed,0.1)
    elap = time.time()-start
    print("Total steps:{} took {:.3f} secs".format(ntotsteps,elap))
    vhist = bman.GetRhistory()
    nrow = vhist.shape[0]
    print("vhist has {} rows".format(nrow))
    steps = range(1,nrow)

    # df = pd.DataFrame(data = vhist,index = idx,columns="vhist")
    df = pd.DataFrame(data = zip(steps,vhist),columns=["step","vhist"])
    print(df)

    sns.lineplot(x="step",y="vhist",data=df )
    plt.show()