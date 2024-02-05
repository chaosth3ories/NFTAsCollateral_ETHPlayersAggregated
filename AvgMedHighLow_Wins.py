import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Berechnen des Gesamteinsatzes und des Einsatze der Gewinner pro Runde
total_bet_per_round = eth_only_bets.groupby('roundid')['deposit_usd'].sum()
winner_bet_per_round = eth_only_bets[eth_only_bets['is_winner'] == 1].groupby('roundid')['deposit_usd'].sum()

# Berechnung des Gewinns pro Runde
profit_per_round = total_bet_per_round - winner_bet_per_round

# Durchschnittlicher und medianer Gewinn pro Runde
average_profit = profit_per_round.mean()
median_profit = profit_per_round.median()

# Höchster und niedrigster Gewinn in einer Runde
max_profit = profit_per_round.max()
min_profit = profit_per_round.min()

# Ausgabe der Ergebnisse
print(f"Durchschnittlicher Gewinn pro Runde: {average_profit}")
print(f"Medianer Gewinn pro Runde: {median_profit}")
print(f"Höchster Gewinn in einer Runde: {max_profit}")
print(f"Niedrigster Gewinn in einer Runde: {min_profit}")
