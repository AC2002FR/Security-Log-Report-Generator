import pandas as pd

# Lire les logs depuis un fichier CSV
# Read logs from a CSV file
logs_df = pd.read_csv('logs.csv')

# Générer des statistiques de base
# Generate basic statistics
total_events = logs_df['event_type'].count()
info_events = logs_df[logs_df['event_type'] == 'INFO'].count()['event_type']
warning_events = logs_df[logs_df['event_type'] == 'WARNING'].count()['event_type']
error_events = logs_df[logs_df['event_type'] == 'ERROR'].count()['event_type']

# Créer un rapport sous forme de dictionnaire
# Create a report as a dictionary
report = {
    'Total Events': total_events,
    'Info Events': info_events,
    'Warning Events': warning_events,
    'Error Events': error_events
}

# Afficher le rapport
# Display the report
print("Security Log Report")
print("===================")
for key, value in report.items():
    print(f"{key}: {value}")
