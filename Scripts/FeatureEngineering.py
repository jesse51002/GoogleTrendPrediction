import pandas as pd
import json
import spacy

# ############# Gets us category data from the json file

jsonRaw = open('../Datasets/US_category_id.json')

categoryJson = json.load(jsonRaw)

categoryData = []

curIndex = 0
# Puts into a dictionary for easy access and Prints the data out
for x in categoryJson['items']:

    catId = int(x['id'])

    for i in range(curIndex, catId):
        categoryData.append("")

    curIndex = catId + 1

    categoryData.append(x['snippet']['title'])


# ############### Gets people data from excel

artistData = pd.read_csv("../Datasets/top10k-spotify-artist-metadata.csv")

instagramData = pd.read_csv("../Datasets/instagram_global_top_1000.csv")

twitterData = pd.read_csv("../Datasets/Top-1000-Celebrity-Twitter-Accounts.csv")

athleteData = pd.read_csv("../Datasets/Forbes Richest Athletes (Forbes Richest Athletes 1990-2021).csv")

politicanDataSet = pd.read_csv("../Datasets/politicans_dataset.csv")


import re
# import spacy to recognize names, countries, etc
spacyNlp = spacy.load("en_core_web_sm")

# function to fill names in with model recongizable words
def simplifyItems(text, num = 0):
    doc = spacyNlp(text)


    for ent in doc.ents:
        # will contain any extra information to give to the model along with the name
        extraInfo = {}

        def replaceEnt(replacement):
            extraInfo

        if ent.label_ == 'PERSON':
            print(ent.text)

            #will contain what will be the replacement
            replacementText = ''

            #Splits the name at space to get the first and last name
            splName = ent.text.split(" ")

            for i, x in artistData.iterrows():
                # Gets the name of the first artist in the dataframe
                artistName = x["artist"]
                # Contains how many parts names are matched in the artist's name
                matchesAmount = 0
                # Gets amount of matches
                for name in splName:
                    if artistName.contains(name):
                        matchesAmount += 1
                # if 2 parts of the name match or 100% match then name has matched
                if matchesAmount >= 2 or matchesAmount == len(splName):
                    replacementText = 'popular_artist'
                    extraInfo['rank'] = x['index']
                    replaceEnt(replacementText)
                    break













# Reads the youtube data
youtubeData = pd.read_csv("../Datasets/US_youtube_trending_data.csv")


# drops excess columns
youtubeData.drop(["video_id", "channelId", "thumbnail_link"], axis=1, inplace=True)

for i,x in youtubeData.head(3).iterrows():
    simplifyItems(x["description"])