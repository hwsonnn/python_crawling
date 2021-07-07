###### 파이썬 data type

#딕셔너리(dictionary) : 키와 값의 쌍
dic = {'a' : 1, 'b' : 2, 'c' : 3}

print(dic['a'])
dic['d'] = 4    # list와 tuple과 달리 순서가 정해져있지 않으므로
                # append 쓸 필요 없음.
                # 추가
dic['b'] = 4    # 수정
print(dic)


print('-'*30)
for item in dic :
    print(item, '=>', dic[item])
    
print('-'*30)
for item in dic.items() :
    print(item)     # tuple 형태로 출력되는 것 확인

print('-'*30)
for key, value in dic.items() :
    print(key, '=>', value)

print('-'*30)
for key in dic.items() :
    print(key)      # item 과 동일 출력 확인 (즉, tuple 형태)

print('-'*30)
for value in dic.items() :
    print(value)    # item 과 동일 출력 확인 (즉, tuple 형태)








































































