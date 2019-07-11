from bs4 import BeautifulSoup
import requests
handle = input('Input your account name on Twitter: ')
ctr = int(input('Input number of tweets to scrape: '))
res=requests.get('https://twitter.com/'+ handle)
bs=BeautifulSoup(res.content,'lxml')
all_tweets = bs.find_all('div',{'class':'tweet'})
if all_tweets:
  for tweet in all_tweets[:ctr]:
    context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
    content = tweet.find('div',{'class':'content'})
    message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
    footer = content.find('div',{'class':'stream-item-footer'})
    stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
    if context:
      print(context)
    print(message)
    print(stat)
    print()
else:
    print("List is empty/account name not found.")
