###### 파이썬 data type 정리
x1 = 10   # int(정수)
x2 = 10.1 # float(실수) <== double type 존재 X

x3 = "안녕하세요.\n반갑습니다."    # str(문자열), "", """..."""
x4 = """
      안녕하세요.
      반갑습니다.
     """
print(x3)
print(x4)

# data type 변환
x1_1 = float(x1)    # int->float
x2_1 = int(x2)      # float->int
x3_1 = str(x2)      # float->str
print(x1_1) ; print(x2_1) ; print(x3_1)
print(type(x1_1)) ; print(type(x2_1)) ; print(type(x3_1))




# list, tupel
# 순서가 정해져있음

# list : 수정 가능
x5 = ['1', 2, 2.5, [7,8,9]]
    #list datetype은 다른 datatype을 가질 수 있음
    #list 안에 list를 가질 수 있음
x5[0]=10.1
x5.append('안녕')

for x in x5 :
    print(x)

# tupel : 수정 불가능
x6 = ('1', 2, 2.5, [7,8,9])
#x6[1]=10.1
#x6.append('안녕')
for x in x6 :
    print(x)

# data type 변환
print(type(x6))
x6_l = list(x6)
print(type(x6_l))
x6_t = tuple(x6_l)
print(type(x6_t))

print("-"*30)

#slicing : str,list,tuple
print(x6_t[:3])
print(x6_t[3:])
print(type(x6_t[3:]))




# Dictionary : 키와 값의 쌍
dic = {'a':1,'b':2,'c':3}
print(dic['a'])
dic['d']=4      #순서가 정해져 있지 X
                #append 쓸 필요 X
dic['b']=4      #수정 가능
print(dic)
print("-"*30)

for key, value in dic.items() :
    print(key,'=>',value)
print("-"*30)

for key in dic.items() :
    print(key)
print("-"*30)

for value in dic.items() :
    print(value)