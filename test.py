import streamlit as st
import pandas as pd
from functools import lru_cache


st.markdown("""

# 微分方程的基本概念

微分方程:含有**未知函数**、未知函数的**导数**与**自变量**的方程

微分方程的**阶**:微分方程中未知函数**导数的最高阶数**

n阶微分方程的一般形式:
$$
F(x,y,y',y'',\cdots,y^{(n)})=0
$$


$$\large
\\begin{align}
 & \\begin{cases}
常微分方程  & 方程中未知函数为\\textbf{一元函数}\\\\
偏微分方程  & u=u(x,y)，\\frac{\partial u}{\partial x}+\\frac{\partial u}{\partial y}=x+y
\end{cases}\\
 & \\begin{cases}
线性 &未知\\textbf{函数} y 及其\\textbf{各阶导数}都是一次的\\
非线性  & y''=x\cdot(y')^2-y=1
\end{cases}
\end{align}
$$

微分方程的**解**:代入微分方程使方程成为恒等式的函数
$$
y'=2x\longrightarrow y=x^2\longrightarrow y=x^2+C
$$
通解:n阶微分方程，含有n个**相互独立**的任意常数的解
$$
y''=0\longrightarrow y=x\longrightarrow y=C_1 x+C_2
$$
初值条件:确定任意常数的条件
特解:确定了通解中的任意常数后的解


# 一阶微分方程
## 1 可分离变量的微分方程

方程可化为

$$
\\frac{dy}{dx}=f(x)\cdot g(y)
$$

解法

(1) 若 $g(y)\\neq 0$，分离变量 
$$ \\frac{dy}{g(y)} = f(x)\,dx $$
两边积分
$$ \int\\frac{dy}{g(y)} = \int f(x)\,dx \quad\\rightarrow\quad G(y) = F(x) + C $$
(2) 若存在 $y=y_0$ 使得 $g(y_0)=0$，则 $y=y_0$ 也是方程的解
$$ y=1,\quad \\frac{dy}{dx}=0,\quad f(x)\cdot g(y_0)=0$$

**例** 求微分方程 $\displaystyle \\frac{dy}{dx} = 2xy$ 的通解
**解** 若 $y \\neq 0$，分离变量： $$ \\frac{dy}{y} = 2x\,dx $$ 两边积分：
$$ \int \\frac{1}{y} \, dy = \int 2x \, dx $$
$$ \ln|y| = x^2 + C_1 $$
$$ |y| = e^{\ln|y|} = e^{x^2 + C_1} \quad\\rightarrow\quad y = \pm e^{C_1} \cdot e^{x^2} $$
若 $y=0$，则 $y=0$ 也是方程的解
综上，通解为：
$$ y = C \cdot e^{x^2} $$

**例** 求微分方程 $y\,dx + x^2 dy - 4 dy = 0$ 满足 $y|_{x=1}=2$ 的特解
**解** 整理方程： $$ y\,dx + (x^2 - 4) dy = 0 \quad\\rightarrow\quad y\,dx = (4 - x^2) dy $$ 分离变量
$$ \\frac{dy}{y} = \\frac{dx}{4 - x^2} $$
两边积分
$$ \int \\frac{1}{y} dy = \int \\frac{1}{4 - x^2} dx $$
$$ \ln|y| = \\frac{1}{4} \ln\left| \\frac{2 + x}{2 - x} \\right| + C_1 $$
$$ 4\ln|y| = \ln\left| \\frac{2 + x}{2 - x} \\right| + 4C_1 $$
令 $C = e^{4C_1}$，整理得： 
$$ \ln|y|^4 = \ln\left| C \cdot \\frac{2 + x}{2 - x} \\right| \quad\\rightarrow\quad y^4 = C \cdot \\frac{2 + x}{2 - x} $$
代入初始条件 $x=1,\ y=2$： 
$$ 2^4 = C \cdot \\frac{2+1}{2-1} \quad\\rightarrow\quad 16 = 3C \quad\\rightarrow\quad C = \\frac{16}{3} $$
因此特解为 
$$ y^4 = \\frac{16}{3} \cdot \\frac{2 + x}{2 - x} $$

## 2 齐次方程

指数位置次数一样
$$
\\begin{align}
\\frac{dy}{dx}  & = \\frac{x^3 + x^2y + xy^2}{y^3}  \\
 & = \\frac{1 + \\frac{y}{x} + \left(\\frac{y}{x}\\right)^2}{\left(\\frac{y}{x}\\right)^3}  \\
 & = \\frac{1 + u + u^2}{u^3} 
\end{align}
$$
令 $u = \\frac{y}{x}$，转换以后再处理

方程可化为 $\\frac{dy}{dx}=\\varphi(\\frac{y}{x})$，$x$ 为自变量，$y,u$ 为函数
解法 换元 $u=\\frac{y}{x}\Longleftrightarrow y=u\cdot x\Longrightarrow dy=udx+xdu$

> $y'=u'x+u,dy=y'dx=u'xdx+udx$

代入方程
$$
u+x\\frac{du}{dx}=\\varphi(u)\Longleftrightarrow x\\frac{du}{dx}=\\varphi(u)-u
$$
若 $\\varphi(u)-u\\not=0 \Longrightarrow \\frac{du}{\\varphi(u)-u}=\\frac{dx}{x}$，求解出
$$
G(u)=ln|x|+C
$$
后，再用 $u = \\frac{y}{x}$ 代回解出 $y$
若有 $u=u_0$,使得 $\\varphi(u_0)-u_0=0$，则由 $u=\\frac{y}{x}$ 可知 $\\frac{y}{x}=u_0$

**例** 求微分方程 $(x^2 + y^2)dx - xy\,dy = 0$ 的通解
**解** 
$$ xy\,dy = (x^2 + y^2)dx $$
当 $y=0$ 时，$x^2dx=0$，不满足原方程，故不是方程的解
当 $y \\neq 0$ 时，两边同除以 $xy$ 
$$ \\frac{dy}{dx} = \\frac{x^2 + y^2}{xy} = \\frac{1 + \left(\\frac{y}{x}\\right)^2}{\\frac{y}{x}} $$
令 $u = \\frac{y}{x}$，则 $y = ux$，两边对 $x$ 求导 
$$ dy = u\,dx + x\,du $$
代入方程
$$ u + x\\frac{du}{dx} = \\frac{1 + u^2}{u} $$
化简
$$ x\\frac{du}{dx} = \\frac{1 + u^2}{u} - u = \\frac{1}{u} $$
分离变量：
$$ u\,du = \\frac{1}{x}dx $$
两边积分
$$ \int u\,du = \int \\frac{1}{x}dx $$
$$ \\frac{1}{2}u^2 = \ln|x| + C $$
回代 $u = \\frac{y}{x}$，得到通解： 
$$ \\frac{1}{2}\left(\\frac{y}{x}\\right)^2 = \ln|x| + C $$

**例** 求微分方程 $y' = \left| \\frac{x}{y} \\right| + \\frac{y}{x}$，满足 $y|_{x=1}=2$ 的特解
**解** 初始条件 $x=1>0,\ y=2>0$，所以 $x,y>0$，$\left| \\frac{x}{y} \\right| = \\frac{x}{y}$，方程化为
$$ \\frac{dy}{dx} = \\frac{x}{y} + \\frac{y}{x} = \\frac{1}{\\frac{y}{x}} + \\frac{y}{x} $$
令 $u = \\frac{y}{x}$，则 $y = ux$，求导得
$$ dy = u\,dx + x\,du $$
代入方程
$$ u + x\\frac{du}{dx} = \\frac{1}{u} + u $$
化简
$$ x\\frac{du}{dx} = \\frac{1}{u} $$
分离变量 
$$ u\,du = \\frac{1}{x}dx $$
两边积分
$$ \int u\,du = \int \\frac{1}{x}dx $$
$$ \\frac{1}{2}u^2 = \ln|x| + C $$
回代 $u = \\frac{y}{x}$
$$ \\frac{1}{2}\left(\\frac{y}{x}\\right)^2 = \ln|x| + C $$
代入初始条件 $x=1,\ y=2$
$$ \\frac{1}{2}\left(\\frac{2}{1}\\right)^2 = \ln 1 + C \quad\\rightarrow\quad C = 2 $$
因此特解为
$$ \\frac{1}{2}\left(\\frac{y}{x}\\right)^2 = \ln|x| + 2 $$

## 3 一阶线性微分方程

$$ \\begin{cases} \displaystyle \\frac{dy}{dx} + P(x)\cdot y = 0 & 齐次 \\\[1em] \displaystyle \\frac{dy}{dx} + P(x)\cdot y = Q(x) & 非齐次 \end{cases} $$

**齐次**
$$ \\frac{dy}{dx} + P(x)\cdot y = 0 $$
整理得
$$ \\frac{dy}{dx} = -P(x)\cdot y $$
若 $y \\neq 0$，分离变量
$$ \\frac{dy}{y} = -P(x)\,dx $$
两边积分： 
$$ \int \\frac{1}{y} dy = \int -P(x)dx $$
$$ \ln|y| = \int -P(x)\,dx + C_1 $$
去掉绝对值： 
$$ 
|y| = e^{\int -P(x)\,dx + C_1} 
$$
$$
y= \pm e^{C_1} \cdot e^{-\int P(x)\,dx} 
$$
若 $y=0$，也是方程的通解
令 $C = \pm e^{C_1}$，则通解为： 
$$ y = C \cdot e^{-\int P(x)\,dx} $$

**非齐次**
$$
y' =- P(x)\cdot y+  Q(x) 
$$
由于齐次
$$
y' =- P(x)\cdot y
$$
的通解为
$$
 y = C \cdot e^{-\int P(x)\,dx} 
$$
所以猜想非齐次的通解形式为
$$
y=C(x) \cdot e^{-\int P(x)\,dx} 
$$
所以非齐次
$$
\\frac{dy}{dx} = -P(x)\cdot y + Q(x)
$$
解： 
$$ \\frac{dy}{dx} = -P(x)\cdot C(x)\cdot e^{\int -P(x)dx} + C'(x)\cdot e^{\int -P(x)dx} $$
$$ \\frac{dy}{dx} = -P(x)\cdot y + C'(x)\cdot e^{\int -P(x)dx} $$
$$
C'(x)\cdot e^{-\int P(x)dx} = Q(x)
$$
$$
C'(x)= Q(x)\cdot e^{\int P(x)dx}
$$
$$ C(x) = \int C'(x)dx = \int Q(x)\cdot e^{\int P(x)dx}dx + C $$
通解
$$ y = \left[ \int Q(x)\cdot e^{\int P(x)dx}dx + C \\right] \cdot e^{-\int P(x)dx} $$

> [!note] 
> **齐次**
> $$ \\frac{dy}{dx} + P(x)\cdot y = 0 $$
> 通解
> $$ y = C \cdot e^{-\int P(x)dx} $$
> **非齐次**
> $$ \\frac{dy}{dx} + P(x)\cdot y = Q(x) $$
> 通解
> $$ y = e^{-\int P(x)dx} \left[ \int Q(x)\cdot e^{\int P(x)dx} dx + C \\right] $$

**例** 求微分方程 $\displaystyle \\frac{dy}{dx} + 2xy = 4x$ 的通解
**解** 其中 $P(x) = 2x,\quad Q(x) = 4x$ 

代入

$$
\\begin{align*} y &= e^{-\int 2x dx} \left[ \int 4x \cdot e^{\int 2x dx} dx + C \\right] \\ &= e^{-x^2} \left[ \int 4x e^{x^2} dx + C \\right] \\ &= e^{-x^2} \left[ 2 e^{x^2} + C \\right] \\end{align*}
$$ 

# 高阶微分方程

## 1 可降阶的高阶微分方程

总共分为三类

$$
\\begin{cases} y^{(n)} = f(x) \\\[1em] y'' = f(x, y') \quad \\text{特点：不显含 } y \\\[1em] y'' = f(y, y') \quad \\text{特点：不显含 } x \end{cases}
$$

**类型一** $y^{(n)} = f(x)$
**解法** 等式两端同时反复积分

**例** 求微分方程 $y''' = 2x$ 的通解
**解**
$$ \int y''' dx = \int 2x dx \quad \\rightarrow \quad y'' = x^2 + C_1 $$
$$ \int y'' dx = \int (x^2 + C_1) dx \quad \\rightarrow \quad y' = \\frac{1}{3}x^3 + C_1 x + C_2 $$
$$ \int y' dx = \int \left( \\frac{1}{3}x^3 + C_1 x + C_2 \\right) dx $$
$$ y = \\frac{1}{12}x^4 + \\frac{C_1}{2}x^2 + C_2 x + C_3 $$

**类型二** $y'' = f(x, y')$ 特点：不显含 $y$
**解法** 做变换，令 $y'=p$ , $y''=p'$
代入原方程 $p'=f(x,p)$ ，用一阶微分方程求解

**例** 求微分方程 $xy'' - y' = x^2$ 的通解（不显含 $y$） 
**解** 令 $y' = p$，则 $y'' = p'$
$$ xp' - p = x^2 \quad\\rightarrow\quad \\frac{dp}{dx} - \\frac{1}{x}p = x $$
这里 $p(x) = -\\frac{1}{x},\ Q(x) = x$
由一阶线性微分方程通解公式
$$ p = e^{\int \\frac{1}{x}dx} \left[ \int x \cdot e^{-\int \\frac{1}{x}dx} dx + C_1 \\right] $$
解得
$$ p = x^2 + C_1 x \quad\\rightarrow\quad y' = x^2 + C_1 x $$
再积分
$$ \int y' dx = \int (x^2 + C_1 x) dx $$
$$ y = \\frac{1}{3}x^3 + \\frac{C_1}{2}x^2 + C_2 $$

**类型三** $y'' = f(y,\ y')$ 特点：不显含 $x$ 
**解法** 做变换，令 $y' = p$，**将 $p$ 看作 $y$ 的函数**
$$ y'' = \\frac{dp}{dx} = \\frac{dp}{dy} \cdot \\frac{dy}{dx} = p \cdot \\frac{dp}{dy} $$
代入方程
$$ p \cdot \\frac{dp}{dy} = f(y,\ p) $$
用关于 $p$ 和 $y$ 的一阶微分方程求解

**例** 求微分方程 $yy'' - (y')^2 = 0$ 的通解（不显含 $x$） 
**解** 令 $y' = p$，则 
$$ y'' = \\frac{dp}{dx} = \\frac{dp}{dy} \cdot \\frac{dy}{dx} = p \cdot \\frac{dp}{dy} $$
代入原方程
$$ y \cdot p \cdot \\frac{dp}{dy} - p^2 = 0 \quad\\rightarrow\quad p \left[ y \cdot \\frac{dp}{dy} - p \\right] = 0 $$
若 $p = 0$，则 $y' = 0$，解得 $y = C_1$（常数解）
若 $p \\neq 0$，则 $y \cdot \\frac{dp}{dy} - p = 0$，解得 $p = C_2 y$，即
$$ y' = C_2 y \quad\\rightarrow\quad \\frac{dy}{dx} = C_2 y \quad\\rightarrow\quad y = C_3 e^{C_2 x} $$

## 2 n 阶线性微分方程

$$ y^{(n)} + a_1(x)\cdot y^{(n-1)} + \cdots + a_{n-1}(x)\cdot y' + a_n(x)\cdot y = f(x) $$
$x$ 为自变量
$y$ 为未知函数

### 2.1 二阶线性微分方程

$$ y'' + P(x)\cdot y' + Q(x)\cdot y = 0 \quad \\text{齐次} $$
$$ y'' + P(x)\cdot y' + Q(x)\cdot y = f(x) \quad \\text{非齐次} $$

线性微分方程的解的结构

### 2.2 齐次 $y'' + P(x)\cdot y' + Q(x)\cdot y = 0$

**性质1** 若 $y_1$ 和 $y_2$ 都是齐次方程的解，则 $c_1\cdot y_1+c_2 \cdot y_2$ 也是齐次方程的解
**证明** 令 $y^* = C_1 y_1 + C_2 y_2$ 
$$ (y^*)' = C_1 y_1' + C_2 y_2' $$
$$ (y^*)'' = C_1 y_1'' + C_2 y_2'' $$
将 $y^*$ 代入方程 $(y^*)'' + P(x)(y^*)' + Q(x)y^* = 0$： 
$$
\\begin{align}
  & (C_1 y_1'' + C_2 y_2'') + P(x)(C_1 y_1' + C_2 y_2') + Q(x)(C_1 y_1 + C_2 y_2) \\ =& \left(C_1 y_1'' + P(x)C_1 y_1' + Q(x)C_1 y_1\\right) + \left(C_2 y_2'' + P(x)C_2 y_2' + Q(x)C_2 y_2\\right) \\ =& C_1\left(y_1'' + P(x)y_1' + Q(x)y_1\\right) + C_2\left(y_2'' + P(x)y_2' + Q(x)y_2\\right) \\ =& C_1 \cdot 0 + C_2 \cdot 0 = 0 
\end{align}
$$

> 结论是解，但不是通解，因为通解的定义是含有2个**相互独立**的任意常数的解

**性质2** 若 $y_1$ 和 $y_2$ 都是齐次方程的两个**线性无关**的**特解**，则方程的**通解**为 $y=c_1 \cdot y_1+c_2 \cdot y_2$

### 2.3 非齐次 $y'' + P(x)\cdot y' + Q(x)\cdot y = f(x)$

$$ y'' + P(x)\cdot y' + Q(x)\cdot y = 0 \quad \\text{齐次} $$
$$ y'' + P(x)\cdot y' + Q(x)\cdot y = f(x) \quad \\text{非齐次} $$
两个是相对应的，即一个等于0，一个等于 $f(x)$

**性质3** 若 $y_1$ 和 $y_2$ 都是非齐次方程的解，则 $y_1 - y_2$ 是齐次方程的解

**证明** 令 $y^* = y_1 - y_2$，则
$$ (y^*)' = y_1' - y_2' $$
$$ (y^*)'' = y_1'' - y_2'' $$
将 $y^*$ 代入齐次方程 $y'' + P(x)y' + Q(x)y = 0$
$$
\\begin{align*} & (y^*)'' + P(x)(y^*)' + Q(x)y^* \\ =& (y_1'' - y_2'') + P(x)(y_1' - y_2') + Q(x)(y_1 - y_2) \\ =& \left(y_1'' + P(x)y_1' + Q(x)y_1\\right) - \left(y_2'' + P(x)y_2' + Q(x)y_2\\right) \\ =& f(x) - f(x) = 0 \end{align*}
$$

**性质4** 若 $y_1$ 是**齐次方程**的解，$y_2$ 是**非齐次方程**的解，则 $y_1+y_2$ 是**非齐次方程**的解

若 $y = C_1 y_1 + C_2 y_2$ 是齐次方程的通解，且 $y^*$ 是非齐次方程的特解，则由性质3可知，任意一个非齐次方程的解 $\widetilde{y}$ 满足
$$ \widetilde{y} - y^* = C_1 y_1 + C_2 y_2 $$
即非齐次方程的通解为
$$ \widetilde{y} = C_1 y_1 + C_2 y_2 + y^* $$

> 非齐的通解 = 齐次通解+非齐特解

由此可知:欲求非齐次线性微分方程的通解
(1) 先求**齐次**线性微分方程的**通解**
(2) 再找一个**非齐次**线性微分方程的**特解**

**性质5 (叠加原理)** 若 $y_1$ 是方程 $y'' + P(x)y' + Q(x)y = f_1(x)$ 的解， 且 $y_2$ 是方程 $y'' + P(x)y' + Q(x)y = f_2(x)$ 的解， 则 $y_1 + y_2$ 是方程 $y'' + P(x)y' + Q(x)y = f_1(x) + f_2(x)$ 的解
**证明** 令 $y^* = y_1 + y_2$，则 
$$ (y^*)' = y_1' + y_2' $$
$$ (y^*)'' = y_1'' + y_2'' $$
将 $y^*$ 带入方程 
$$
\\begin{align*}& (y^*)'' + P(x)(y^*)' + Q(x)y^*\\
=& (y_1'' + y_2'') + P(x)(y_1' + y_2') + Q(x)(y_1 + y_2) \\ =& \left(y_1'' + P(x)y_1' + Q(x)y_1\\right) + \left(y_2'' + P(x)y_2' + Q(x)y_2\\right) \\ =& f_1(x) + f_2(x) \end{align*}
$$

叠加原理一般用于拆分微分方程
$$ y'' + x y' + y = 1 + \sin x + e^x $$
拆分： 
$$\\begin{cases} y'' + x y' + y = 1 & (y_1) \\ y'' + x y' + y = \sin x & (y_2) \\ y'' + x y' + y = e^x & (y_3) \end{cases}
$$
解为 $y_1+y_2+y_3$

## 3 二阶常系数线性微分方程

二阶线性微分方程： 
$$ y'' + P(x)y' + Q(x)y = 0 \quad \\text{齐次} $$
$$ y'' + P(x)y' + Q(x)y = f(x) \quad \\text{非齐次} $$
二阶（常系数）线性微分方程： 
$$ y'' + py' + qy = 0 \quad \\text{齐次} $$
$$ y'' + py' + qy = f(x) \quad \\text{非齐次} $$

### 3.1 齐次 $y'' + py' + qy = 0$

**例** 分析方程的特解 $y''+y'-2y=0 \Longleftrightarrow y''+y'=2y$
此处 $y$ 的导数与 $y$ 一致，故推断 $y=e^x$
$$
({e^x})'=e^x=y~,~({e^x})''=e^x=y
$$
则
$$ y'' + y' - 2y = 0 \iff y'' + y' = 2y $$
$$ y'' + y' - 6y = 0 \iff y'' + y' = 6y $$
 齐次方程
$$ y'' + p y' + q y = 0 \iff y'' + p y' = -q y $$
设 $y = e^{rx}$，则
$$ y' = r e^{rx} = r y $$
$$ y'' = r^2 e^{rx} = r^2 y $$
 代入
$$ y'' + p y' = r^2 y + p r y = (r^2 + p r) y $$

由上例，猜测齐次方程 $y'' + py' + qy = 0$ 的特解为 $y^*=e^{r\cdot x}$
分析
$$ (y^*)' = r e^{rx} $$
$$ (y^*)'' = r^2 e^{rx} $$
带入方程
$$ r^2 e^{rx} + p \cdot r e^{rx} + q \cdot e^{rx} = 0 \iff (r^2 + pr + q) \cdot e^{rx} = 0 $$
因为 $e^{rx} \\neq 0$，所以
$$ r^2 + pr + q = 0 $$
当 $r$ 满足此等式，则 $e^{rx}$ 为微分方程的解
其中 $r^2 + pr + q = 0$ 称为**特征方程**，由判别法 $\Delta=p^2-4q$

$$
\\begin{cases} \Delta = p^2 - 4q > 0 & \\text{两个不相等的实根}  & r_1 \\neq r_2 \\\[1em] \Delta = p^2 - 4q = 0 & \\text{两个相等的实根}  &r_1=r_2  \\\[1em] \Delta = p^2 - 4q < 0 & \\text{共轭虚根} & r_1,r_2=\\alpha\pm \\beta_i  \end{cases}
$$
            
(1) 如果有两个不相等的实根，那么$\dfrac{e^{r_1 x}}{e^{r_2 x}} = e^{(r_1 - r_2)x}\\not\equiv$ 常数 $\Longrightarrow$ 两个特解线性无关，由性质2得到齐次通解
(2) 如果有两个相等的实根，那么只找到一个特解 $y_1=e^{r_1x}$，需要特解非常数，那么就要找一个线性无关的特解，此时令 $\\frac{y_2}{y_1}=u(x)$，$y_2=y_1\cdot u(x)=u(x)\cdot e^{r_1 x}$
将 $y_2$ 代入齐次方程
$$
y_2 ''=(u''+2r_1\cdot u'+r_1^2 \cdot u)e^{r_1 x}\quad y_2 '=(u'+r_1\cdot u)e^{r_1 x}
$$
得到一个 $u(x)$ 的微分方程，其中
含 $u$ 的项 
$$ (r_1^2 + pr_1 + q)u = 0 \cdot u = 0 $$
含 $u'$ 的项
$$ (2r_1 + p)u' = 0 \cdot u' = 0 $$
于是解出
$$ u''(x) = 0 $$
即若 $y_2$ 是 $y_1$ 线性无关的特解，那么需要 $u''(x)=0$ ，可设$u(x)=x$，$y_2=xe^{r_1 x}$，从而由性质2得到齐次通解
(3) 两个特解为$e^{r_1 x}$,$e^{r_2 x}$，由于是两个虚根，由欧拉公式变形得
$$
\\begin{align}
e^{\\alpha x}\cdot sin \\beta x\\
e^{\\alpha x}\cdot cos \\beta x
\end{align}
$$
得到两个特解，从而由性质2得到齐次通解

**总结**：齐次 $y'' + py' + qy = 0$ 求解步骤
(1) 写出特征方程： $r^2 + pr + q = 0$
(2) 求出特征方程的根：$r_1, r_2$ 
(3) 根据特征方程的根写出通解

| 特征根的情况                             | 线性无关的两个特解                                               |
| ---------------------------------- | ------------------------------------------------------- |
| 实根 $r_1 \\neq r_2$                  | $e^{r_1 x},\quad e^{r_2 x}$                             |
| 实根 $r_1 = r_2$                     | $e^{r_1 x},\quad x e^{r_1 x}$                           |
| 复数根 $r_{1,2} = \\alpha \pm \\beta i$ | $e^{\\alpha x}\sin\\beta x,\quad e^{\\alpha x}\cos\\beta x$ |

**例** 求微分方程 $y'' - 2y' - 3y = 0$ 的通解
**解** 特征方程
$$r^2 - 2r - 3 = 0$$
特征根
$$r_1 = 3,\quad r_2 = -1$$
两个线性无关的特解
$$y_1 = e^{3x},\quad y_2 = e^{-x}$$
通解
$$y = C_1 e^{3x} + C_2 e^{-x}$$

**例** 求微分方程 $y'' - 2y' + 5y = 0$ 的通解
**解** 特征方程
$$r^2 - 2r + 5 = 0$$
特征根
$$
\\begin{align*} r^2 - 2r + 1 + 4 &= 0 \\ (r - 1)^2 &= -4 \\ r - 1 &= \pm 2i \\ r &= 1 \pm 2i \end{align*}
$$
两个线性无关的特解
$$y_1 = e^x \sin 2x,\quad y_2 = e^x \cos 2x$$
通解
$$y = C_1 e^x \sin 2x + C_2 e^x \cos 2x$$


### 3.2 非齐次 $y'' + py' + qy = f(x)$

分两种类型
$$
f(x) = \\begin{cases} \\begin{align}
 & e^{\lambda x} \cdot P_n(x) \\\[2em]  & e^{\lambda x} \cdot \left[ P_n(x) \cdot \sin(\omega x) + P_l(x) \cdot \cos(\omega x) \\right] 
\end{align}
\end{cases}
$$

 其中，$P_n(x)$ 为 $n$ 次多项式，$P_l(x)$ 为 $l$ 次多项式

> [!note]
> 非齐次的通解=齐次通解+非齐次特解


**类型1** $y'' + py' + qy = e^{\lambda x} \cdot P_n(x)$

**例1**
$y'' + 3y' + y = e^{2x} \cdot (5x^2 + x + 1)$　　$\lambda = 2,\quad P_n(x) = 5x^2 + x + 1$

**例2**
$2y'' + y = e^{x} \cdot 1$　　$\lambda = 1,\quad P_n(x) = 1$

**例3**
$5y'' + y' + 4y = x \cdot e^{0x}$　　$\lambda = 0,\quad P_n(x) = x$

特解形式： $y^* = x^k \cdot e^{\lambda x} \cdot Q_n(x)$ 
其中 $P_n(x)$ 与 $Q_n(x)$ 次数相同，$k$ 是待定常数，待定 $n$ 次多项式
$$
Q_n(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
$$
将 $y^*$ 带入非齐次方程，确定特解中的系数
由特征方程
$$r^2 + p \cdot r + q = 0$$
解出特征根 $r_1,\ r_2$ 

| $\lambda$ 和特征根 $r_1, r_2$ 的关系         | 特解形式                                         | $k$   |
| ------------------------------------- | -------------------------------------------- | ----- |
| $\lambda \\neq r_1,\ \lambda \\neq r_2$ | $y^* = x^0 \cdot e^{\lambda x} \cdot Q_n(x)$ | $k=0$ |
| $\lambda = r_1,\ \lambda \\neq r_2$    | $y^* = x^1 \cdot e^{\lambda x} \cdot Q_n(x)$ | $k=1$ |
| $\lambda = r_1,\ \lambda = r_2$       | $y^* = x^2 \cdot e^{\lambda x} \cdot Q_n(x)$ | $k=2$ |

例 求微分方程 $2y'' + y' - y = 2e^{x}$ 的通解 $\lambda=1,\ P_n(x)=2$ 
解 对应的齐次方程：$2y'' + y' - y = 0$ 
特征方程：$2r^2 + r - 1 = 0$
特征根：$r_1 = \\frac{1}{2},\ r_2 = -1$ 
齐次方程通解：$Y(x) = C_1 e^{\\frac{1}{2}x} + C_2 e^{-x}$ 
非齐次方程特解：$y^* = x^k \cdot e^{\lambda x} \cdot Q_n(x)$
由于 $\lambda \\neq r_1,\ \lambda \\neq r_2$，故
非齐次方程特解
$$y^* = x^0 \cdot e^x \cdot b = b e^x$$
$$(y^*)' = b e^x,\quad (y^*)'' = b e^x$$
代入方程
$$2b e^x + b e^x - b e^x = 2e^x \quad \\rightarrow \quad b=1$$
所以
$$y^* = e^x$$
非齐次方程通解
$$y = Y(x) + y^* = C_1 e^{\\frac{x}{2}} + C_2 e^{-x} + e^x$$


**类型2** $y'' + py' + qy =e^{\lambda x} \cdot \left[ P_n(x) \cdot \sin(\omega x) + P_l(x) \cdot \cos(\omega x) \\right]$

**例1**
$$ y'' - 3y' + 2y = e^{3x} \cdot  (5x^2 + x + 1)\sin x \Longrightarrow e^{3x} \cdot \left[ (5x^2 + x + 1)\sin x + 0 \cdot \cos x \\right]$$

**例2**
$$ y'' + 5y' + 4y = \cos 2x \Longrightarrow e^{0x} \cdot \left[ 0 \cdot \sin 2x + 1 \cdot \cos 2x \\right] $$

特解形式
$$ y^* = x^k \cdot e^{\lambda x} \cdot \left[ Q_1(x) \cdot \sin(\omega x) + Q_2(x) \cdot \cos(\omega x) \\right] $$
其中 $k$ 是待定常数，待定 $m$ 次多项式 $Q_1(x),\ Q_2(x)$，且 $m = \max\{n, l\}$ 
将 $y^*$ 带入非齐次方程，确定特解中的系数
$$ k = \\begin{cases} 0 & \lambda \pm \omega i \\text{ 不是特征根} \\ 1 & \lambda \pm \omega i \\text{ 是特征根} \end{cases} $$

由特征方程 $r^2 + p \cdot r + q = 0$ 解出特征根：

| $\lambda \pm \omega i$ 和特征根的关系 | 特解形式 |
|---|---|
| $\lambda \pm \omega i$ 不是特征根 | $e^{\lambda x} \cdot \left[ Q_m(x) \cdot \sin(\omega x) + R_m(x) \cdot \cos(\omega x) \\right]$ |
| $\lambda \pm \omega i$ 是特征根 | $x \cdot e^{\lambda x} \cdot \left[ Q_m(x) \cdot \sin(\omega x) + R_m(x) \cdot \cos(\omega x) \\right]$ |


# 差分方程

差分就是数列后一项减去前一项
设函数 $y = f(t)$ 中的自变量 $t$ 为自然数，并记 $y_t = f(t)$， 则差 $y_{t+1} - y_t$ 称为函数的一阶差分，简称差分，记作 $\Delta y_t = y_{t+1} - y_t$

二阶差分就是一阶差分的差分
把 $\Delta y_t = y_{t+1} - y_t$ 也当做 $t$ 的函数，进一步进行差分，即 
$$
\\begin{align}
 \Delta^2 y_t  = \Delta(\Delta y_t) 
  & = \Delta y_{t+1} - \Delta y_t  \\
  & = (y_{t+2} - y_{t+1}) - (y_{t+1} - y_t)  \\
  & = y_{t+2} - 2y_{t+1} + y_t 
\end{align}
$$

**差分的性质** (可类比微分)
(1) 线性性质
$$\Delta(au_t + bv_t) = a\Delta u_t + b\Delta v_t$$
(2) 乘积性质
$$\Delta(u_t v_t) = v_t\Delta u_t + u_{t+1}\Delta v_t = u_t\Delta v_t + v_{t+1}\Delta u_t$$
(3) 商的性质
$$\Delta\left(\\frac{u_t}{v_t}\\right) = \\frac{v_t\Delta u_t - u_t\Delta v_t}{v_{t+1}v_t}$$

## 1 一阶常系数线性差分方程

形如 $y_{t+1} +ay_t=f(t)$ 为一阶常系数线性差分方程，其中 $a\\ne 0$

(1) 一阶常系数线性**齐次**差分方程
如果 $f(t)=0$，则变为齐次形式
$$y_{t+1} + a y_t = 0$$
其通解为： 
$$y_t = C(-a)^t$$
$C$ 为任意常数. 这种类型是一个等比数列，公比为 $-a$

(2) 一阶常系数线性**非齐次**差分方程
$f(t) \\ne 0$，则为非齐次类型. 解的结构与微分方程一样是对应的**齐次通解+非齐次特解**

(3) 若 $f(t) = P_m(t) \cdot d^t$，其中 $P_m(t)$ 为 $t$ 的 $m$ 次多项式，则方程有特解
$$ y_t^* = t^k Q_m(t) d^t $$
其中 $Q_m(t)$ 为 $t$ 的 $m$ 次**一般**多项式
差分方程 $y_{t+1}+ay_{t}=P_m(t) \cdot d^t$ 的特征方程为
$$
\lambda+a=0\Longrightarrow \lambda=-a
$$
从而若 $a \\ne -d$，则 $k=0$；若 $a = -d$，则 $k=1$

## 2 二阶常系数线性**齐次**差分方程 

二阶常系数线性齐次差分方程的一般形式是
$$y_{t+2} + a y_{t+1} + b y_t = 0$$
其中 $b \\ne 0$
与二阶常系数线性齐次微分方程类似，特征方程为
$$\lambda^2 + a\lambda + b = 0$$
设两个特征根分别为 $\lambda_1$ 和 $\lambda_2$，则根据两个特征根的不同情况，通解也有三种类型
(1) 两个不相等的特征根，则通解为
$$y_t = C_1 \lambda_1^t + C_2 \lambda_2^t$$
(2) 两个相等的特征根，通解为
$$y_t = (C_1 + C_2 t)\lambda^t$$
(3) 一对共轭复根 $\lambda_{1,2} = a \pm bi$，则通解为
$$y_t = r^t\left(C_1 \cos\\beta t + C_2 \sin\\beta t\\right)$$
其中 $r = \sqrt{a^2 + b^2}$，$\\beta = \\arctan\\frac{b}{a}$， $C_1, C_2$ 为任意常数



# 经济应用

## 1 成本收益、弹性

(1) 成本函数

**总成本函数**：$C(x)$，其中 $x$ 为产量(或需求量)
总成本=固定成本+可变成本 
$$C(x) = C_0 + C_1(x)$$
**固定成本**：$C_0$，不生产时仍需支出的成本
**可变成本**：$C_1(x)$，随产量变动的成本

**平均成本**： 
$$\overline{C}(x) = \\frac{C(x)}{x}$$
经济意义：平均生产一单位产品的成本 

**边际成本**：$C'(x)$，即总成本函数关于产量 $x$ 的一阶导函数
由于 $C(x) = C_0 + C_1(x)$，所以 $C'(x) = C_1'(x)$
经济意义：再增加一单位产量，总成本会增加多少

(2) 收益函数

**总收益函数**
$$R(x) = P(x)\cdot x$$
其中 $x$ 为产量，$P$ 为商品价格，$P = P(x)$ 表示反需求曲线
**平均收益函数**：
$$\overline{R}(x) = \\frac{R(x)}{x}$$
表示平均每一单位产量的收益
**边际收益函数**：$R'(x)$，表示增加一单位产量，所增加的收益

(3) 利润函数
**总利润函数**
$$L(x) = R(x) - C(x)$$
总利润=总收入-总成本

**平均利润函数**
$$\overline{L}(x) = \\frac{L(x)}{x} = \\frac{R(x) - C(x)}{x}$$
平均一单位产量的利润
**边际利润函数**
$$
L'(x)=R'(x)-C'(x)
$$
增加一单位产量所带来的利润

(4) 弹性:因变量的变化率与自变量的变化率的比值
$$ e = \lim_{\Delta x \\to 0} \\frac{\\frac{\Delta y}{y}}{\\frac{\Delta x}{x}} = \lim_{\Delta x \\to 0} \\frac{\Delta y}{\Delta x} \cdot \\frac{x}{y} = \\frac{x y'}{y} $$
自变量增加 1%，导致因变量增加 3%，弹性即为 3
自变量增加 1%，因变量减少 2%，弹性即为 -2

**弹性的考察方式**
1.需求的价格弹性： 
$$ e_d = -\\frac{dQ}{dP} \cdot \\frac{P}{Q} $$
由于绝大多数商品需求量与价格成反向关系，为了保证需求的价格弹性为正，公式中增加一个负号，其中 $Q=Q(P)$ 为需求函数
2.供给的价格弹性： 
$$ e_s = \\frac{dQ}{dP} \cdot \\frac{P}{Q} $$
其中 $Q=Q(P)$ 为供给函数
3.边际收益与需求价格弹性的关系
边际收益（关于产量 $x$ 的导数）
$$
\\begin{align}
R'(x) = \\frac{dR(x)}{dx}  & = \\frac{d\\bigl[x \cdot P(x)\\bigr]}{dx}  \\
 & = P + x\\frac{dP}{dx} = P\left(1 + \\frac{x}{P}\\frac{dP}{dx}\\right)  \\
 & = P\left(1 - \\frac{1}{e_d}\\right)
\end{align}
$$
边际收益（关于价格 $P$ 的导数）
$$
\\begin{align}
R'(P) = \\frac{dR(P)}{dP}  & = \\frac{d\\bigl[P \cdot x(P)\\bigr]}{dP}  \\
 & = x + P\\frac{dx}{dP} = x\left(1 + \\frac{P}{x}\\frac{dx}{dP}\\right)  \\
 & = x\left(1 - e_d\\right)
\end{align}
$$

> 一般边际收益指总收益函数 $R$ 关于产量 $x$ 的一阶导数

## 2 复利、连续复利、终值和现值

设 $A$ 为本金，$r$ 为每期利率，$n$ 为复利期数
**终值公式**
$$A_n = A(1 + r)^n$$
$A_n$ 为终值，$A$ 为现值
折现（已知终值求现值）
$$A = A_n(1 + r)^{-n}$$
$(1 + r)^{-n}$ 为折现因子
1.如果一年支付 $m$ 次利息，则每次支付利息的利率为 $\dfrac{r}{m}$(近似值)，此时 $n$ 年后的余额为 
$$ A_n = A\left(1 + \dfrac{r}{m}\\right)^{mn} $$
2.如果 $m \\to \infty$，则
$$ \lim_{m \\to \infty} A_n = A \lim_{m \\to \infty} \left(1 + \dfrac{r}{m}\\right)^{mn} = A e^{rn} $$
称为连续复利，折现因子为 $e^{-rn}$

## 3 差分方程的经济应用

**例** 某公司每年的工资总额在比上一年增加 20% 的基础上再追加 200 万元，若 $W_t$ 以表示第 $t$ 年的工资总额（百万元）
1.写出 $W_t$ 满足的差分方程，并求解该方程；  
2.若该公司在第一年开始的工资总额为 2000 万元，问 5 年后，工资总额达到多少？
**解**  
(1) 由题意得
$$
W_{t+1} = (1+0.2\%)W_t + 200
= 1.2W_t + 200
$$
差分方程为
$$
W_{t+1} = 1.2W_t + 2
$$
对应的齐次方程的通解为
$$
W_t^* = C \cdot 1.2^t
$$
非齐次特解为  
$$
W_t^{**} = -10
$$
从而非齐次通解为  
$$
W_t = C \cdot 1.2^t - 10
$$
(2) 根据已知条件可知  
$$
C = 30
$$
从而  
$$
W_t = 30 \cdot 1.2^t - 10
$$
5 年后工资总额为  
$$
W_5 = 30 \cdot 1.2^5 - 10 = 64.6496
$$

## 4 级数的经济应用

**例** 设银行存款的年利率为 r = 0.05，并依年复利计算。某基金会希望通过存款 A 万元实现第一年提取 19 万元，第二年提取 28 万元，…，第 n  年提取 (10 + 9n) 万元，并能按此规律一直提取下去，问 A 至少应为多少万元？

**解**  设 A_n 为用于第n年提取 (10 + 9n) 万元的折现值，则  
$$
A_n = (1 + r)^{-n} (10 + 9n)
$$
故  
$$
\\begin{align}
A = \sum_{n=1}^\infty A_n  & = \sum_{n=1}^\infty \\frac{10 + 9n}{(1 + r)^n}  \\
 & = 10 \sum_{n1}^\infty \\frac{1}{(1 + r)^n} + 9 \sum_{n=1}^\infty \\frac{n}{(1 + r)^n} = 200 + 9 \sum_{n=1}^\infty \\frac{n}{(1 + r)^{n-1}}
\end{align}
$$
因为
$$
S(x) = x \left( \sum_{n=1}^\infty x^n \\right)' = x \left( \\frac{x}{1-x} \\right)' = \\frac{x}{(1-x)^2}, \quad x \in (-1,1)
$$
所以  
$$
S\left(\\frac{1}{1+r}\\right) = S\left(\\frac{1}{1.05}\\right) = 420
$$
故
$$
A = 200 + 9 \\times 420 = 3980
$$

""")
