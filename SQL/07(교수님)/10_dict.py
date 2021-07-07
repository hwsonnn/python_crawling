#파이썬 data type
x1 = 10     #int(정수)
x2 = 10.1   #float(실수)

x3 = "안녕하세요\n반갑습니다."   #str(문자열) , '', """.."""
x4 = """
    안녕하세요
    반갑습니다.
    """
print(x3)
print(x4)


#형변환
x1_1 = float(x1)    #int->float
x2_1 = int(x2)      #float->int
x2_2 = str(x2)      #float ->str

print(x1_1, type(x1_1))
print(x2_1, type(x2_1))
print(x2_2, type(x2_2))