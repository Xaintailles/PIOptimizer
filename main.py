# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 00:20:35 2022

@author: Gebruiker
"""

import pandas as pd

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

allSystemsCleaned = allPlanetsCleaned.groupby(['solarSystemID', 'constellationID', 'regionID','security','typeName']).size().to_frame(name = 'count').reset_index()

del allPlanetsCleaned
