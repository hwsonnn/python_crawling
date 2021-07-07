def fileToStr(filename) :
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    f.close()

    return data

if __name__ == "__main__" :
    fname = input("파일명을 입력하세요")
    data = fileToStr(fname)
    print(data)
