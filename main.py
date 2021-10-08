import math
import matplotlib.pyplot as plt
import sympy
import time


def mysqrt1(x):  #sqrt(x)+b, sympy.integrate(sympy.sqrt(x) + a, (x,i,i+1)
    global total
    global period
    b=(total - (2*period**(3/2))/3 )/period
    print("b=",b)
    return math.sqrt(x)+b

def quadraticF(x):
    return -x*(x-2)

def sampling(f,period):
    sampleList=[]
    sum=0
    for i in range(1,period+1):
        tmpV=f(i/period)
        sampleList.append(tmpV)
        sum+=tmpV
    return sampleList,sum

def drawAndSave(List,period,total):
    plt.figure()
    plt.scatter(range(1,period+1),List,)
    plt.xlabel("Period")
    plt.ylabel("Amount")
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    plt.title(localtime)
    plt.savefig("Period="+str(period)+"Total="+str(total)+".png")
    # plt.show()


def saveToCSV(investmentList,period,total):
    localtime=time.strftime("-日期%Y%m%d-时间%H%M", time.localtime())
    try:
        csvF=open("投资计划-期数"+str(period)+"-总额"+str(total)+localtime+".csv","w")
    except:
        print("创建文件出错，若已打开表格，请关闭表格后重新运行本程序。")
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

def main(f,period,total):
    standardList,sum=sampling(f,period)
    investmentList = [v * (total/sum) for v in standardList]
    # print(investmentList)
    drawAndSave(investmentList,period,total)

    sum2=0
    for v in investmentList:
        sum2+=v
    # print("实际投资总额:"+str(sum2))

    saveToCSV(investmentList,period,total)


period=int(input('请输入定投期数:\n '))
# period=5

total=float(input('请输入定投总金额:\n'))
# total=2000

# print("定投期数:"+str(period),"定投总金额:"+str(total))

main(quadraticF,period,total)

input("按回车键关闭程序...")



