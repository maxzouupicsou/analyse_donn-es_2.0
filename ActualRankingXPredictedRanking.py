import numpy as np

# Définir le classement actuel 2023-2024 et le classement prédit pour 2024-2025
current_ranking = {
    'Arsenal': 1, 'Manchester City': 2, 'Aston Villa': 4, 'Tottenham': 5, 'Newcastle Utd': 6,
    'Chelsea': 7, 'Manchester Utd': 8, 'West Ham': 9, 'Bournemouth': 10, 'Brighton': 11,
    'Wolves': 12, 'Fulham': 13, 'Crystal Palace': 14, 'Everton': 15, 'Brentford': 16,
    'Nott\'ham Forest': 17, 'Luton Town': 18, 'Burnley': 19, 'Sheffield Utd': 20
}

predicted_ranking = {
    'Liverpool': 1, 'Tottenham': 2, 'Arsenal': 3, 'Manchester City': 4, 'Everton': 5,
    'Fulham': 6, 'Manchester Utd': 7, 'West Ham': 8, 'Chelsea': 9, 'Bournemouth': 10,
    'Newcastle Utd': 11, 'Brentford': 12, 'Wolves': 13, 'Aston Villa': 14, 'Brighton': 15,
    'Nott\'ham Forest': 16, 'Crystal Palace': 17, 'Luton Town': 18, 'Sheffield Utd': 19, 'Burnley': 20
}

# Créer des listes pour le tracé
clubs = list(predicted_ranking.keys())
current_positions = [current_ranking[club] if club in current_ranking else np.nan for club in clubs]
predicted_positions = [predicted_ranking[club] if club in predicted_ranking else np.nan for club in clubs]

# Tracé
plt.figure(figsize=(10, 8))
plt.scatter(current_positions, predicted_positions, color='blue')
plt.title('Comparison of Current vs. Predicted League Positions for Premier League Teams')
plt.xlabel('Current League Position (2023-2024)')
plt.ylabel('Predicted League Position (2024-2025)')
plt.xticks(range(1, 21))
plt.yticks(range(1, 21))
plt.grid(True)

# Annoter chaque point avec le nom du club
for i, club in enumerate(clubs):
    plt.annotate(club, (current_positions[i], predicted_positions[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.gca().invert_yaxis()  # Inverser l'axe Y pour le haut est le meilleur classement
plt.gca().invert_xaxis()  # Inverser l'axe X pour le haut est le meilleur classement
plt.show()

