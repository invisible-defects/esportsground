class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.R=sum(i.R for i in members)/len(members)


def make_corp(inp, tab=[]):
    if inp==1: 
        tab.append([None])
        return tab
    elif inp%2==0:
        tab.append([[None, None] for i in range(inp//2)])
        inp//=2
        return make_corp(inp, tab)
    else: 
        if (inp%4)%2==0: 
            tab.append([None])
            inp-=1
            tab[-1].append([[None, None] for i in range(inp//2)])
            inp//=2
            return make_corp(inp+1, tab)
        else:
            tab.append([[None, None] for i in range(inp//2)])
            tab[-1].append([None])
            inp//=2
            return make_corp(inp+1, tab)


class placeholderForOlympicSystem:
    def __init__(self, teams):
        self.teams=teams
        self.table=make_corp(len(teams))
        self.names=[i.name for i in teams]
        self.name_table=make_corp(len(teams))
        for i in range(len(self.names)):
            self.name_table[0][i//2][i%2]=self.names[i]


class placeholderForCirculSystem:
    def __init__(self, teams):
        table=[[None for j in range(len(teams)+1)] for i in range(len(teams)+1)]
        for i in range(len(teams)+1):
            table[i][0]=teams[i].name
            for j in range(len(teams)+1):
                if i==0: table[0][j]=teams[j].name
                if i==j: table[i][j]="-"
        self.table=table