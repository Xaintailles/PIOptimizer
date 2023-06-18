# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 00:20:35 2022

@author: Gebruiker
"""

#Regionid to regionname: https://gist.github.com/mentos1386/8192dba4f124395c0d7f

import pandas as pd
from resources import get_p_zero_requirements

universeDump = pd.read_csv(r'./data/mapDenormalize.csv')

invTypes = pd.read_csv(r'./data/invTypes.csv')

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

fountain = allPlanetsCleaned[allPlanetsCleaned['regionID'] == 10000058]
fountain['itemName'] = fountain.itemName.str.split(" ", expand = True)
fountain = fountain[['itemName', 'planetType']]
fountain = pd.DataFrame(fountain.groupby(['itemName','planetType'])['itemName']\
                        .count())
fountain.columns = ['count']
fountain = fountain.reset_index()

df_system = pd.DataFrame(fountain['itemName'].unique(), columns=(['itemName']))
df_system['key'] = '0'

result_set = get_p_zero_requirements(data_folder='data', needed_p='Robotics')

planets_requirements = result_set['p_zero_requirements']
planets_combinations = pd.DataFrame(planets_requirements)\
                        .reset_index()

df_planets_requirement = pd.melt(planets_combinations, id_vars = 'index')\
                            .drop('variable', axis=1)\
                            .groupby(['index','value'])['value']\
                            .count()
df_planets_requirement = pd.DataFrame(df_planets_requirement)
df_planets_requirement.columns = ['count']
df_planets_requirement = df_planets_requirement.reset_index()
df_planets_requirement.columns = ['index',
                                  'planetType',
                                  'count']

final_df = pd.DataFrame(columns = ['index',
                                   'planetType',
                                   'necessaryCount',
                                   'systemName',
                                   'availableCount'])

#main logic is here
for iterator in df_planets_requirement['index']:
    
    #For each index, ie combination of P0 planets
    df = df_planets_requirement[df_planets_requirement['index']==iterator]
    
    df['key'] = '0'
    
    #Cross-join the requirements and the actuals
    #Create a column showing if there are enough planet of each type
    df_2 = df.merge(df_system, on='key')
    df_2 = df_2.merge(fountain, on=['itemName','planetType'], how='left')
    df_2['viable'] = df_2.apply(lambda row: row.count_x <= row.count_y, axis = 1)
    
    #Create a new df that contains each system and if it's viable
    df_3 = df_2.groupby(['itemName','viable'])\
                .size()\
                .reset_index()\
                .rename(columns={0:'count'})
    
    #Create a new df that isolates only systems that have unique values of viable
    df_4 = df_3.groupby(['itemName'])\
                .size()\
                .reset_index()\
                .rename(columns={0:'count'})
    df_4 = df_4[df_4['count']==1]
    
    #Join df4, containing only systems with 1 value of viable
    #Isolate the systems for which unique value of viable == True
    df_3 = df_3.merge(df_4, on='itemName', how='left')
    df_3 = df_3.dropna()
    df_3 = df_3[df_3['viable'] == True]
    df_3 = pd.DataFrame(df_3[['viable','itemName']])
    
    #Grab that information, and join it to df2
    #df2 contains the requirements and all the details
    #cleanup the df
    df_2 = df_2.merge(df_3, on=['itemName'], how='left')
    df_2 = df_2[df_2['viable_y'] == True]
    df_2 = pd.DataFrame(df_2[['index',
                              'planetType',
                              'count_x',
                              'itemName',
                              'count_y']])\
        .rename(columns={
        'index': 'index',
        'planetType': 'planetType',
        'count_x': 'necessaryCount',
        'itemName': 'systemName',
        'count_y': 'availableCount'
        })
    
    #append the result to the df where we store all the results
    if iterator == 1:
        final_df = df_2
    else:
        final_df = final_df.append(df_2)
        
final_df = final_df.drop_duplicates()

#This df is a ranking of how appropriate each system is.
#The higher the count, the better the system should be.
best_system_df = final_df[['index','systemName']]\
                .drop_duplicates()
best_system_df = best_system_df\
                .groupby(['systemName'])\
                .size()\
                .reset_index()\
                .rename(columns={0:'count'})
