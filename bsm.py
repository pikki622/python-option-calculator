import math

class BSM():

    def pdf(self, x):
        return math.exp(-x**2/2) / math.sqrt(2*math.pi)

    def cdf(self, x):
        return (1 + math.erf(x / math.sqrt(2))) / 2

    def d1(self, S, K, V, T):
        return (math.log(S / float(K)) + (V**2 / 2) * T) / (V * math.sqrt(T))

    def d2(self, S, K, V, T):
        return self.d1(S, K, V, T) - (V * math.sqrt(T))

    def theo(self, S, K, V, T, dT):
        if dT == 'C':
            return S * self.cdf(self.d1(S, K, V, T)) - K * self.cdf(self.d2(S, K, V, T))
        else:
            return K * self.cdf(-self.d2(S, K, V, T)) - S * self.cdf(-self.d1(S, K, V, T))

    def delta(self, S, K, V, T, dT):
        if dT == 'C':
            return self.cdf(self.d1(S, K, V, T))
        elif dT == 'P':
            return self.cdf(self.d1(S, K, V, T)) - 1
        else:
            return 1

    def vega(self, S, K, V, T):
        return (S * math.sqrt(T) * self.pdf(self.d1(S, K, V, T))) / 100

    def theta(self, S, K, V, T):
        return -((S * V * self.pdf(self.d1(S, K, V, T))) / (2 * math.sqrt(T))) / 365

    def gamma(self, S, K, V, T):
        return self.pdf(self.d1(S, K, V, T))/(S * V * math.sqrt(T))