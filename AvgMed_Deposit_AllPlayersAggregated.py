import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Berechnung des durchschnittlichen und medianen Einsatzes aller Spieler
average_bet_all_players = eth_only_bets['deposit_usd'].mean()
median_bet_all_players = eth_only_bets['deposit_usd'].median()

# Ausgabe der durchschnittlichen und medianen Einsatzhöhe aller Spieler
print(f"Durchschnittlicher Einsatz aller Spieler: {average_bet_all_players}")
print(f"Median des Einsatzes aller Spieler: {median_bet_all_players}")
