
from math import log, e, sqrt


def E(R, *args):
    """
    R: current player's rating
    args: current rating of other players
    
    returns: probability of win
    """
    return 1.0/(1+10**((R-sum(args)/float(len(args)))/400.))



def K(R):
    """
    R: current player's rating 
    
    returns: player's koefficent
    """
    if R>=2500: return 30-2*log(2500)
    else: return 30-2*log(R)



def R_new(R, K, S, E):
    """
    R: current player's rating
    K: koefficent
    S: match result: 1 if win, 0.5 if draw, 0 if lose
    E: predicted probability of win
    
    returns: new value of rating
    """
    R_n=R+K*(S-E)
    return R_n



def set_R(*args):
    (total_kills, total_deaths, total_time_played, total_wins, total_kills_headshot, total_shots_hit, total_shots_fired, total_mvps, total_matches_played)=args
    total_time_played/=3600.0
    R=total_kills*log(total_time_played)*total_wins*total_matches_played*total_kills_headshot*total_mvps*total_shots_hit/(total_deaths*(total_deaths+total_kills)*total_shots_fired*total_shots_fired)
    T=R*25/3
    return T if T<=2500 else 2500


def set_R(total_kills, total_deaths, total_time_played, total_wins, total_kills_headshot, total_shots_hit, total_shots_fired, total_mvps, total_matches_played):
    total_time_played/=3600.0
    R=total_kills*log(total_time_played)*total_wins*total_matches_played*total_kills_headshot*total_mvps*total_shots_hit/(total_deaths*(total_deaths+total_kills)*total_shots_fired*total_shots_fired)
    T=R*25/3
    return T if T<=2500 else 2500