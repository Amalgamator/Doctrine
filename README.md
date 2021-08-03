# Doctrine
![Status](https://img.shields.io/badge/Status-In_Development-blue?style=flat-square) ![Lines of code](https://img.shields.io/tokei/lines/github/Amalgamator/Doctrine?style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors/Amalgamator/Doctrine?style=flat-square) ![GitHub last commit](https://img.shields.io/github/last-commit/Amalgamator/Doctrine?style=flat-square) 

## About
This project aims to build a fully fleshed out Discord bot for the Age of Empires II community.

## Planned features
```
d!tech ["tech"] : gives you in-depth information about a technology ["tech"] and ANY object it applies to
d!unit ["unit"] : gives you in-depth information about a unit ["unit"], best/worst counters, techs that apply to it
d!hasunit ["unit"] : shows all civs that have [unit]
d!hastech ["tech"] : shows all civs that have [tech]
d!cbonus [civ] : shows all civ bonuses and unique units / techs for [civ].
d!randmap [label] ([label] .... ) : selects a random map from the standard map pool, [label] constrains the pool by types. 
                                    [label] can be (in no particular order): 
                                        open/restricted (how wallable & bottlenecked the map is), 
                                        land/hybrid/water (water: fully disconnected opponents by water), 
                                        tc/-tc (false/true nomadic types), 
                                        elev/-elev (true/false elevation), 
                                        ponds/-ponds (true/false ponds in map, doesn't necessarily mean fish!)
d!randciv ["label"] (["label"] .... ) : selects a random civ from the civ pool, 
                                    ["label"] can be a unit or tech (use "" or '' to avoid whitespace issues)
d!elo [playername/steamnumber] : gives you the 1v1 RM elo and TG RM elo of a player
d!welo [playername/steamnumber] : gives a weighted average of a player's 1v1 RM / 1v1 DM / TG RM / TG DM and custom games.
d!morelo [playername/steamnumber] : Shows an in-depth analysis of a player's ratings in all gametypes.
                                     (1) Preferred maps, preferred civs. (find preferences)
                                     (2) A map*civ matrix of winrates. (find weaknesses)
                                     (3) Smurfness estimator & Rating history.
                                     (4) Recordings link & Average game time.
d!hint : gives a random (obscure) fact about the game.
d!map ["mapname"] : tells you everything you need to know about a map.
                    - The spawning distances of starting resources
                    - A total average % breakdown of terrain by type (land, non-buildable land, water, shallow, forest, ...)
                    - A total resource breakdown by type and placement 
                                   (start/neutral) 
                                   (deepfish, fish, shorefish, hunt, herd, prey, trees, berries, gold, stone)
d!bo [civ] ["unit"*n,] ["building"*n,] ["tech,tech"] ( [teamciv,teamciv,teamciv] ) ( ["map"] ) ( ["name"] ) : 
                                   generates a time-optimised build order based 
                                   on an idealised simulation.
                                   ["map"] is optional, however, if no map is given, simulator will assume Arabia resources.
                                   ["name"] is required to save to web and share (2,3). alphanumeric, hyphen, dot and spaces only. 80chars.
                                   ["unit"*n] --> "unit name" times n, n the amount you want.
                                   the same for building. ["tech"] or a list of techs can be included.
                                   To add multiple unit types, separate them by comma only.
                                   [teamciv] applies the teambonus from that/those civ/civs if applicable
                     - Will respond with:
                             (1) A build order overlay txt file (for use in game)
                             (2) A link to the online version (web UI to share/edit/save and see more stats)
                             (3) BO: "Name" in MM:SS, (sharecode: ###########).
d!bo [code] : shows the response tied to that code
d!bo list : gives a list of the most popular BOs as logged by d!bo usage
d!bo web : responds with the link to the web version

/// Additional features to work on, when done with the abovementioned features ///
d!twitch : twitch integration, will check functionality later
d!twitch list : list of aoe2 twitch streamers
d!tools : list of aoe2 tools
d!servers : list of important aoe2 discords
d!sustain [civ] ["unit"*n] (["unit"*n]) : shows you how much vils on each res you need for sustained production
                                          For example, [franks] [knight*10] [monk] --> 60f, 100g.
d!duel ["unit"] ["unit"] : simulates a number of 1v1 fights between two opposing player-controlled units, to see who comes out on top.
d!instahit ["unit"] ["unit"] ["tech"] ["tech"] : how many units, with perfect micro, does it take to insta-kill an opponent unit. 
                                                 In other words, how many units in a control group.

/// OTHER ///
d!help : pretty much this overview here, but prettier, more clear, useful and edited.
d!doctrine : about Doctrine, a link to our discord, etc
d!yt : links to our YT channel
d!activity : shows a table for AoE2DE activity last 4 hours, 12 hours, day, week, month (steamapi, aoe2.net api) 
d!members : number of discord servers using Doctrine bot
d!rumpel : "What is a Rumpel?" -- Debbie, Wife of the Snek
d!thanks : a list of community members that have inspired or helped me.
d!donate : responds with a patreon link or something, to support development, server costs and Dev coffee/tea
```

## Dev tools needed

### Install Mongodb 
Get MongoDB Community Server version 3.6.x for your platform, available at https://www.mongodb.com/try/download/community. 
Don't forget to add the executables to the system PATH variables.

### Download .csv files, import to mongodb

https://docs.google.com/spreadsheets/d/1MTnVLHNx0z_y_Zw2JoF4s0li_N9JtqDY0Dlbxl4aDww/edit#gid=1840039594
From the link, download all the sheets that don't start with an __ and are unlocked. (buildings, techs, units, etc)
From the terminal, change to the directory where the downloaded files are and input following commands to import the data:

```
mongoimport --db doctrine --collection techtable --type csv --headerline --file '.\AoE2 DE - Data - TechTable.csv'
mongoimport --db doctrine --collection techs --type csv --headerline --file '.\AoE2 DE - Data - Techs.csv'
mongoimport --db doctrine --collection unittable --type csv --headerline --file '.\AoE2 DE - Data - UnitTable.csv'
mongoimport --db doctrine --collection units --type csv --headerline --file '.\AoE2 DE - Data - Units.csv'
mongoimport --db doctrine --collection buildtable --type csv --headerline --file '.\AoE2 DE - Data - BuildTable.csv'
mongoimport --db doctrine --collection buildings --type csv --headerline --file '.\AoE2 DE - Data - Buildings.csv'
```
And from: https://docs.google.com/spreadsheets/d/1ItIrBZwrF1KsmvlIiNayALcGv0A2xHRWBAYb3OaHmBw/edit?usp=sharing

```
mongoimport --db doctrine --collection mappool --type csv --headerline --file '.\Maps - Sheet1.csv'
```

### Get python >=3.7.0 and dependencies
Clone this repo, change directories to where `bot.py` exists and run 
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install pymongo
pip install .
```
