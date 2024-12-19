# Installing Marvel Package
pip install marvel

# Create an account on Marvel Developer Portal to get public and private key to access Marvel Data using Api
from marvel import Marvel
marvel = Marvel(PUBLIC_KEY = "###", PRIVATE_KEY = "###" )

characters = marvel.characters
ch = characters.all() 
#  this gives list of all the characters or superheroes 

# Now creating a list suoerheroes with required data as per our need
char_details = []
for i in ch:
    char_id = i['id']
    char_name = i['name']
    num_series = i['series']['available']
    num_comics = i['comics']['available']
    num_stories  = i['stories']['available']
    char_dect = {"char_id":i['id'], "char_name":i['name'], "char_desc":i['description'], "num_series":i['series']['available'], "num_comics":i['comics']['available'], "num_stories":i['stories']['available']}
    char_details.append(char_dect)


# Finally converting the list into a csv file for further analysis
import pandas as pd
marvel_char = pd.DataFrame(char_details)
marvel_char.to_csv(r'file_name.csv')

