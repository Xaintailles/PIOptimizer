# -*- coding: utf-8 -*-
'''
@author: Xaintailles
'''

import pandas as pd
import itertools
import json

def get_p_zero_requirements(data_folder: str, needed_p: str):
    """
    Returns p0 requirements based on inputs.
    Only works for P3 right now
    
    @data_folder: folder where data is stored
    @needed_p: name of the PI material you want to check requirements for
    """

    f = open(f"./{data_folder}/p_4_source.json")
    p4Source = json.load(f)
    
    f = open(f"./{data_folder}/p_3_source.json")
    p3Source = json.load(f)
    
    f = open(f"./{data_folder}/p_2_source.json")
    p2Source = json.load(f)
    
    f = open(f"./{data_folder}/p_1_source.json")
    p1Source = json.load(f)
    
    f = open(f"./{data_folder}/p_0_source.json")
    p0Source = json.load(f)
    
    # %% test for p4
    
    # TODO: implement when issue in test return value False
    
    test_results = []
    
    issue = False
    
    for key, value in p4Source.items():
        for source in value:
            if source not in p3Source:
                issue = True
                test_results.append({'p4': f'Issue with {source}'})   
    if not issue:
        test_results.append({'p4': True})
    
    # %% test for p3
    
    issue = False
    
    for key, value in p3Source.items():
        for source in value:
            if source not in p2Source:
                issue = True
                test_results.append({'p3': f'Issue with {source}'})   
    if not issue:
        test_results.append({'p3': True})
        
    # %% test for p2    
    
    issue = False
    
    for key, value in p2Source.items():
        for source in value:
            if source not in p1Source:
                issue = True
                test_results.append({'p2': f'Issue with {source}'})   
    if not issue:
        test_results.append({'p2': True})
        
    # %% test for p1
        
    issue = False
    
    for key, value in p1Source.items():
        for source in value:
            if source not in p0Source:
                issue = True
                test_results.append({'p1': f'Issue with {source}'})   
    if not issue:
        test_results.append({'p1': True})
    
    # %% creating the df
    
    p4df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p4Source.items() ]))\
        .melt(var_name = 'p4', value_name = 'p3')\
        .drop_duplicates()\
        .dropna()\
        .reset_index(drop = True)
    
    p3df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p3Source.items() ]))\
        .melt(var_name = 'p3', value_name = 'p2')\
        .drop_duplicates()\
        .dropna()\
        .reset_index(drop = True)
    
    p2df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p2Source.items() ]))\
        .melt(var_name = 'p2', value_name = 'p1')\
        .drop_duplicates()\
        .dropna()\
        .reset_index(drop = True)
    
    p1df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p1Source.items() ]))\
        .melt(var_name = 'p1', value_name = 'p0')\
        .drop_duplicates()\
        .dropna()\
        .reset_index(drop = True)
    
    p0df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in p0Source.items() ]))\
        .melt(var_name = 'p0', value_name = 'planet')\
        .drop_duplicates()\
        .dropna()\
        .reset_index(drop = True)
    
    
    p4necessities = pd.merge(p4df,p3df,on='p3',how='inner')
    p4necessities = pd.merge(p4necessities,p2df,on='p2',how='inner')
    p4necessities = pd.merge(p4necessities,p1df,on='p1',how='inner')
    
    
    p3necessities = pd.merge(p3df,p2df,on='p2',how='inner')
    p3necessities = pd.merge(p3necessities,p1df,on='p1',how='inner')
    p3necessities = pd.merge(p3necessities,p0df,on='p0',how='inner')
    
    
    p2necessities = pd.merge(p2df,p1df,on='p1',how='inner')
    p2necessities = pd.merge(p2necessities,p0df,on='p0',how='inner')
    
    
    # %% filtering based on request and creating cartesian product
    
    df_filtered = p3necessities[p3necessities['p3']==needed_p]
    
    unique_p0 = pd.unique(df_filtered['p0'])
    
    all_planets_list = []
    
    for p_zero in unique_p0:
        all_planets_list.append(list(df_filtered[df_filtered['p0']==p_zero]['planet']))
        
    print(all_planets_list)
    
    final_cartesian = []
    
    for element in itertools.product(*all_planets_list):
        final_cartesian.append(element)
        
    return({'test_results': test_results, 'p_zero_requirements': final_cartesian})






