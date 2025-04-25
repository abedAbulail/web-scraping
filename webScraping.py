import requests
from bs4 import BeautifulSoup
from googlesearch import search as s
import csv

search = input("Enter the search query: ")
result = s(search,2)
url = ""
for i in result:
    url = i

    print(url)

print(url)
# date=input("Enter the date: MM/DD/YYYY ")

# page = requests.get(
# f"https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa?date={date}#matchesclipPrev"
# )


# def main(page):
#     src=page.content
#     supe=BeautifulSoup(src,'lxml')
#     matches=[]
#     champeans = supe.find_all("div", {"class": "matchCard"})

#     def get_match_info(champean):
#         title=champean.contents[1].find('h2').text.strip()
#         all_matches = champean.contents[3].find_all('div', {'class': 'liItem'})
#         number_of_matches=len(all_matches)
#         for i in range(number_of_matches):
#             match = all_matches[i]
#             teamA = match.find('div', {'class': 'teamA'}).text.strip()
#             teamB = match.find("div", {"class": "teamB"}).text.strip()
#             result=match.find("div", {"class": "MResult"}).find_all('span',{'class':'score'})

#             score = f"{result[1].text.strip()} - {result[0].text.strip()}"
#             time=match.find("div", {"class": "MResult"}).find('span',{'class':'time'}).text
#             matches.append({'title':title,'teamA':teamA,'teamB':teamB,'score':score,'time':time})
#         print(matches)

#     for i in range(len(champeans)):
#         get_match_info(champeans[i])
#     keys = matches[0].keys()
#     with open("matches.csv", "w", encoding="utf-8-sig") as output_file:
#         dict_writer = csv.DictWriter(output_file, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(matches)
#         print("File has been created successfully")
# main(page)
