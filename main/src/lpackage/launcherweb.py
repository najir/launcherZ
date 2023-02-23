######################################
# Web Module for all web requests and interactions
######################################
from wsgiref import headers
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import nmap, socket

class webControllerClass():



######################################
# Takes the URL given and returns null or data from the RSS Feed
# A dict of dicts contains up to the last 3 posts in feed
######################################
    def pullRss(self, url):
        int = 0
        urlData = urllib.request.urlopen(urllib.request.Request(url, method='GET', headers={'User-Agent' : 'Mozilla/5.0'})).read().decode('utf8')
        parse = BeautifulSoup(urlData, 'xml')
        xmlData = parse.find_all('item', limit=3)
        rssDict = {}

        for entry in xmlData:
            rssDict[int] = {
                "NAME" : entry.title.text,
                "DESCRIPTION" : entry.description.text,
                "LINK" : entry.link.text
                }
            int += 1

        return rssDict
        

######################################
# Takes URL and returns img at link
######################################
    def pullImage(self, url):
        textUrl = urllib.parse.quote_plus(url)
        w = open("./rsc/img/" + textUrl, 'wb')
        w.write(urllib.request.urlopen(url).read())
        w.close()

######################################
# Sends a ping to the server and returns T/F
######################################
# For build complexity sake I will be redoing this to only use the socket module :/
    def serverPing(self, serverIP, serverPort):
        returnBool = 0
        scanner = nmap.PortScanner()
        status = scanner.scan(serverIP, serverPort)
        status = status['scan'][serverIP]['tcp'][int(serverPort)]['state']
        if status != 'down':                # This will need to be changed so it actually returns properly
            returnBool = 1
        return returnBool