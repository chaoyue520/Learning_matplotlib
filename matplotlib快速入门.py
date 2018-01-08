#!/usr/bin/python
# -*- coding: UTF-8 -*-

## 参考资料
# 1、http://python.jobbole.com/85106/
# 2、https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

import matplotlib.pyplot as plt

# 查看帮助
plt.legend?



################################################################### 折线图
# 数据
x=[1,2,3,4]
y=[5,6,7,8]
x1=[1,2,3,4]
y1=[5,6,9,10]

# 画图
plt.plot(x,y,label='line one')
plt.plot(x1,y1,label='line two')

# 添加图形元素
plt.xlabel('this is X')
plt.ylabel('this is Y')
plt.title('Title is here')
plt.legend(loc=0)

# 展示图形
plt.show()



################################################################### 柱状图
# 数据
x=[1,2,3,4]
y=[5,6,7,8]

# 画图
plt.bar(x,y)

# 添加图形元素
plt.axis([0,10,0,100])
# 限定x,y轴的范围，等价于下方
plt.xlim([0,10])
plt.ylim([0,100])

# 展示图形
plt.show()


# 数据
x=np.random.randint(0,100,100)

# 设定分箱范围
bins=[0,40,80,100]

# 画图
plt.hist(x,bins)
plt.show()

################################################################### 散点图
# 数据
x=np.random.randint(0,100,100)
y=np.random.randint(0,100,100)

# 画图
plt.scatter(x,y)
plt.show()

################################################################### 散点图

# 数据
label='A','B','C'
size=[10,20,30]

# 添加图形元素
explode=(0,0.3,0)
plt.pie(size,labels=label,autopct='%1.1f%%',shadow=True,explode=explode,startangle=90)

# 设置起始点角度
plt.axis('equal')

# 展示图形
plt.show()


################################################################### 多图
# 数据
x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)
x3=np.linspace(0.0,10.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)
y3=x3*x3+2

# 画图
# 2行2列第1个位置
plt.subplot(2,2,1)
plt.plot(x1,y1,'o-')
# 2行2列第2个位置
plt.subplot(2,2,2)
plt.plot(x2,y2,'.-')
# 2行1列第2个位置
plt.subplot(2,1,2)
plt.plot(x3,y3,'^-')

# 展示图形
plt.show()


# 第一张图
plt.figure(1)

# 第一张图中的第一个子图
plt.subplot(211)
plt.plot([1,2,3])

# 第一张图中的第二个子图
plt.subplot(212)
plt.plot([4,2,9])

# 第二张图
plt.figure(2)
# 默认创建subplot(111)
plt.plot([4,5,6])

# 切换到第一张图
plt.figure(1)
# 令子图subplot(211)成为figure1的当前图
plt.subplot(211)
# 添加subplot211的标题
plt.title('this is Title')
plt.text(0.75,2,r'The text')
plt.grid(True)
plt.show()


plt.text(0,75,2,r'$mu=100,sigma=10')



################################################################### 多图叠加
import matplotlib.pyplot as plt

# 数据
t=np.arange(0.0,5,0.2)

# 画图并展示
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()

# 数据
x=np.linspace(-np.pi,np.pi,256)

# 画图并展示
plt.plot(x,np.sin(x),color='blue',linestyle='-',lw=2,label='sin line')
plt.plot(x,np.cos(x),'r--',label='cos line')
plt.xlim(-4,4)

# 标记坐标刻度
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'])  # 转义
plt.yticks([-1,0,1])
plt.show()



################################################################### 调整坐标轴
x=np.linspace(-np.pi,np.pi,256)

# 画图并展示
plt.plot(x,np.sin(x),color='blue',linestyle='-',lw=2,label='sin line')
plt.plot(x,np.cos(x),'r--',label='cos line')
plt.xlim(-4,4)

# 标记坐标刻度
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'])  # 转义
plt.yticks([-1,0,1])

# 调整坐标范围
ax=plt.gca()

# 左边和上边的边界设置为不可见
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 让x轴的标记位置显示在x坐标轴下边（默认就在下方）
ax.xaxis.set_ticks_position('bottom')
# 然后把x轴bottom这条线提到0这个位置
ax.spines['bottom'].set_position(('data',0))

# 同上
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 添加图例
plt.legend(loc=0)

#　展示图形
plt.show()