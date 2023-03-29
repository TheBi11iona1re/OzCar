import pandas as pd
import numpy as np
def cleandata(file):
    df = pd.read_csv(file)
    print("Number of rows in orignal file: "+str(len(df)))
    emptyvalues = np.where(pd.isnull(df))
    print("Number of rows containing empty values: "+str(len(set(emptyvalues[0]))))
    #creates new dataframe without rows that have empty values
    dfempty = df.drop(emptyvalues[0])
    #remove duplicate rows
    dfclean = dfempty.drop_duplicates()
    print("Number of duplicate rows: "+str(len(dfempty)-len(dfclean)))
    print("Number of rows in cleaned dataframe: "+str(len(dfclean)))
    df["Color"] = df["Color"].replace(regex=["whte", "whtie", "while", "wr", "waite"], value = "white") #Turns misspelled white into white
    df["Color"] = df["Color"].replace(regex=["baige"], value="beige") 
    df["Color"] = df["Color"].replace(regex=["missano"], value="misano") 
    df["Color"] = df["Color"].replace(regex=["perl"], value="pearl")
    df["Color"] = df["Color"].replace(regex=["onxy"], value="onyx")
    df["Color"] = df["Color"].replace(regex=["bugerney"], value="burgundy")
    df["Color"] = df["Color"].replace(regex=["charcol"], value="charcoal")
    df["Color"] = df["Color"].replace(regex=["crÃ¨me"], value="cream")
    df["Color"] = df["Color"].replace(regex=["leatherette", "learher"], value="leather")
    df["Color"] = df["Color"].replace(regex=["lighting"], value="lightning")
    df["Color"] = df["Color"].replace(regex=["metalic"], value="metallic")
    df["Color"] = df["Color"].replace(regex=["silber"], value="silver")
    df["Color"] = df["Color"].replace(regex=["gray", "greg"], value ="grey")
    return dfclean

