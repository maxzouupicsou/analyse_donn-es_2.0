import pandas as pd

# Chemins vers les fichiers CSV
general_stats_path = "/path/to/general_stats.csv"
squad_stats_path = "/path/to/squad_stats.csv"
goalkeeping_stats_path = "/path/to/goalkeeping_stats.csv"
penalty_stats_path = "/path/to/penalty_stats.csv"
defensive_actions_path = "/path/to/defensive_actions.csv"

# Chargement des données
general_stats = pd.read_csv(general_stats_path)
squad_stats = pd.read_csv(squad_stats_path)
goalkeeping_stats = pd.read_csv(goalkeeping_stats_path)[['Squad', 'Performance_GA', 'Performance_Saves', 'Performance_Save%', 'Performance_CS']]
penalty_stats = pd.read_csv(penalty_stats_path)[['Squad', 'Standard_PK', 'Standard_PKatt']]
defensive_actions_stats = pd.read_csv(defensive_actions_path)[['Squad', 'Tackles_Tkl', 'Interception', 'Challenges_Tkl']]

# Calcul des points totaux et des différences de buts
general_stats['Total_Pts'] = general_stats['Home_Pts'] + general_stats['Away_Pts']
general_stats['Total_GD'] = general_stats['Home_GD'] + general_stats['Away_GD']
general_stats['Total_xGD'] = general_stats['Home_xGD'] + general_stats['Away_xGD']

# Fusion des datasets
full_data = pd.merge(general_stats, squad_stats, left_on='squad', right_on='Squad', how='inner')
full_data = pd.merge(full_data, goalkeeping_stats, on='Squad', how='inner')
full_data = pd.merge(full_data, penalty_stats, on='Squad', how='inner')
full_data = pd.merge(full_data, defensive_actions_stats, on='Squad', how='inner')

# Calcul du score de prédiction étendu avec tous les facteurs
full_data['Extended_Prediction_Score'] = (
    0.20 * full_data['Total_Pts'] +
    0.15 * full_data['Total_GD'] +
    0.15 * full_data['Total_xGD'] +
    0.10 * full_data['Possesion'] +
    0.10 * full_data['Performance_Save%'] +
    0.10 * full_data['Performance_CS'] +
    0.05 * full_data['Standard_PK'] - 0.05 * full_data['Standard_PKatt'] +
    0.05 * full_data['Tackles_Tkl'] +
    0.05 * full_data['Interception'] +
    0.05 * full_data['Challenges_Tkl']
)
full_data['Extended_Prediction_Score'] -= 0.05 * full_data['Performance_GA']

# Création d'un classement complet des équipes basé sur le nouveau score
full_ranking = full_data[['squad', 'Extended_Prediction_Score']].sort_values(by='Extended_Prediction_Score', ascending=False)

# Affichage du classement
print(full_ranking)
