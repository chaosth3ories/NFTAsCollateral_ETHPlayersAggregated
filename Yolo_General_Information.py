import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# 1. Gesamtanzahl aller Spiele (Runden)
total_games = eth_only_bets['roundid'].nunique()

# 2. Gesamtanzahl der einzelnen Spieler
total_players = eth_only_bets['depositor'].nunique()

# 3. Anzahl der abgebrochenen Runden
aborted_rounds = eth_only_bets['is_too_little_players'].sum()

# 4. Anzahl der unclaimed Gewinne
unclaimed_wins = eth_only_bets['is_unclaimed'].sum()

# 5. Gesamtvolumen in ETH und USD
total_volume_eth = eth_only_bets['deposit_eth'].sum()
total_volume_usd = eth_only_bets['deposit_usd'].sum()

# Ausgabe der Ergebnisse
print(f"Gesamtanzahl aller Spiele (Runden): {total_games}")
print(f"Gesamtanzahl der einzelnen Spieler: {total_players}")
print(f"Anzahl der abgebrochenen Runden: {aborted_rounds}")
print(f"Anzahl der unclaimed Gewinne: {unclaimed_wins}")
print(f"Gesamtvolumen in ETH: {total_volume_eth}")
print(f"Gesamtvolumen in USD: {total_volume_usd}")
