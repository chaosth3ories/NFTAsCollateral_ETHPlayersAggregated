import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Umwandlung der 'block_time' in ein Datum im Format YYYY-MM-DD
eth_only_bets['date'] = pd.to_datetime(eth_only_bets['block_time']).dt.date

# Berechnung des ETH-Preises für jede Transaktion
eth_only_bets['eth_price'] = eth_only_bets['deposit_usd'] / eth_only_bets['deposit_eth']

# Identifizierung und Zählung der abgebrochenen Spiele pro Tag
aborted_games_per_day = eth_only_bets[eth_only_bets['is_too_little_players'] == 1].groupby('date').size()

# Berechnung des durchschnittlichen ETH-Preises pro Tag
average_eth_price_per_day = eth_only_bets.groupby('date')['eth_price'].mean()

# Erstellen des Plots
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Datum')
ax1.set_ylabel('Anzahl abgebrochener Spiele', color=color)
ax1.plot(aborted_games_per_day.index, aborted_games_per_day, color=color, label='Abgebrochene Spiele')
ax1.tick_params(axis='y', labelcolor=color)

# Zweite Y-Achse für den durchschnittlichen ETH-Preis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Durchschnittlicher ETH-Preis', color=color)
ax2.plot(average_eth_price_per_day.index, average_eth_price_per_day, color=color, label='ETH-Preis')
ax2.tick_params(axis='y', labelcolor=color)

# Formatierung des Datums auf der X-Achse
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Titel und Legende
fig.tight_layout()  # adjust layout
plt.title('Anzahl abgebrochener Spiele und ETH-Preisverlauf')
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines + lines2, labels + labels2, loc='upper left')

plt.show()
