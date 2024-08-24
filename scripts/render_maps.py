import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import numpy as np
import pandas as pd
from utils import *

df = pd.read_csv('./landmarks/20240822.csv')

def get_transform(p1, m1, p2, m2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    m1 = np.array(m1)
    m2 = np.array(m2)
    
    sx = (p1[0]-p2[0])/(m1[0]-m2[0])
    sy = (p1[1]-p2[1])/(m1[1]-m2[1])
    mx = (m1[0] + m2[0])/2
    my = (m1[1] + m2[1])/2
    px = (p1[0] + p2[0])/2
    py = (p1[1] + p2[1])/2
    ox = mx - px/sx
    oy = my - py/sy
    
    s, o = np.array([sx, sy]), np.array([ox, oy])
    print(s, o)
    def transform(m):
        return (np.array(m)-o)*s

    return transform

def paste_image_centered(base_image, overlay_image, position, number, fontsize=50):
    
    overlay_width, overlay_height = overlay_image.size
    base_x, base_y = position
    paste_position = (
        base_x - overlay_width // 2,
        base_y - overlay_height // 2
    )
    base_image.paste(overlay_image, paste_position, overlay_image)
    
    draw = ImageDraw.Draw(base_image)
    text = str(number)
    font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", fontsize)
    text_width, text_height = draw.textsize(text, font=font)
    text_position = (base_x - text_width // 2, base_y - text_height // 2 - 10)
    draw.text(text_position, text, font=font, fill="red")

def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


import plotly.graph_objects as go
import plotly.express as px

for idx, map_code in enumerate(map_codes):
    map_id = start_map_id + idx
    map_name = map_code_to_names[map_code]
    anchors = map_anchors[map_code]
    print(anchors, map_code)
    transform = get_transform(anchors['local'][0], anchors['web'][0],
                             anchors['local'][1], anchors['web'][1])
    base_image_path = f'base_maps/{map_name}/2x.jpg'
    base_image_base64 = image_to_base64(base_image_path)
    icons = [Image.open(f'icons/{i}.png').convert("RGBA") for i in range(19)]

    fig = go.Figure()

    fig.add_layout_image(
        dict(
            source=f"data:image/png;base64,{base_image_base64}",
            x=0,
            y=0,
            xref="paper",
            yref="paper",
            sizex=1,
            sizey=1,
            opacity=1,
            layer="below"
        )
    )

    df_subset = df[df['map_id']==map_id].sort_values(by='landmark_catalog_uniform_id')
    df_subset[['x_transformed', 'y_transformed']] = df_subset.apply(
        lambda row: pd.Series(transform([row['x'], row['y']]) / 4), axis=1)
    df_subset['y_transformed'] *= -1
    # df_subset['description_cn'] = df_subset.apply(lambda row: html.escape(row['description_cn']), axis=1)

    # Plot with Plotly Express
    fig = px.scatter(
        df_subset,
        x='x_transformed',
        y='y_transformed',
        text='landmark_catalog_uniform_id',
        title=f"Black Myth: Wukong - {map_name}",
        custom_data=['name_cn', 'landmark_catalog_name', 'description_cn']
    )

    fig.update_traces(
        hovertemplate = 
                    "<b>%{customdata[0]}</b><br>" +
                    "<b>%{customdata[1]}</b><br><br>" +
                    "%{customdata[2]}<br>"
    )

    # Update layout to add base image
    fig.update_layout(
        images=[dict(
            source=f"data:image/jpeg;base64,{base_image_base64}",
            x=0,
            y=0,
            sizex=2048,
            sizey=2048,
            xref="x",
            yref="y",
            opacity=1,
            sizing="stretch",
            layer="below"
        )]
    )

    # Update layout to remove all gridlines, ticks, and tick labels
    fig.update_layout(
        xaxis=dict(
            range=[0, 2048],
            showgrid=False,       # Remove gridlines
            showticklabels=False, # Remove tick labels
            showline=False        # Remove axis line
        ),
        yaxis=dict(
            range=[-2048, 0],
            showgrid=False,       # Remove gridlines
            showticklabels=False, # Remove tick labels
            showline=False        # Remove axis line
        ),
        xaxis_title=None,        # Optionally remove x-axis title
        yaxis_title=None         # Optionally remove y-axis title

    )

    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
      )

    # Add custom markers using layout images
    for index, row in df_subset.iterrows():
        custom_marker_path = f'Icons/{row["landmark_catalog_uniform_id"]}.png'
        fig.add_layout_image(
            x=row['x_transformed'],
            y=row['y_transformed'],
            source=Image.open(custom_marker_path),
            xref="x",
            yref="y",
            sizex=50,  # Adjust size as needed
            sizey=50,  # Adjust size as needed
            xanchor="center",
            yanchor="middle",
            opacity=1
        )

    fig.write_html(f'interactive_maps/{convert_to_snake_case(map_name)}.html', full_html=False, include_plotlyjs='cdn')
