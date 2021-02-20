import ctypes
import os, random
import datetime as dt
import pandas as pd
import glob
import requests

SPI_SETDESKWALLPAPER = 20
PATH = 'C:/Users/Tammo/SideProjects/randombackground/'

df = pd.read_csv(PATH + 'unsplash/photos.csv')

def getNewWallpaper():
    photo = random.choice(df['photo_image_url'])
    img_data = requests.get(photo).content
    pathURL = (dt.datetime.now()).strftime("%m-%d-%Y")
    savePath = f'{pathURL}' + '.jpg'
    with open(PATH + savePath, 'wb') as handler:
        handler.write(img_data)
    return ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH + savePath, 0)

if __name__ == "__main__":
    getNewWallpaper()
