import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Konvertierung der 'block_time' in datetime-Objekte und Extraktion der Stunden und Minuten
eth_only_bets['block_time'] = pd.to_datetime(eth_only_bets['block_time'])
eth_only_bets['hour'] = eth_only_bets['block_time'].dt.hour + eth_only_bets['block_time'].dt.minute / 60

# Erstellen eines Histogramms für die Spielzeiten
plt.figure(figsize=(10, 6))  # Größe des Diagramms

# Wir verwenden Bins für jede Stunde des Tages, von 0 bis 24
bins = np.arange(0, 24, 1)

plt.hist(eth_only_bets['hour'], bins=bins, alpha=0.75, edgecolor='black')

plt.title('Histogram of Betting Times')  # Titel des Diagramms
plt.xlabel('Time (Hours)')  # X-Achsen-Beschriftung
plt.ylabel('Amount of Games')  # Y-Achsen-Beschriftung

plt.xticks(np.arange(0, 25, 1))  # Setzt X-Achsen-Ticks für jede Stunde
plt.grid(True)  # Gitterlinien anzeigen
plt.show()  # Diagramm anzeigen
