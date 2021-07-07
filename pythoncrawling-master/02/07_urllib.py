from urllib.request import urlopen

response = urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
data = response.read()
print(data)


