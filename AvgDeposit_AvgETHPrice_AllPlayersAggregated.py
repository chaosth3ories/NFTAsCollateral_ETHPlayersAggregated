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

# Berechnung der durchschnittlichen Einsatzhöhe in ETH und des durchschnittlichen ETH-Preises pro Tag
average_deposit_per_day = eth_only_bets.groupby('date')['deposit_eth'].mean()
average_price_per_day = eth_only_bets.groupby('date')['eth_price'].mean()

# Erstellen des Plots
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Datum')
ax1.set_ylabel('Durchschnittliche Einsatzhöhe in ETH', color=color)
ax1.plot(average_deposit_per_day.index, average_deposit_per_day, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Zweite Y-Achse für den durchschnittlichen ETH-Preis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Durchschnittlicher ETH-Preis', color=color)
ax2.plot(average_price_per_day.index, average_price_per_day, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Formatierung des Datums auf der X-Achse
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

fig.tight_layout()  # adjust layout
plt.title('Durchschnittliche Einsatzhöhe in ETH und durchschnittlicher ETH-Preis')
plt.show()
