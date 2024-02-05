import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Zählen, wie oft gewonnen wurde
total_wins = eth_only_bets['is_winner'].sum()

# Zählen, wie oft verloren wurde
# Annahme: Ein Eintrag in der Datenbank entspricht einem Spiel, also ist die Anzahl der Verluste die Anzahl der Spiele minus die Anzahl der Gewinne
total_losses = len(eth_only_bets) - total_wins

# Ausgabe der Ergebnisse
print(f"Anzahl der Gewinne: {total_wins}")
print(f"Anzahl der Verluste: {total_losses}")
