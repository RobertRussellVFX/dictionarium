from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup
import urllib.request



class English:
   

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://archives.nd.edu/cgi-bin/wordz.pl?english='
        

    def key_words_search_words(self, user_message):
      words = user_message.split()[1:]
      keywords = '+'.join(words)
      search_words = ' '.join(words)
      return keywords, search_words
        

    def search(self, keywords):
        response = urllib.request.urlopen(self.url+keywords)
        content = response.read()
        soup = BeautifulSoup(content, 'lxml')
        result_links = soup.find("pre").find(text=True)
        return result_links
        


    def send_link(self, result_links, search_words):
        if search_words in result_links:
            print(result_links)
            print(search_words)
        return result_links, search_words


   # def send_link(self, result_links, search_words): 
  #    send_link = set()
   #   for link in result_links:
   #       text = link.lower()
   #       if search_words in text:  
  #          send_link.add(link.get('pre'))
  #          print(send_link)
  #        return send_link

  