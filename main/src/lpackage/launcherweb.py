######################################
# Web Module for all web requests and interactions
######################################
import urllib.request, urllib.error
import nmap, socket

class webControllerClass():



######################################
# Takes the URL given and returns null or data from the RSS Feed
# Ideally this would return the last 3 blog posts at the feed url
######################################
    def pullRss(url):
        return

######################################
# Takes URL and returns img at link
######################################
    def pullImage(url):
        imgData = urllib.request.urlopen(url).read()
        return imgData

######################################
# Sends a ping to the server and returns T/F
######################################
    def serverPing(serverIP):
        ipAddress = input(serverIP)
        scanner = nmap.PortScanner()
        host = socket.gethostbyname(ipAddress)
        scanner.host(host, '1', '-v')
        return scanner[host].state()