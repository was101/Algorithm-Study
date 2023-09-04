def solution(players, callings):
    ranks = {}
    for idx, player in enumerate(players):
        ranks[player] = idx
    for player in callings:
        rank = ranks[player]
        ranks[player] -= 1
        ranks[players[rank - 1]] += 1
        players[rank] = players[rank-1]
        players[rank-1] = player
    return players