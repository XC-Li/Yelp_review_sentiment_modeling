"""
Helper Program for Yelp Project
Author: Xiaochi(George) Li
"""

from tqdm import tqdm
import json

def business_filter(file_name):
    """
    Business.json filter
    find the business that is restaurant and give them non overlap idA and idB
    
    """
    typeA = set(['American (Traditional)', 'Italian','Mexican','Chinese','American (New)','Japanese'])
    idA = {'American (Traditional)':1, 'Italian':2,'Mexican':3,'Chinese':4,'American (New)':5,'Japanese':6}
    typeB = set(['Nightlife', 'Fast Food', 'Breakfast & Brunch', 'Coffee & Tea', 'Cafes'])
    idB = {'Nightlife':1, 'Fast Food':2, 'Breakfast & Brunch':3, 'Coffee & Tea':4, 'Cafes':5}

    with open(file_name, 'r', encoding='utf-8') as file:
        business_dict = {}  # data structure: business_id -> [idA, idB]
        for record in tqdm(file, total = 188593):
            record = json.loads(record)
            if record['categories'] is not None and 'Restaurants' in record['categories']:  # business is restaurant
                business_dict[record['business_id']] = [0,0]  # initilize record
                overlapA = False
                for kwA in typeA:
                    if kwA in record['categories']:  # find a match in typeA
                        for single_category in record['categories']:
                            if single_category in (typeA - set([kwA])):
                                overlapA = True  # this record has multiple type in typeA
                        if not overlapA:
                            business_dict[record['business_id']][0] = idA[kwA]
                        continue  # only make the first match effective
                overlapB = False
                for kwB in typeB:
                    if kwB in record['categories']:  # find a match in typeB
                        for single_category in record['categories']:
                            if single_category in (typeB - set([kwB])):
                                overlapB = True  # this record has multiple type in typeB
                        if not overlapB:
                            business_dict[record['business_id']][1] = idB[kwB]
                        continue  # only make the first match effective 

    # summary of the filter step
    print("Summary")
    print("TypeA:")
    countA = 0
    for kwA in typeA:
        count = 0
        for id in business_dict:
            if business_dict[id][0] == idA[kwA]:
                count += 1
                countA += 1
        print(kwA, count)
    print("typeA: 0", len(business_dict)-countA)
    
    print("\nTypeB:")
    countB = 0
    for kwB in typeB:
        count = 0
        for id in business_dict:
            if business_dict[id][1] == idB[kwB]:
                count += 1
                countB += 1
        print(kwB, count)
    print("typeB: 0", len(business_dict)-countB)

    return business_dict

import pandas as pd
def review_loader(file_name,restaurant_dict):
    with open(file_name, 'r', encoding='utf-8') as file:
        dataset = []
        col_name = ['business_id','typeA','typeB','useful','cool','funny','review','stars']
        for record in tqdm(file, total = 5996996):
            record = json.loads(record)
            if record['business_id'] in restaurant_dict:
                bid = record['business_id']
                dataset.append([bid,restaurant_dict[bid][0],restaurant_dict[bid][1],record['useful'],record['cool'],record['funny'],record['text'],record['stars']])
    dataset = pd.DataFrame(dataset,columns=col_name).set_index('business_id')
    print(dataset.shape)
    return dataset
