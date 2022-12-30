from pricing import Pricing
import matplotlib.pyplot as plt

god = 365

class Plot(Pricing):
    def plotPL(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        P_L = [self.p_l(s, params, exp) for s in bePrice]
        plt.plot(bePrice, P_L, label=int(exp*god))
        
    def plotDelta(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        D = [self.deltaFull(s, params, exp) for s in bePrice]
        plt.plot(bePrice, D, label=int(exp*god))
        
    def plotTheta(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        T = [self.thetaFull(s, params, exp) for s in bePrice]
        plt.plot(bePrice, T, label=int(exp*god))
        
    def plotVega(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        V = [self.vegaFull(s, params, exp) for s in bePrice]
        plt.plot(bePrice, V, label=int(exp*god))
        
    def plotGamma(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        V = [self.gammaFull(s, params, exp) for s in bePrice]
        plt.plot(bePrice, V, label=int(exp*god))