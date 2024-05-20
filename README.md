# Pickle158's Sports API Project
This is an API that will get the current Denver Nuggets game score using python and an API and print it on a mechanical 7 segment display (For Raspberry Pi).
The code for this was made in python, and is completely open source.  If you have any suggestions to make this better, it would be appreciated.  It is still a working progress, but its getting there.  

# Which API file should I use?
The main.py file will run on any os with python, and it will get the score of the game and print it out in the terminal.  However, if you want it to do more, the MechForPi file is made to run on a Raspberry Pi (Wiring shown below), and will print the score on mechanical 7 segment displays (get ur own).

# How to get the API
I got my API from sportsdata.io  They aren't all that helpful, so it took a while to get this to work.  All you need is to get your free forever API trial, and obtain your API key.  Then, just put your key into the API key field of my code and it should work.

Thanks to POSTMAN API for help with testing and visualizing the results in a clean format with a clear editor, wouldnt have been able to do this without them.


# Team ID's  
If you want to get the score of other teams, you must change the TEAM_ID field to your team's ID.  The Available team ID's are listed below.
- Washington  Wizards  Team ID: 1
- Charlotte  Hornets  Team ID: 2
- Atlanta  Hawks  Team ID: 3
- Miami  Heat  Team ID: 4
- Orlando  Magic  Team ID: 5
- New York  Knicks  Team ID: 6
- Philadelphia  76ers  Team ID: 7
- Brooklyn  Nets  Team ID: 8
- Boston  Celtics  Team ID: 9
- Toronto  Raptors  Team ID: 10
- Chicago  Bulls  Team ID: 11
- Cleveland  Cavaliers  Team ID: 12
- Indiana  Pacers  Team ID: 13
- Detroit  Pistons  Team ID: 14
- Milwaukee  Bucks  Team ID: 15
- Minnesota  Timberwolves  Team ID: 16
- Utah  Jazz  Team ID: 17
- Oklahoma City  Thunder  Team ID: 18
- Portland  Trail Blazers  Team ID: 19
- Denver  Nuggets  Team ID: 20
- Memphis  Grizzlies  Team ID: 21
- Houston  Rockets  Team ID: 22
- New Orleans  Pelicans  Team ID: 23
- San Antonio  Spurs  Team ID: 24
- Dallas  Mavericks  Team ID: 25
- Golden State  Warriors  Team ID: 26
- Los Angeles  Lakers  Team ID: 27
- Los Angeles  Clippers  Team ID: 28
- Phoenix  Suns  Team ID: 29
- Sacramento  Kings  Team ID: 30
