import requests
from bs4 import BeautifulSoup as bs

COURSE = "" #course id
NAME = "" #name (dash-separated0
URL = "https://app.memrise.com/course/{}/{}".format(COURSE,NAME)
COURSE_TOTAL = 0 # how many lists in course

txt = f"{URL}"

for i in range(1,COURSE_TOTAL+1):
	loc = URL + "/" + str(i)
	print(loc)

	html = requests.get(loc)
	html = html.text

	page_soup = bs(html,"html.parser")

	title = page_soup.find("h3",{"class":"progress-box-title"}).text.replace("\n","")
	counter = 0

	for c in title:
		if c == " ":
			counter += 1
		else:
			break

	newtitle = title[counter:]
	
	txt += f"\n\n{newtitle}"
	
	rows = page_soup.find_all("div",{"class":"thing text-text"})

	for row in rows:
		col_a = row.find("div",{"class":"col_a col text"})
		spanish = [*col_a][0].text
		
		col_b = row.find("div",{"class":"col_b col text"})
		english = [*col_b][0].text
		
		txt += f"\n{spanish} - {english}"
	print(txt)

txtb = txt.encode("utf-8","replace")

with open("txt.txt","wb") as f:
	f.write(txtb)
	f.close()
