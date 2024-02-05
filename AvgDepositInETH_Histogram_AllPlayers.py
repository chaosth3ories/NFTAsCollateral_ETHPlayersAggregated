import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einsätze in ETH
eth_only_bets = data[data['collateral_name'] == 'ETH']

# Filtern der Daten, um nur Wetten bis 2 ETH einzuschließen
filtered_data = eth_only_bets[eth_only_bets['deposit_eth'] <= 2]

# Erstellen eines Histogramms für die durchschnittlichen Wetten in ETH
plt.figure(figsize=(10, 6))  # Größe des Diagramms

# Berechnung der Bins in 0.05 ETH Schritten bis 2 ETH
bins = np.arange(0, 1.55, 0.05)

plt.hist(filtered_data['deposit_eth'], bins=bins, alpha=0.75, edgecolor='black')

plt.title('Histogram of Average Bets in ETH')  # Titel des Diagramms
plt.xlabel('Amount in ETH')  # X-Achsen-Beschriftung
plt.ylabel('Amount of Players')  # Y-Achsen-Beschriftung

plt.grid(True)  # Gitterlinien anzeigen
plt.xlim(0, 2)  # Beschränkung der X-Achse bis 2 ETH
plt.show()  # Diagramm anzeigen

