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

allSystemsCleaned = allPlanetsCleaned.groupby(['solarSystemID', 'constellationID', 'regionID','security','itemName','typeName']).size().to_frame(name = 'count').reset_index()


#To Do: split the name of the system based on finding the first space after the number of the planet to get the system name
fountain = allPlanetsCleaned[allPlanetsCleaned['regionID'] == 10000058]

#Regionid to regionname: https://gist.github.com/mentos1386/8192dba4f124395c0d7f