# launcherZ
	Isaac Perks   
	2/9/23   
 
 
# Description
A Python based Front-End GUI replacement launcher for Monster Hunter Frontier.
Another developer reverse engineered the binaries that handle the main game launcher which can be found here:   
https://github.com/rockisch/mhf-iel
 
This project extends on that framework and looks to create a GUI that provides new additions and QOL changes compared
to the current launcher.   
For example I will be looking to implement;   
- A server list that is adjustable and editable   
- Servers list objects would contain:   
	- Icons/Images   
	- Descriptions/Details   
	- Uptime   
	- Active or registered players   
- Each server has a templated page that contains:   
	- Banners/Logos/Wallpapers   
	- RSS Feed for posts and updates   
	- More in depth install instructions or details   

	Project utilises PySide6 to take advantage of the QT6 framework. In this particular case QT Designer and QT
	Creater were not used.

### Build
	OS: Windows   
	IDE: Visual Studio Community 2022   
	Language: Python 3.9   
	Dependencies(Requirements tx will be added):   
	PySide6   
	python-nmap   
	BeautifulSoup   

### Attributes
	https://github.com/rockisch/mhf-iel