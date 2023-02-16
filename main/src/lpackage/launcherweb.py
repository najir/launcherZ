######################################
# Web Module for all web requests and interactions
######################################
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import nmap, socket

class webControllerClass():



######################################
# Takes the URL given and returns null or data from the RSS Feed
# A dict of dicts contains up to the last 3 posts in feed
######################################
    def pullRss(self, url):
        int = 0
        urlData = urllib.request.Request(url)
        parse = BeautifulSoup(urlData.content, 'xml')
        xmlData = parse.find_all('entry', limit=3)
        rssDict = {}

        for entry in xmlData:
            rssDict[int] = {
                "NAME" : entry.title.text,
                "DESCRIPTION" : entry.summary.text,
                "LINK" : entry.link['href']
                }
            int += 1

        return rssDict
        

######################################
# Takes URL and returns img at link
######################################
    def pullImage(self, url):
        imgData = urllib.request.urlopen(url).read()
        return imgData

######################################
# Sends a ping to the server and returns T/F
######################################
    def serverPing(self, serverIP):
        returnBool = 0
        ipAddress = input(serverIP)
        scanner = nmap.PortScanner()
        host = socket.gethostbyname(ipAddress)
        scanner.host(host, '1', '-v')
        if scanner[host].state():                # This will need to be changed so it actually returns properly
            returnBool = 1
        return returnBool