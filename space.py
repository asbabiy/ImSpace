from PIL import Image
import pandas as pd
import plotly.express as px
import re
import click

@click.command()
@click.option('--file', default='', help='Path to the image')
def rgb(file):
    export = re.findall(r'\w+(?=\.(?:jpg|png))', file)
    assert export, 'Only *.jpg and *.png are supported'
    img = Image.open(file)
    img.thumbnail((200, 200))
    size = img.size
    
    colors = []
    for i in range(size[0]):
        for k in range(size[1]):
            color = img.getpixel((i, k))
            colors.append(color)
    rgb_df = pd.DataFrame(data=colors, columns=['RED', 'GREEN', 'BLUE']).drop_duplicates()
    
    fig = px.scatter_3d(rgb_df, x='RED', y='GREEN', z='BLUE', color='RED', height=1000)
    fig.update_layout(title_text='IMAGE RGB REPRESENTATION', title_x=0.5)
    fig.write_html(export[0] + '.html')
    
    click.echo('Done.')