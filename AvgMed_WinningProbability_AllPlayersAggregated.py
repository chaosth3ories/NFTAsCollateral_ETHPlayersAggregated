import pandas as pd

# Einlesen der Daten aus der CSV-Datei
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Berechnung des Gesamteinsatzes pro Runde in USD
total_bets_per_round = eth_only_bets.groupby('roundid')['deposit_usd'].sum()

# Zuordnung des Gesamteinsatzes jeder Runde zu den individuellen Wetten
eth_only_bets['total_bet_round'] = eth_only_bets['roundid'].map(total_bets_per_round)

# Berechnung der individuellen Gewinnwahrscheinlichkeit
eth_only_bets['win_probability'] = eth_only_bets['deposit_usd'] / eth_only_bets['total_bet_round']

# Berechnung der durchschnittlichen und medianen Gewinnwahrscheinlichkeit
average_probability = eth_only_bets['win_probability'].mean()
median_probability = eth_only_bets['win_probability'].median()

# Ausgabe der Wahrscheinlichkeiten
print(f"Average Winning Probability: {average_probability}")
print(f"Median Winning Probability: {median_probability}")

