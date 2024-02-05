import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Identifizieren der Gewinne und Verluste
eth_only_bets['result'] = eth_only_bets.apply(lambda row: row['deposit_usd'] if row['is_winner'] == 1 else -row['deposit_usd'], axis=1)

# Berechnen des Gesamtgewinns und -verlustes pro Spieler
total_result_per_player = eth_only_bets.groupby('depositor')['result'].sum()

# Durchschnittlicher und medianer Gewinn und Verlust über alle Spieler
average_result = total_result_per_player.mean()
median_result = total_result_per_player.median()

# Höchster und niedrigster Gewinn/Verlust für einen Spieler
max_result = total_result_per_player.max()
min_result = total_result_per_player.min()

# Ausgabe der Ergebnisse
print(f"Durchschnittlicher Gewinn/Verlust pro Spieler: {average_result}")
print(f"Medianer Gewinn/Verlust pro Spieler: {median_result}")
print(f"Höchster Gewinn/Verlust für einen Spieler: {max_result}")
print(f"Niedrigster Gewinn/Verlust für einen Spieler: {min_result}")
