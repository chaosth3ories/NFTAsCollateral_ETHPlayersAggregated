import pandas as pd


# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Anzahl der Runden (Sessions) pro Spieler
sessions_per_player = eth_only_bets.groupby('depositor')['roundid'].nunique()

# Durchschnittliche und mediane Anzahl der Sessions pro Spieler
average_sessions_per_player = sessions_per_player.mean()
median_sessions_per_player = sessions_per_player.median()

# Ausgabe der Ergebnisse
print(f"Durchschnittliche Anzahl der Sessions pro Spieler: {average_sessions_per_player:.2f}")
print(f"Median der Anzahl der Sessions pro Spieler: {median_sessions_per_player:.2f}")

