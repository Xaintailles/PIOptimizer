# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:58:03 2023

@author: Gebruiker
"""

import pandas as pd
import json

def get_region_planets(region: str):
    
    universeDump = pd.read_csv(r'./data/mapDenormalize.csv')
    
    invTypes = pd.read_csv(r'./data/invTypes.csv')
    
    with open(r"./data/region_ids.json") as f:
        regionId_region = json.load(f)      
    regionId = regionId_region[region]
    
    planetTypeId = invTypes[invTypes['typeName'].str.startswith('Planet (',na=False)]
    
    allPlanets = pd.merge(universeDump,
                          planetTypeId,
                          on='typeID',
                          how='inner')
    
    goodColumns = [
        'typeID',
        'solarSystemID',
        'constellationID',
        'regionID',
        'itemName',
        'security',
        'typeName'
    ]
    
    allPlanetsCleaned = allPlanets[goodColumns]
    
    allPlanetsCleaned['planetType'] = allPlanetsCleaned['typeName']\
                                        .str.split(' ', n=1, expand = True)[1]
    allPlanetsCleaned['planetType'] = allPlanetsCleaned['planetType']\
                                        .str.replace('(','')\
                                        .str.replace(')','')
    allSystemsCleaned = allPlanetsCleaned.groupby(['solarSystemID', 
                                                   'constellationID', 
                                                   'regionID',
                                                   'security',
                                                   'itemName',
                                                   'typeName'])\
                                        .size()\
                                        .to_frame(name = 'count')\
                                        .reset_index()
    
    region_df = allPlanetsCleaned[allPlanetsCleaned['regionID'] == int(regionId)]
    region_df['itemName'] = region_df.itemName.str.split(" ", expand = True)
    region_df = region_df[['itemName', 'planetType']]
    region_df = pd.DataFrame(region_df.groupby(['itemName','planetType'])['itemName']\
                            .count())
    region_df.columns = ['count']
    region_df = region_df.reset_index()
    
    df_system = pd.DataFrame(region_df['itemName'].unique(), columns=(['itemName']))
    df_system['key'] = '0'
    
    return(df_system, region_df)
    
test = get_region_planets('Fountain')
    
