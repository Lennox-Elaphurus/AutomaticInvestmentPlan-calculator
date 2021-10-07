import math
import scipy
import sympy


def mysqrt1(x):  #sqrt(x)+b, sympy.integrate(sympy.sqrt(x) + a, (x,i,i+1)
    global total
    global period
    b=(total - (2*period**(3/2))/3 )/period
    print("b=",b)
    return math.sqrt(x)+b

def mysqrt2(x): #a* sqrt(x)

def discreteIntegrate(f,down,up):
    global total
    global period
    a=(total - (2*period**(3/2))/3 )/period

    investementList=[]
    sum=0
    x=sympy.symbols('x')
    for i in range(int(down),int(up)):
        inv=float(sympy.integrate(sympy.sqrt(x) + a, (x,i,i+1)))
        sum+=inv
        investementList.append(inv)
    # print(investementList)
    return sum,investementList


global period
# period=int(input('请输入定投期数:\n '))
period=12

global total
# total=input('请输入定投总金额:\n')
total=72

print("定投期数:"+str(period),"定投总金额:"+str(total)+"万")

x=sympy.symbols('x')
a=sympy.symbols('a')
b=sympy.symbols('b')
p=sympy.symbols('p')
# print(sympy.integrate(sympy.sqrt(x) + a, (x,0,p)))

print(discreteIntegrate(mysqrt,0,period))



