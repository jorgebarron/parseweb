"""
input: - number indicating which subpage we are parsing
output: - prints all items in the page.
          (release date is comment out but could be printed)
"""
from bs4 import BeautifulSoup
import urllib.request

def ParseWeb(numberPages):

    if numberPages == 1:
        webPage = "http://sceper.ws/"
    else:
# address format from the 2nd page: http://sceper.ws/page/2
        webPage = "http://sceper.ws/page/%d" % numberPages
        
    response = urllib.request.urlopen(webPage)
    html = response.read()
    soup = BeautifulSoup(html)

    # relevant information to extract is in the class "entry clearfix"
    
    g_data = soup.find_all("div",{"class":"entry clearfix"})

    # and the third element of the dictionary g_data 

    for item in g_data:
        item = item.contents[3].text
        fName = item.split('\n')[4]
        #print (fName.split("Release Name: ",1)[1])
        print (fName.split("Release Name: ",1)[1])
        fDate = item.split('\n')[5]
        ### print Release Date
        #print (fDate)
    print ('')

if __name__ == '__name__':
    ParseWeb()
