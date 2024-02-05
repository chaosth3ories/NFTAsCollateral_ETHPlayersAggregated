import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Filtern der Daten auf Einträge mit einem ENS-Namen
players_with_ens = eth_only_bets[~eth_only_bets['ens_name'].isna() & (eth_only_bets['ens_name'] != '')]

# Zählen der einzigartigen Spieler mit einem ENS-Namen
unique_players_with_ens = players_with_ens['depositor'].nunique()

# Ausgabe der Anzahl
print(f"Amount of Players with an ENS-Name: {unique_players_with_ens}")
