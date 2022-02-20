# -*- coding: utf-8 -*-
'''
Created on Sun Feb 20 22:01:39 2022

@author: Gebruiker
'''

import pandas as pd

# %% Dic Definitions

p4Source = {
    'Broadcast Node': ['Data Chips', 'High-Tech Transmitters', 'Neocoms'],
    'Integrity Response Drones': ['Gel-Matrix Biopaste', 'Hazmat Detection Systems', 'Planetary Vehicles'],
    'Nano-Factory': ['Reactive Metals', 'Industrial Explosives', 'Ukomi Superconductors'],
    'Organic Mortar Applicators': ['Condensates', 'Robotics', 'Bacteria'],
    'Recursive Computing Module': ['Guidance Systems', 'Synthetic Synapses', 'Transcranial Microcontrollers'],
    'Self-Harmonizing Power Core': ['Camera Drones', 'Hermetic Membranes', 'Nuclear Reactors'],
    'Sterile Conduits': ['Smartfab Units', 'Vaccines', 'Water'],
    'Wetware Mainframe': ['Biotech Research Reports', 'Cryoprotectant Solution', 'Supercomputers']
    }

p3Source = {
    'Biotech Research Reports': ['Construction Blocks', 'Livestock', 'Nanites'],
    'Camera Drones': ['Rocket Fuel', 'Silicate Glass'],
    'Condensates': ['Coolant', 'Oxides'],
    'Cryoprotectant Solution': ['Fertilizer', 'Synthetic Oil', 'Test Cultures'],
    'Data Chips': ['Microfiber Shielding', 'Supertensile Plastics'],
    'Gel-Matrix Biopaste': ['Biocells', 'Oxides', 'Superconductors'],
    'Guidance Systems': ['Transmitter', 'Water-Cooled CPU'],
    'Hazmat Detection Systems': ['Polytextiles', 'Transmitter', 'Viral Agent'],
    'Hermetic Membranes': ['Gen. Enhanced Livestock', 'Polyaramids'],
    'High-Tech Transmitters': ['Polyaramids', 'Transmitter'],
    'Industrial Explosives': ['Fertilizer', 'Polytextiles'],
    'Neocoms': ['Biocells', 'Silicate Glass'],
    'Nuclear Reactors': ['Enriched Uranium', 'Microfiber Shielding'],
    'Planetary Vehicles': ['Mechanical Parts', 'Miniature Electronics', 'Supertensile Plastics'],
    'Robotics': ['Consumer Electronics', 'Mechanical Parts'],
    'Smartfab Units': ['Construction Blocks', 'Miniature Electronics'],
    'Supercomputers': ['Consumer Electronics', 'Coolant', 'Water-Cooled CPU'],
    'Synthetic Synapses': ['Supertensile Plastics', 'Test Cultures'],
    'Transcranial Microcontrollers': ['Biocells', 'Nanites'],
    'Ukomi Superconductors': ['Superconductors', 'Synthetic Oil'],
    'Vaccines': ['Livestock', 'Viral Agent'],
    'Reactive Metals': ['Reactive Metals'],
    'Bacteria': ['Bacteria'],
    'Water': ['Water']
    }

p2Source = {
    'Biocells': ['Biofuels', 'Precious Metals'],
    'Construction Blocks': ['Reactive Metals', 'Toxic Metals'],
    'Consumer Electronics': ['Toxic Metals', 'Chiral Structures'],
    'Coolant': ['Water', 'Electrolytes'],
    'Enriched Uranium': ['Toxic Metals', 'Precious Metals'],
    'Fertilizer': ['Proteins', 'Bacteria'],
    'Gen. Enhanced Livestock': ['Proteins', 'Biomass'],
    'Livestock': ['Biofuels', 'Proteins'],
    'Mechanical Parts': ['Reactive Metals', 'Precious Metals'],
    'Microfiber Shielding': ['Industrial Fibers', 'Silicon'],
    'Miniature Electronics': ['Silicon', 'Chiral Structures'],
    'Nanites': ['Reactive Metals', 'Bacteria'],
    'Oxides': ['Oxygen', 'Oxidizing Compound'],
    'Polyaramids': ['Industrial Fibers', 'Oxidizing Compound'],
    'Polytextiles': ['Industrial Fibers', 'Biofuels'],
    'Rocket Fuel': ['Electrolytes', 'Plasmoids'],
    'Silicate Glass': ['Silicon', 'Oxidizing Compound'],
    'Superconductors': ['Water', 'Plasmoids'],
    'Supertensile Plastics': ['Oxygen', 'Biomass'],
    'Synthetic Oil': ['Electrolytes', 'Oxygen'],
    'Test Cultures': ['Water', 'Bacteria'],
    'Transmitter': ['Chiral Structures', 'Plasmoids'],
    'Viral Agent': ['Bacteria', 'Biomass'],
    'Water-Cooled CPU': ['Water', 'Reactive Metals'],    
    'Reactive Metals': ['Reactive Metals'],
    'Bacteria': ['Bacteria'],
    'Water': ['Water']
    }

