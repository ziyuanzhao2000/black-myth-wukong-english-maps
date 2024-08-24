import requests
import pandas as pd
from utils import *

# Get location data
landmarks_url = "https://mapapi.gamersky.com/landmark/getLandmarkList"
headers = {
    "Content-Type": "application/json", 
    "Accept": "application/json" 
}

df_lst = []
for idx, (map_code, map_name) in enumerate(map_code_to_names.items()):
    map_id = start_map_id + idx
    map_name = map_code_to_names[map_id_to_code(map_id)]
    payload = {
        "catalogIdsSelected": map_id_to_landmark_catalog_ids[map_id],
        "gameMapId": map_id  
    }
    response = requests.post(landmarks_url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Got all location data for the map {map_name}")
        data = response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
    landmarks = data['landmarks']
    data = {
        'description_cn': [landmark['description'] for landmark in landmarks],
        'name_cn': [landmark['name'] for landmark in landmarks],
        'id': [landmark['id'] for landmark in landmarks],
        'landmark_catalog_id': [landmark['landmarkCatalogId'] for landmark in landmarks],
        'x': [landmark['x'] for landmark in landmarks],
        'y': [landmark['y'] for landmark in landmarks]
    }
    df = pd.DataFrame(data)
    df['map_id'] = map_id
    df['map_name'] = map_name
    df['landmark_catalog_name'] = df.apply(lambda row: landmark_id_to_catalog_name(map_id, row['landmark_catalog_id']), 
                                           axis=1)
    df['description_en'] = 'Translation Pending'
    df['name_en'] = 'Translation Pending'
    df_lst.append(df)
    
df = pd.concat(df_lst)
df['landmark_catalog_uniform_id'] = df.apply(lambda row: catalog_id_to_uniform_id(row['map_id'], 
                                                                                  row['landmark_catalog_id']), axis=1)
df = df.astype({
    'description_cn': 'str',
    'name_cn': 'str',
    'description_en': 'str',
    'name_en': 'str',
    'id': 'int64',
    'landmark_catalog_id': 'int64',
    'landmark_catalog_name': 'str',
    'x': 'float64',
    'y': 'float64',
    'map_id': 'int64',
    'map_name': 'str',
})