# Doctrine
![Status](https://img.shields.io/badge/Status-In_Development-blue?style=flat-square) ![Lines of code](https://img.shields.io/tokei/lines/github/Amalgamator/Doctrine?style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors/Amalgamator/Doctrine?style=flat-square) ![GitHub last commit](https://img.shields.io/github/last-commit/Amalgamator/Doctrine?style=flat-square) 


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

### Get python >=3.7.0 and dependencies
Clone this repo, change directories to where `bot.py` exists and run 
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install pymongo
pip install .
```

### Ask for the .env file
