import math
import matplotlib.pyplot as plt
import sympy
import time
import numpy as np


def mysqrt1(x):  #sqrt(x)+b, sympy.integrate(sympy.sqrt(x) + a, (x,i,i+1)
    global total
    global period
    b=(total - (2*period**(3/2))/3 )/period
    print("b=",b)
    return math.sqrt(x)+b

def quadraticF(x):
    return -x*(x-2)

def sampling(alpha,period):
    sampleList=[]
    sum=0
    for i in range(1,period+1):
        tmpV=(i/period)**alpha
        sampleList.append(tmpV)
        sum+=tmpV
    return sampleList,sum


def saveToCSV(investmentList,period,total):
    localtime=time.strftime("-日期%Y%m%d-时间%H%M", time.localtime())
    try:
        csvF=open("投资计划-期数"+str(period)+"-总额"+str(total)+localtime+".csv","w")
    except:
        print("创建文件出错，若已打开表格，请关闭表格后重新运行本程序。")
        input("按回车键关闭程序...")
        exit(-1)
    csvF.write("期数,当期投资金额\n")
    for i in range(period):
        csvF.write(str(i+1)+","+str(investmentList[i])+"\n")
    csvF.write("\n投资总期数,计划投资总额\n"+str(period)+","+str(total)+"\n")
    csvF.close()

    csvF=open("投资计划-期数"+str(period)+"-总额"+str(total)+localtime+".csv","r")
    csvTable=csvF.read()
    csvF.close()
    print("\n计划如下：\n"+csvTable.replace(",", "\t"))
    print("以上表格已保存为csv文件，可以用Excel打开")
    print("期数-定投金额 散点图已保存在当前目录")


def mylog(x):
    return math.log10(x+1)


def main(alpha,period,total):
    standardList,sum=sampling(alpha,period)
    investmentList = [v * (total/sum) for v in standardList]
    # print(investmentList)

    # draw and save
    plt.figure()
    plt.scatter(range(1,period+1),investmentList,color='r')
    plt.xlabel("Period")
    plt.ylabel("Amount")
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    plt.title("Period="+str(period)+" Total="+str(total)+" f(x)=x^"+str(alpha))

    xList=np.arange(0,1,0.01)
    yList=[x**alpha * (total/sum) for x in xList]
    xList=[x * period for x in xList]
    plt.plot(xList,yList,label="x^"+str(alpha),linestyle="--",color='g')

    xList=np.arange(0,1,0.01)
    yList=[x**2 * (total/sum) for x in xList]
    xList=[x * period for x in xList]
    plt.plot(xList,yList,label="x^2",linestyle="--",color='y')

    xList=np.arange(0,1,0.01)
    yList=[math.sqrt(x) * (total/sum) for x in xList]
    xList=[x * period for x in xList]
    plt.plot(xList,yList,label="x^0.5",linestyle="--",color='b')

    xList=np.arange(0,1,0.01)
    yList=[ total/period for x in xList]
    xList=[x * period for x in xList]
    plt.plot(xList,yList,label="const",linestyle="--",color='black')

    xList=np.arange(0,1,0.01)
    yList=[ x * (total/sum) for x in xList]
    xList=[x * period for x in xList]
    plt.plot(xList,yList,label="x",linestyle="--",color='grey')

    plt.legend()
    try:
        plt.savefig("Period="+str(period)+"Total="+str(total)+".png")
    except:
        print("创建图片出错，请关闭已打开的图片后重新运行本程序")
        input("按回车键关闭程序...")
        exit(-1)
    # plt.show()
    # end draw and save

    sum2=0
    for v in investmentList:
        sum2+=v
    # print("实际投资总额:"+str(sum2))

    saveToCSV(investmentList,period,total)


period=int(input('请输入定投期数:\n '))
total=float(input('请输入定投总金额:\n'))
alpha=float(input('请输入函数指数: (例如，sqrt(x)输入0.5,x^2输入2)\n'))

main(alpha,period,total)

input("按回车键关闭程序...")



