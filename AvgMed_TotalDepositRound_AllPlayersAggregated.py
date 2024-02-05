import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Gruppieren der Daten nach Runden-ID und Berechnung des Gesamteinsatzes pro Runde
total_bet_per_round = eth_only_bets.groupby('roundid')['deposit_usd'].sum()

# Berechnung des durchschnittlichen und medianen Gesamteinsatzes pro Runde
average_total_bet_per_round = total_bet_per_round.mean()
median_total_bet_per_round = total_bet_per_round.median()

# Ausgabe der durchschnittlichen und medianen Gesamteinsatzhöhe pro Runde
print(f"Durchschnittlicher Gesamteinsatz pro Runde: {average_total_bet_per_round}")
print(f"Median des Gesamteinsatzes pro Runde: {median_total_bet_per_round}")
