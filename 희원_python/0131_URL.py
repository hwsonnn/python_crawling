from urllib.request import urlopen

rs=urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
data=rs.read()

print(data)

