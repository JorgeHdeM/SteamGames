# SteamGames
## Description
This project compares your owned games with friends' ones in order to decide faster which game to play  
If you want to add different countries to the output file, modify: ***Modules/countries.py***  

Generated files in \Output:  
- Games_PlayedTime - CSV file containing GameName and PlayedTime
- Friends_Price - CSV file containing GameName, GameID, FriendsOwnedGame, PriceMX, PriceUS
## Pre-requisites
1. Install Python
2. Install pandas library
```bash
pip install pandas
```
## Installation
```bash
gitclone https://github.com/JorgeHdeM/SteamGames.git
```

## Setup Steam accounts
1. Login in this [Steam link](https://steamcommunity.com/login/home/?goto=%2Fdev%2Fapikey)  
![alt text](https://github.com/JorgeHdeM/SteamGames/blob/develop/src/assets/SteamKey.png)
  
2. In the **domain** field, type your username
3. SteamApp > Profile > Edit profile > Copy last numbers as marked  
![alt text](https://github.com/JorgeHdeM/SteamGames/blob/develop/src/assets/SteamProfile2.png)
  
4. Copy **ApiKey**, **UserID** and **UserName** to the *users.csv* file
    - You can populate same ApiKey for all users
    - **Highly recommended to use personal API_KEY for each user to avoid call errors**

## Output
After running **main.py** and a little formatting:
1. Games_PlayedTime  
![alt text](https://github.com/JorgeHdeM/SteamGames/blob/develop/src/assets/Games_PlayedTime_Demo.png)

2. Friends_Price
    - SHARED_FRIENDS refers to the friends owning the specific game
![alt text](https://github.com/JorgeHdeM/SteamGames/blob/develop/src/assets/Games_Price_Demo.png)

### IMPORTANT
FREE_GAMES can be false positives since the game's name is different, for example:  
API game name: *Grand Theft Auto V*  
Real Steam name: *Grand Theft Auto V: Premium Edition*

## License
[MIT](https://choosealicense.com/licenses/mit/)
