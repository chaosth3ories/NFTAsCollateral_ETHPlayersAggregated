import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Anzahl der abgebrochenen Spiele
aborted_games_count = eth_only_bets['is_too_little_players'].sum()

# Identifizieren der Spieler in abgebrochenen Spielen
players_in_aborted_games = eth_only_bets[eth_only_bets['is_too_little_players'] == 1]['depositor'].nunique()

# Gesamtanzahl der einzigartigen Spieler
total_unique_players = eth_only_bets['depositor'].nunique()

# Berechnen des Prozentsatzes der Spieler in abgebrochenen Spielen im Vergleich zu allen Spielern
percentage_players_in_aborted_games = (players_in_aborted_games / total_unique_players) * 100

# Ausgabe der Ergebnisse
print(f"Amount of cancelled games: {aborted_games_count}")
print(f"Amount of unique players in cancelled games: {players_in_aborted_games}")
print(f"Percentage of players in cancelled games: {percentage_players_in_aborted_games:.2f}%")
