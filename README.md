# 定投计划计算器


本定投计划计算器，用于在规定投资期数（*投资时间间隔固定*）和投资总额的条件下，按照自定义函数计算每次定投需投入的金额。

*如下面的数学公式不能正确显示，请使用README.pdf*

## 程序使用

Windows用户双击运行`定投计划计算器.exe`，按照指示输入参数即可。（*首次启动程序耗时较长，之后启动大约需要10秒*） 

## 输入输出

输入：
- 计划投资的总期数（记为`period`）
- 计划投入的总金额 (记为`total`)
- 希望定投金额拟合的指数函数的参数`alpha`（$f(x)=x^{\alpha}$）


输出：
- 每期需投入的金额（保存为CSV文件）
- 期数-当前投入金额 散点图，附带$y=x^2, y=\sqrt{x}, y=const, y=x$四条参考线


## 计算步骤

1. 给定一个参考函数($f(x)=x^{\alpha}$)，取其在`[0,1]`区间上的一段作为标准化函数`f`
$$
f(x)=x^{\alpha},x\in\left[0,1\right]
$$

2. 根据期数，在`[0,1]`区间均匀地取`period`个点,记为`X`，求得`f`在该点处的值，记为`Y`，取其在`[0,1]`区间上的一段作为标准化函数`f`
$$
X=\lbrace 0,\frac{1}{period},\frac{2}{period},\frac{2}{period} ,...,1\rbrace \\
Y=f(X)
$$

3. 将`X`和`Y`缩放到`period`和`total`对应的范围，得到`X'`，`Y'`

$$
X^{\prime} = \lbrace period \cdot x \mid x \in X \rbrace \\
\\
sum = \sum _{x \in X}  x \\
Y^{\prime} = \lbrace \frac{total}{sum} \cdot y \mid y \in Y \rbrace \\
$$
4. 此时$\sum _{y \in Y^{\prime}} y = total$，`Y'`即为所求


## 特性

该方法适用于任何在`[0,1]`上恒为正的参考函数
