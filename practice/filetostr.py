def fileToStr(filename) :
    f = open(filename, "r", encoding="utf-8")   #컴퓨터가 읽을 수 있도록 인코딩
    data = f.read()
    f.close()

    return data

if __name__ == "__main__" :
    fname = input("파일명을 입력하세요")
    data = fileToStr(fname)
    print(data)

#파일을 불러와줄 함수 (파일 그대로)