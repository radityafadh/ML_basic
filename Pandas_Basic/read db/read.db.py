from sqlalchemy import create_engine
import pandas as pd

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'aoe2_game'
DB_PORT = 3307 

# Create connection string
engine = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    # 1. Civilization Analysis
    civilization_units = pd.read_sql("""
        SELECT c.name AS civilization, 
               c.unique_unit, 
               u.attack, 
               u.armor
        FROM civilizations c
        JOIN units u ON c.unique_unit = u.name
        ORDER BY u.attack DESC
    """, engine)

    # 2. Unit Statistics
    unit_stats = pd.read_sql("""
        SELECT age, 
               COUNT(*) AS total_units,
               AVG(attack) AS avg_attack,
               MAX(attack) AS max_attack
        FROM units
        GROUP BY age
    """, engine)

    # 3. Player Performance (fixed column names)
    win_rates = pd.read_sql("""
        SELECT c.name AS civilization, 
               COUNT(m.winner_id) AS wins,
               COUNT(*) AS total_matches,
               ROUND(COUNT(m.winner_id)*100.0/COUNT(*), 2) AS win_rate
        FROM players p
        JOIN civilizations c ON p.civilization_id = c.civ_id
        LEFT JOIN matches m ON p.player_id = m.winner_id
        GROUP BY c.name
        HAVING total_matches > 0
        ORDER BY win_rate DESC
    """, engine)

    # 4. Technology Insights
    tech_by_building = pd.read_sql("""
        SELECT b.name AS building, 
               COUNT(t.tech_id) AS tech_count,
               GROUP_CONCAT(t.name) AS technologies
        FROM buildings b
        LEFT JOIN technologies t ON b.building_id = t.research_building_id
        GROUP BY b.name
        HAVING tech_count > 0
    """, engine)

    # 5. Match History
    match_history = pd.read_sql("""
        SELECT m.match_date, 
               p1.username AS winner, 
               c1.name AS winner_civ,
               p2.username AS loser,
               c2.name AS loser_civ
        FROM matches m
        JOIN players p1 ON m.winner_id = p1.player_id
        JOIN civilizations c1 ON p1.civilization_id = c1.civ_id
        JOIN players p2 ON m.loser_id = p2.player_id
        JOIN civilizations c2 ON p2.civilization_id = c2.civ_id
        ORDER BY m.match_date DESC
        LIMIT 5
    """, engine)

    # 6. Advanced: Best Civilization Analysis
    best_civ = pd.read_sql("""
        SELECT c.name AS civilization,
               COUNT(m.winner_id) AS wins,
               MAX(u.attack) AS strongest_unit_attack,
               c.bonus AS special_bonus
        FROM civilizations c
        JOIN players p ON c.civ_id = p.civilization_id
        LEFT JOIN matches m ON p.player_id = m.winner_id
        JOIN units u ON c.unique_unit = u.name
        GROUP BY c.name, c.bonus
        ORDER BY wins DESC, strongest_unit_attack DESC
        LIMIT 3
    """, engine)

    # Print the results
    print("Civilization Analysis:")
    print(civilization_units.head())

    print("\nUnit Statistics:")
    print(unit_stats.head())

    print("\nPlayer Performance:")
    print(win_rates.head())

    print("\nTechnology Insights:")
    print(tech_by_building.head())

    print("\nMatch History:")
    print(match_history.head())

    print("\nBest Civilization Analysis:")
    print(best_civ.head())

except Exception as e:
    print("❌ Error occurred:", e)