import pyshorteners

def shortlink(url):
    S=pyshorteners.Shortener()
    short_url=S.tinyurl.short(url)
    print(f"The Shorten URL of given Url = {short_url}")
    
URL=input("Enter the URl:- ")
shortlink(URL)