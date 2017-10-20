def find_team_mate(players, team_mates, n):
    """
    players: persons who needs team, list class gamer
    team_mates: list of classes gamer possible teammates
    n: number of team mates
    """
    for i in range(len(team_mates)):
        team_mates[i]=team_mates[i].R
        
    R=sum(i.R for i in players)
    def delta(a): return a-R
    team_mates=sorted(list(map(delta, team_mates)))
    i=0
    while team_mates[i]<0: i+=1
    return team_mates[i-n//2:i+n//2+n%2]