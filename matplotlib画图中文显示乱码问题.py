################################################################### 显示中文
from pylab import *  

mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体    
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题  

# 数据
t = arange(-5*pi, 5*pi, 0.01)  
y = sin(t)/t  

# 画图并添加图例
plt.plot(t, y)  
plt.title(u'这里写的是中文')  
plt.xlabel(u'X坐标')  
plt.ylabel(u'Y坐标')  

# 展示图形
plt.show()  