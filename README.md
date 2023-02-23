# launcherZ
	Isaac Perks   
	2/9/23   
 
 
# Description
A Python based Front-End GUI replacement launcher for Monster Hunter Frontier.   
Another developer reverse engineered the binaries that handle the main game launcher which can be found here:   
https://github.com/rockisch/mhf-iel   
 
This project extends on that framework and looks to create a GUI that provides new additions and QOL changes compared
to the current launcher.  
Currently I have implement a variety of features to benefit players and server owners   
- Add custom servers to the server list
- Server IP, details, Logo/Icon, and name are viewable from the list
- Server uptimes are checked on serverlist load
- Servers can provide a link to install instructions for new users
- Server Banners, logos are show on server pages and can be changed dynamically
- Servers can provide an RSS feed to be shown on their server page

To be Implemented:
- Password encrytion
- Connect launcher to ieless
- server specific calls(User info from databses for example)

- Project utilises PySide6 to take advantage of the QT6 framework. In this particular case QT Designer and QT
Creater were not used.
- urllib to pull photos from links
- beautiful soup to pull rss feed and parse xml
- Servers are stored and handeled in a sqlite3 database



### Build
	OS: Windows   
	IDE: Visual Studio Community 2022   
	Language: Python 3.9   
	Dependencies(Requirements tx will be added):   
	PySide6   
	python-nmap   
	BeautifulSoup   
	lxml   

### Attributes
	https://github.com/rockisch/mhf-iel
	Gajah Mada - Flaticon
	freepik - Flaticon