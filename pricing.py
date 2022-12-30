from bsm import BSM

class Pricing(BSM):

    def deltaFull(self, fPrice, params, exp):
        n = len(params)
        deltaFull = 0
        for i in range(n):
            param = params[i]
            if exp:
                param['exp'] = exp
            deltaSingle = self.delta(fPrice, param['strike'], param['vola'], param['exp'], param['dType']) * param['quant']
            deltaFull = deltaFull + deltaSingle
        return deltaFull

    def vegaFull(self, fPrice, params, exp):
        n = len(params)
        vegaFull = 0
        for i in range(n):
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] != 'F':
                vegaSingle = self.vega(fPrice, param['strike'], param['vola'], param['exp']) * param['quant']
                vegaFull = vegaFull + vegaSingle
        return vegaFull

    def thetaFull(self, fPrice, params, exp):
        n = len(params)
        thetaFull = 0
        for i in range(n):
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] != 'F':
                thetaSingle = self.theta(fPrice, param['strike'], param['vola'], param['exp']) * param['quant']
                thetaFull = thetaFull + thetaSingle
        return thetaFull
        
    def gammaFull(self, fPrice, params, exp):
        n = len(params)
        gammaFull = 0
        for i in range(n):
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] != 'F':
                gammaSingle = self.gamma(fPrice, param['strike'], param['vola'], param['exp']) * param['quant']
                gammaFull = gammaFull + gammaSingle
        return gammaFull

    def p_l(self, fPrice, params, exp):
        n = len(params)
        plF = 0
        for i in range(n):
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] == 'F':
                plS = (fPrice - param['price']) * param['quant']
            else:
                theo = round(self.theo(fPrice, param['strike'], param['vola'], param['exp'], param['dType']), 3)
                plS = (theo - param['price']) * param['quant']
            plF = plF + plS
        return plF