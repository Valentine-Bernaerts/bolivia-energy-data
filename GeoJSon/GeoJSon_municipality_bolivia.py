import geopandas as gpd

# 1. Charger le fichier GeoJSON complet
gdf_bolivia = gpd.read_file("bol_municipios_339_pob2012_ed.geojson")

# 2. Ta liste extraite du CSV (corrigée avec des espaces)
# J'ai retiré le "TOTAL" et remplacé les "_" par des espaces
mes_21_mun = [
    'Exaltación', 'Guayaramerín', 'Reyes', 'Riberalta', 'Santa Rosa', 
    'Ixiamas', 'Bella Flor', 'Bolpebra', 'Cobija', 'Filadelfia', 
    'Ingavi', 'Nueva Esperanza', 'Porvenir', 'Puerto Gonzalo Moreno', 
    'Puerto Rico', 'San Lorenzo', 'San Pedro', 'Santa Rosa', 
    'Santos Mercado', 'Sena', 'Villa Nueva'
]

# Note : Comme il y a deux "Santa Rosa" (un dans le Beni et un dans le Pando), 
# le filtre NOM_MUN va normalement prendre les deux, ce qui est correct pour toi.

# 3. Filtrer le GeoJSON
gdf_norte_amazonica = gdf_bolivia[gdf_bolivia['NOM_MUN'].isin(mes_21_mun)]

# 4. Vérification de sécurité
found = gdf_norte_amazonica['NOM_MUN'].unique()
missing = set(mes_21_mun) - set(found)

print(f"Nombre de municipalités trouvées dans le GeoJSON : {len(gdf_norte_amazonica)}")

if missing:
    print(f"⚠️ Attention ! Ces noms n'ont pas été trouvés : {missing}")
    print("Conseil : Vérifie si l'orthographe est différente dans le GeoJSON (ex: accents).")
else:
    print("✅ Parfait ! Toutes les municipalités ont été trouvées.")

# 5. Sauvegarder le résultat pour ton usage final
gdf_norte_amazonica.to_file("norte_amazonica_21.geojson", driver='GeoJSON')
print("Fichier 'norte_amazonica_21.geojson' créé avec succès !")