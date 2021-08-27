import glassdoor_scrapper as gs
import pandas as pd
path ="/Users/Monsef/Downloads/chromedriver"
df=gs.get_jobs('data_scientist',15,False,path,8)