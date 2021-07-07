#import func
from func import fileToStr

filename = input("파일명을 입력하세요.")
data = fileToStr(filename)
print(data)