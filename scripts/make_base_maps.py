import requests
from io import BytesIO
import numpy as np
import os
import requests
from PIL import Image
from utils import *

# Function to download image from URL
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))

base_url = "https://image.gamersky.com/webimg13/db/game_map/black_myth_wukong/{map_code}/{z}/{x}_{y}.jpg"

for map_code, map_name in map_code_to_names.items():
    for z_level, z_level_name in z_level_code_to_names.items():
        os.makedirs(map_name, exist_ok=True)
        base = 500*(2**(z_level-10))
        lower = base + 8 * 2**(z_level-10)
        upper = lower + 4 * 2**(z_level-10)
        x_range = range(lower, upper)  # Example x range
        y_range = range(lower, upper)  # Example y range

        # Download images and store in a list
        images = []
        for y in y_range:
            row_images = []
            for x in x_range:
                url = base_url.format(map_code=map_code,z=z_level, x=x, y=y)
                print(f"Downloading {url}")
                img = download_image(url)
                row_images.append(img)
            images.append(row_images)

        # Determine the size of each tile
        tile_width, tile_height = images[0][0].size

        # Create a new image with the appropriate size
        map_width = tile_width * len(x_range)
        map_height = tile_height * len(y_range)
        stitched_image = Image.new('RGB', (map_width, map_height))

        # Paste each image into the correct position
        for i, row in enumerate(images):
            for j, img in enumerate(row):
                stitched_image.paste(img, (j * tile_width, i * tile_height))

        # Save the stitched image
        stitched_image.save(f"{map_name}/{z_level_name}.jpg")

        # Convert to NumPy array
        np_array = np.array(stitched_image)
        print("Map has been stitched and converted to NumPy array.")