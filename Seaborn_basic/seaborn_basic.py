import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Create Minecraft-themed dummy data
num_players = 100
biomes = ['Forest', 'Plains', 'Desert', 'Taiga', 'Jungle', 'Swamp', 'Mountains']
mobs = ['Zombie', 'Skeleton', 'Creeper', 'Spider', 'Enderman', 'Slime']
tools = ['Wood', 'Stone', 'Iron', 'Gold', 'Diamond', 'Netherite']
versions = ['1.16', '1.17', '1.18', '1.19', '1.20']

data = {
    'PlayerID': np.arange(1, num_players + 1),
    'Username': ['Player' + str(i) for i in range(1, num_players + 1)],
    'PlayTimeHours': np.random.normal(50, 15, num_players).clip(5, 120).round(1),
    'BlocksMined': np.random.poisson(5000, num_players) + np.random.randint(0, 5000, num_players),
    'MobsKilled': np.random.poisson(200, num_players) + np.random.randint(0, 300, num_players),
    'Deaths': np.random.poisson(15, num_players) + np.random.randint(0, 30, num_players),
    'FavoriteBiome': np.random.choice(biomes, num_players, p=[0.2, 0.15, 0.1, 0.15, 0.15, 0.1, 0.15]),
    'MostKilledMob': np.random.choice(mobs, num_players, p=[0.2, 0.2, 0.25, 0.15, 0.1, 0.1]),
    'MainToolMaterial': np.random.choice(tools, num_players, p=[0.1, 0.15, 0.3, 0.1, 0.25, 0.1]),
    'RedstoneBuilds': np.random.poisson(5, num_players) + np.random.randint(0, 10, num_players),
    'NetherVisits': np.random.poisson(3, num_players) + np.random.randint(0, 5, num_players),
    'EndVisits': np.random.poisson(1, num_players) + np.random.randint(0, 3, num_players),
    'DiamondsFound': np.random.poisson(15, num_players) + np.random.randint(0, 20, num_players),
    'GameVersion': np.random.choice(versions, num_players, p=[0.1, 0.15, 0.25, 0.3, 0.2]),
    'SurvivalMode': np.random.choice([True, False], num_players, p=[0.8, 0.2]),
    'DaysPlayed': np.random.randint(5, 365, num_players),
    'AnimalsBred': np.random.poisson(10, num_players) + np.random.randint(0, 20, num_players)
}

# Create DataFrame
minecraft_df = pd.DataFrame(data)

# Display the first 5 rows
print(minecraft_df.head())

#encoding string to num
for col in ['FavoriteBiome', 'MostKilledMob', 'MainToolMaterial', 'GameVersion', 'Username']:
    minecraft_df[col] = minecraft_df[col].astype('category').cat.codes

# #distribution plot
# sns.displot(minecraft_df, x='PlayTimeHours', kde=True, bins=15 )
# plt.show()

# #jointplot
# sns.jointplot(data=minecraft_df, x='PlayTimeHours', y='BlocksMined', kind='hex')
# plt.show()

# #kdeplot
# sns.kdeplot(data=minecraft_df, x='PlayTimeHours', y='BlocksMined', levels=5, fill=True, alpha=0.5, thresh=0.05)
# plt.show()

# #pairplot
# sns.pairplot(data=minecraft_df, hue='FavoriteBiome', palette='Set2', corner=True, diag_kind='kde')
# plt.show()

# #rugplot
# sns.rugplot(data=minecraft_df, x='PlayTimeHours', y='BlocksMined', height=0.5, color='green')
# plt.show()

# #Styling
# sns.set_style("darkgrid")
# plt.figure(figsize=(10, 6))
# sns.set_context("notebook", font_scale=1.2)
# sns.jointplot(data=minecraft_df, x='PlayTimeHours', y='BlocksMined', kind='hex')
# plt.show()

# CATEGORICAL PLOT

# #barplot
# sns.barplot(data=minecraft_df, x='FavoriteBiome', y='PlayTimeHours', order=biomes, palette='Set2')
# plt.show()

# #countplot
# sns.countplot(data=minecraft_df, x='FavoriteBiome', order=biomes, palette='Set2', hue='SurvivalMode', edgecolor='black')
# plt.show()

# #box plot
# sns.boxplot(data=minecraft_df, x='FavoriteBiome', y='PlayTimeHours', order=biomes, palette='Set2', hue='SurvivalMode')
# plt.show()

# #violin plot
# sns.violinplot(data=minecraft_df, x='FavoriteBiome', y='PlayTimeHours', order=biomes, palette='Set2', hue='SurvivalMode')
# plt.show()

# #strip plot
# sns.stripplot(data=minecraft_df, x='FavoriteBiome', y='PlayTimeHours', order=biomes, palette='Set2', hue='SurvivalMode', jitter=True)
# plt.show()

# #swarm plot
# sns.swarmplot(data=minecraft_df, x='FavoriteBiome', y='PlayTimeHours', order=biomes, palette='Set2', hue='SurvivalMode')
# plt.show()

# #palletes
# plt.figure(figsize=(10, 6))
# sns.set_style("darkgrid")
# sns.set_context("notebook", font_scale=1.2)
# sns.barplot(data=minecraft_df, x='FavoriteBiome', y='PlayTimeHours', order=biomes, palette='mako')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.show()

# #heatmap
# plt.figure(figsize=(20, 12))
# sns.heatmap(data=minecraft_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, square=True)
# plt.show()

# #clustermap on survival mode
# plt.figure(figsize=(20, 12))
# sns.clustermap(data=minecraft_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, square=True)
# plt.show()

#facetgrid
# minecraft_fg = sns.FacetGrid(data=minecraft_df, col='SurvivalMode', row='GameVersion', hue='FavoriteBiome', palette='Set2')
# minecraft_fg.map(sns.scatterplot, 'PlayTimeHours', 'BlocksMined')
# minecraft_fg.add_legend()
# plt.show()

#regplot
plt.figure(figsize=(10, 6))
sns.regplot(data=minecraft_df, x='PlayTimeHours', y='BlocksMined', scatter_kws={'alpha':0.6})
plt.title('Play Time vs Blocks Mined')
plt.xlabel('Play Time (Hours)')
plt.ylabel('Blocks Mined')
plt.grid(True)
plt.tight_layout()
plt.show()