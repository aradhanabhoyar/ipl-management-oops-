### IPL Management System ###
class Player:
    def __init__(self,jn,nm,r,w,tn):
        self.__jerseyno = jn
        self.__name = nm
        self.__run = r
        self.__wicket = w
        self.__teamname = tn

    # Getter method ##
    def get_jerseyno(self):
        return self.__jerseyno
    def get_name(self):
        return self.__name
    def get_run(self):
        return self.__run
    def get_wicket(self):
        return self.__wicket
    def get_teamname(self):
        return self.__teamname
    
    ## Setter method ##
    def set_jerseyno(self,jerseyno):
        self.__jerseyno = jerseyno
    def set_name(self,name):
        self.__name = name
    def set_run(self,run):
        self.__run = run
    def set_wicket(self,wicket):
        self.__wicket = wicket
    def set__teamname(self,teamname):
        self.__teamname = teamname
    
    def display_info(self):
        print(f"\nJersey no: {self.__jerseyno}")
        print(f"Name : {self.__name}")
        print(f"Runs : {self.__run}")
        print(f"Wickets : {self.__wicket}")
        print(f"Team Name : {self.__teamname}") 
    
Team1 =[]
P1 = Player(45,"Rohit Sharma",540,0,"Mumbai Indians")
Team1.append(P1)
P2 = Player(63,"Suryakumar Yadav",610,0,"Mumbai Indians")
Team1.append(P2)
P3 = Player(77,"Ishan Kishan",440,0,"Mumbai Indians")
Team1.append(P3)
P4 = Player(95,"Tilak Varma",360,0,"Mumbai Indians")
Team1.append(P4)
P5 = Player(11,"Hardik Pandya",310,9,"Mumbai Indians")
Team1.append(P5)
P6 = Player(99,"Gerald Coetzee",15,18,"Mumbai Indians")
Team1.append(P6)
P7 = Player(25,"Piyush Chawla",10,17,"Mumbai Indians")
Team1.append(P7)
P8 = Player(3,"Nehal Wadhere",190,0,"Mumbai Indians")
Team1.append(P8)
P9 = Player(93,"Jasprit Bumrah",20,21,"Mumbai Indians")
Team1.append(P9)
P10 = Player(24,"Tim David",220,0,"Mumbai Indians")
Team1.append(P10)
P11 = Player(17,"Srjun Tendulkar",12,4,"Mumbai Indians")
Team1.append(P11)


Team2 = []
R1 = Player(18,"Virat Kohli",741,0,"RBC")
Team2.append(R1)
R2 = Player(97,"Faf du Plessis",600,0,"RBC")
Team2.append(R2)
R3 = Player(88,"Rajat Patidar",310,0,"RBC")
Team2.append(R3)
R4 = Player(25,"Mohammed Siraj",12,19,"RBC")
Team2.append(R4)
R5 = Player(55,"Mayank Dagar",20,5,"RBC")
Team2.append(R5)
R6 = Player(33,"Glenn Maxwell",350,0,"RBC")
Team2.append(R6)
R7 = Player(88,"Rajat Patidar",310,2,"RBC")
Team2.append(R7)
R8 = Player(50,"Will Jacks",280,3,"RBC")
Team2.append(R8)
R9 = Player(38,"Josh Hazlewood",0,22,"RBC")
Team2.append(R9)
R10 = Player(15,"Bhuvneshwar Kumar",0,6,"RBC")
Team2.append(R10)
R11 = Player(103,"Dinesh Karthik",400,0,"RBC") 
Team2.append(R11)


Team3 = []
C1 = Player(7,"MS Dhoni",180,0,"CSK")
Team3.append(C1)
C2 = Player(31,"Shivam Dube",450,5,"CSK")
Team3.append(C2)
C3 = Player(66,"MS Dhoni",196,0,"CSK")
Team3.append(C3)
C4 = Player(5,"Ravindra Jadega",250,14,"CSK")
Team3.append(C4)
C5 = Player(18,"Devon Conway",156,0,"CSK")
Team3.append(C5)
C6 = Player(9,"Ruturaj Gaikwad",580,0,"CSK")
Team3.append(C6)
C7 = Player(19,"Ayush Mhatre",240,0,"CSK")
Team3.append(C7)
C8 = Player(14,"Sam Curran",114,1,"CSK")
Team3.append(C8)
C9 = Player(12,"Noor Ahmad",7,24,"CSK")
Team3.append(C9)
C10 = Player(16,"Khaleel Ahmed",2,15,"CSK")
Team3.append(C10)
C11 = Player(13,"Matheesha Pathirana",0,13,"CSK")
Team3.append(C11)


all_players = Team1 + Team2 + Team3
## Top Bowler ##
top_bowler = all_players[0]
for player in all_players:
    if player.get_wicket() > top_bowler.get_wicket():
        top_bowler = player

## Top Batsman ##
top_batsman = all_players[0]
for player in all_players:
    if player.get_run() > top_batsman.get_run():
        top_batsman = player

## All Rounder ##
all_rounders = []
for player in all_players:
    if player.get_run() > 0 and player.get_wicket() > 0:
        all_rounders.append(player)

#Search and display player info#
search_name = input("\nEnter player name to search : ")
found = False
for player in all_players:
    if player.get_name().lower() == search_name.lower():
        print("\nPlayer found:")
        player.display_info()
        found = True
        break
if not found:
    print("Player not found in the team.")

print("Top Bolwer")
print(f"{top_bowler.get_name()}({top_bowler.get_teamname()})- Wickets : {top_bowler.get_wicket()}")
print("Top Batsman")
print(f"{top_batsman.get_name()}({top_batsman.get_teamname()}) - Runs : {top_batsman.get_run()}")
print("All Rounder")
for player in all_rounders:
    player.display_info()
    
