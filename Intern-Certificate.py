from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

#pip install pillow
#pip install pandas
#pip install os

df = pd.read_csv('IntenDetails.csv') #Read from .csv file
fontName = ImageFont.truetype('fonts/Lato-Black.ttf',160) #Font style and size
fontDomain = ImageFont.truetype('fonts/Lato-Black.ttf',100)
fontDuration = ImageFont.truetype('font/arial.ttf',75)
fontIssueDate1 = ImageFont.truetype('fonts/Lato-Black.ttf',70)
fontIssueDate2 = ImageFont.truetype('fonts/Lato-Black.ttf',180)
fontID = ImageFont.truetype('fonts/Lato-Black.ttf',60)
fontSpecial = ImageFont.truetype('fonts/Lato-Black.ttf',70)

for index,j in df.iterrows():
    img = Image.open('blank.png') #Open the .jpg file
    draw = ImageDraw.Draw(img)

    #Issue Date
    id = j['IssueDate(dd-mmm-yyyy)'].split('-')
    line1 = id[1]+" "+id[2]
    if len(id[0])==1:
        line2 = "0"+id[0]
    else:
        line2 = id[0]
    draw.text(xy=(260,250),text='{}'.format(line1),fill=(0,0,0),font=fontIssueDate1)
    draw.text(xy=(325,350),text='{}'.format(line2),fill=(0,0,0),font=fontIssueDate2)

    #Name
    name = j['Name'].split(' ',1)
    if len(name)>1:
        draw.text(xy=(260,990),text='{}'.format(name[0]),fill=(0,0,0),font=fontName)
        draw.text(xy=(260,1200),text='{}'.format(name[1]),fill=(0,0,0),font=fontName)
    else:
        draw.text(xy=(260,1200),text='{}'.format(name[0]),fill=(0,0,0),font=fontName)

    tag = ' '.join([str(s) for s in name])

    #ID
    draw.text(xy=(260,1535),text='{}'.format(j['ID']),fill=(0,0,0),font=fontID)

    #Special
    draw.text(xy=(1975,1370),text='{}'.format(j['Special']),fill=(255,140,0),font=fontSpecial)


    #Domain
    draw.text(xy=(1787,1145),text='{}'.format(j['Domain']),fill=(0,0,0),font=fontDomain)

    #Duration with start and end dates
    dd = j['StartDate'] + " to " + j['EndDate']  #double date
    draw.text(xy=(2150,1525),text='{}'.format(dd),fill=(0,0,0),font=fontDuration)


    img.save('Generated-Certificates/{}.png'.format(tag))