p1Source = {
    'Water': ['Aqueous Liquids'],
    'Industrial Fibers': ['Autotrophs'],
    'Reactive Metals': ['Base Metals'],
    'Biofuels': ['Carbon Compounds'],
    'Proteins': ['Complex Organisms'],
    'Silicon': ['Felsic Magma'],
    'Toxic Metals': ['Heavy Metals'],
    'Electrolytes': ['Ionic Solutions'],
    'Bacteria': ['Micro Organisms'],
    'Oxygen': ['Noble Gas'],
    'Precious Metals': ['Noble Metals'],
    'Chiral Structures': ['Non-CS Crystals'],
    'Biomass': ['Planktic Colonies'],
    'Oxidizing Compound': ['Reactive Gas'],
    'Plasmoids': ['Suspended Plasma'],
    }

p0Source = {
    'Aqueous Liquids': ['Barren', 'Gas', 'Ice', 'Oceanic', 'Storm', 'Temperate'],
    'Autotrophs': ['Temperate'],
    'Base Metals': ['Barren', 'Gas', 'Lava', 'Plasma', 'Storm'],
    'Carbon Compounds': ['Barren', 'Oceanic', 'Temperate'],
    'Complex Organisms': ['Oceanic', 'Temperate'],
    'Felsic Magma': ['Lava'],
    'Heavy Metals': ['Ice', 'Lava', 'Plasma'],
    'Ionic Solutions': ['Gas', 'Storm'],
    'Micro Organisms': ['Barren', 'Ice', 'Oceanic', 'Temperate'],
    'Noble Gas': ['Gas', 'Ice', 'Storm'],
    'Noble Metals': ['Barren', 'Plasma'],
    'Non-CS Crystals': ['Lava', 'Plasma'],
    'Planktic Colonies': ['Ice', 'Oceanic'],
    'Reactive Gas': ['Gas'],
    'Suspended Plasma': ['Lava', 'Plasma', 'Storm']
    }

# %% test for p4

issue = False

for key, value in p4Source.items():
    for source in value:
        if source not in p3Source:
            print(f'Issue with %s' % source)
            issue = True
            break
if not issue:
    print('Test succesfull for p4Source')

# %% test for p3

issue = False

for key, value in p3Source.items():
    for source in value:
        if source not in p2Source:
            print(f'Issue with %s' % source)
            issue = True
            break
if not issue:
    print('Test succesfull for p3Source')
    
# %% test for p2    

issue = False

for key, value in p2Source.items():
    for source in value:
        if source not in p1Source:
            print(f'Issue with %s' % source)
            issue = True
            break
if not issue:
    print('Test succesfull for p2Source')
    
# %% test for p1
    
issue = False

for key, value in p1Source.items():
    for source in value:
        if source not in p0Source:
            print(f'Issue with %s' % source)
            issue = True
            break
if not issue:
    print('Test succesfull for p1Source')

    
    

# %% creating the df

p4df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p4Source.items() ])).melt(var_name = 'p4', value_name = 'p3').drop_duplicates().dropna().reset_index(drop = True)

p3df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p3Source.items() ])).melt(var_name = 'p3', value_name = 'p2').drop_duplicates().dropna().reset_index(drop = True)

p2df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p2Source.items() ])).melt(var_name = 'p2', value_name = 'p1').drop_duplicates().dropna().reset_index(drop = True)

p1df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p1Source.items() ])).melt(var_name = 'p1', value_name = 'p0').drop_duplicates().dropna().reset_index(drop = True)

p0df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p0Source.items() ])).melt(var_name = 'p0', value_name = 'resource').drop_duplicates().dropna().reset_index(drop = True)


p4necessities = pd.merge(p4df,p3df,on='p3',how='inner')
p4necessities = pd.merge(p4necessities,p2df,on='p2',how='inner')
p4necessities = pd.merge(p4necessities,p1df,on='p1',how='inner')


p3necessities = pd.merge(p3df,p2df,on='p2',how='inner')
p3necessities = pd.merge(p3necessities,p1df,on='p1',how='inner')


p2necessities = pd.merge(p2df,p1df,on='p1',how='inner')
p2necessities = pd.merge(p2necessities,p0df,on='p0',how='inner')

test = pd.merge(p2necessities,p2necessities,on='p2', how='inner')

test = test[test['p0_x'] != test['p0_y']]
test['necessary'] = test[['resource_x','resource_y']].values.tolist()

mylist = test['necessary'].tolist()

for i in mylist:
    print(i)
    break







