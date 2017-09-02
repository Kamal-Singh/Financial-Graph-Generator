from pandas_datareader import data
import datetime
from bokeh.plotting import figure, output_file, show 

def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else:
        value="Equal"
    return value

def init(symbol,bd,bm,by,ed,em,ey):
    global df
    start=datetime.datetime(by,bm,bd)
    end=datetime.datetime(ey,em,ed)
    df=data.DataReader(symbol,"google",start,end)
    df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
    df["Height"]=abs(df.Close-df.Open)
    df["Middle"]=(df.Close+df.Open)/2

def Plot(symbol):
    global p
    p=figure(x_axis_type="datetime",title='Finance Graph For '+symbol,width=1000,height=300,responsive=True,logo=None)
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label="Time"
    p.xaxis.axis_label_text_font_size="17pt"
    p.title.text_font_size="22pt"
    hours_12=12*60*60*1000
    p.segment(df.index,df.High,df.index,df.Low,color="#161615")
    p.rect(df.index[df.Status=='Increase'],df.Middle[df.Status=='Increase'],hours_12,df.Height[df.Status=='Increase'],
        fill_color='#9bf27d',line_color='#161615')
    p.rect(df.index[df.Status=='Decrease'],df.Middle[df.Status=='Decrease'],hours_12,df.Height[df.Status=='Decrease'],
        fill_color='#d83838',line_color='#161615')
    output_file("Graph.html")
    show(p)