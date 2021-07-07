import matplotlib.pyplot as plt
#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


y1=[156,312,54,21,8,75,431,65,464,56]
y2=[653,632,4,5,12,54,6,2,5,54]
y3=[1,1,5,64,4,8,51,21,35,64]

y=[y1,y2,y3]
print(y)
print(len(y))

plt.plot(y1, label='2017')
plt.plot(y2, label='2018')
plt.plot(y3, label='2019')
  
"""
for i in range(len(y)):
    plt.plot """

plt.title('Title')
plt.legend()
plt.show()



