# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 00:20:35 2022

@author: Gebruiker
"""

import pandas as pd
from resources import get_p_zero_requirements

universeDump = pd.read_csv(r'C:\Users\Gebruiker\Downloads\mapDenormalize.csv')

invTypes = pd.read_csv(r'C:\Users\Gebruiker\Downloads\invTypes (1).csv')

planetTypeId = invTypes[invTypes['typeName'].str.startswith('Planet (',na=False)]

del invTypes

allPlanets = pd.merge(universeDump,planetTypeId,on='typeID',how='inner')

del universeDump
del planetTypeId

goodColumns = ['typeID','solarSystemID','constellationID','regionID','itemName','security','typeName']

allPlanetsCleaned = allPlanets[goodColumns]

del allPlanets
del goodColumns

allPlanetsCleaned['planetType'] = allPlanetsCleaned['typeName'].str.split(' ', n=1, expand = True)[1]

allPlanetsCleaned['planetType'] = allPlanetsCleaned['planetType'].str.replace('(','')

allPlanetsCleaned['planetType'] = allPlanetsCleaned['planetType'].str.replace(')','')

allSystemsCleaned = allPlanetsCleaned.groupby(['solarSystemID', 'constellationID', 'regionID','security','itemName','typeName']).size().to_frame(name = 'count').reset_index()

fountain = allPlanetsCleaned[allPlanetsCleaned['regionID'] == 10000058]

fountain['itemName'] = fountain.itemName.str.split(" ", expand = True)

#Regionid to regionname: https://gist.github.com/mentos1386/8192dba4f124395c0d7f

test = get_p_zero_requirements()

print(test['test_results'])

planets_requirements = test['p_zero_requirements']

df_planets_requirement = pd.melt(pd.DataFrame(planets_requirements).reset_index(), id_vars = 'index').drop('variable', axis=1)

df_planets_requirement = df_planets_requirement.groupby(['index','value'])['value'].count()

df_planets_requirement = pd.DataFrame(df_planets_requirement)

df_planets_requirement.columns = ['count']

df_planets_requirement = df_planets_requirement.reset_index()


#TODO: work on getting the correct system now that you have a list of all tbhe planets needed and all the planets present