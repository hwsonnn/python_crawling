####### 파이썬 data type

# list와 tuple은 순서가 정해져있음.

# list : 수정 가능
x1 = ['1', 2, 2.5, [7, 8, 9]]  # 다른 프로그램 언어와 차이점은
                    # list data type은 다른 data type을 가질 수 있다는 것이다.
                    # list안에 list를 가질 수도 있다.
x1.append('안녕')


for x in x1 :
    print(x)



# 튜플(tuple) : 수정 불가능
st = ('1', 2, 2.5, [7, 8, 9])
#st[1] = 10.1
#st.append('안녕')
for x in st :
    print(x)




# data type 변환
print(type(st))
xtl = list(st)
print(type(xtl))
xt = tuple(xtl)
print(type(xt))

print('-'*30)
#슬라이싱 : 문자열, 리스트, 튜플
print(xt[:3])
print(xt[3:])

















