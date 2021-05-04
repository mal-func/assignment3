class cric:

    def __init__(self,name,no_of_in,runs,wickets,not_outs,catches):
        self.name=name
        self.no_of_in=no_of_in
        self.runs=runs
        self.wickets=wickets
        self.not_outs=not_outs
        self.player="-"
        self.catches=catches
  
    def analyze(self):
        self.bat_avg=float(self.runs)/self.no_of_in
        if self.no_of_in >= 50:
            if self.bat_avg>35:
                if self.wickets>49:
                    self.player="All Rounder"
                else:
                    self.player="Batsman"
                    
            if self.wickets>49:
                if self.bat_avg>35:
                    self.player="All Rounder"
                else:
                    self.player="Bowler"

    def display(self):
        print(f'Name of the player: {self.name}\nNo. of Innings: {self.no_of_in}\nNo. of runs: {self.runs}\nNo. of wickets: {self.wickets}\nNo. of catches: {self.catches}\n{self.player}')

      
ls=[]
a="y"
while a=="y":
    name=input("Enter player's name: ")
    no_of_in=int(input("Enter number of innings played: "))
    runs=int(input("Enter the number of runs scored: "))
    wickets=int(input("Enter the number of wickets taken: "))
    not_outs=int(input("Enter the number of not out innings: "))
    catches=int(input("Enter the number of catches taken: "))
    ob=cric(name,no_of_in,runs,wickets,not_outs,catches)
    ob.analyze()
    ls.append(ob)
    a=input("Do you wish to continue(y/n)? ")
    a=a.lower()

for x in ls:
    x.display()
