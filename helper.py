import pandas as pd


# make a function that will take all the column names 
# and turn those into a new column name "regija"

REGIJA = {"občine", "občina", "ob�ine", "kohezijska / statistična regija", "kohezijska / statistična regija", "kohezijska / \nstatistična regija", "urad za delo"}

LETO = {"leto", "year"}

def normaliziraj_imena_stolpcev(df):
    # find all the columns that have the names in REGIJA and create a new column "regija"
    for imeStolpca in df.columns:
        imeStolpcaLower = imeStolpca.lower().strip()
        if imeStolpcaLower in REGIJA:
            df["__region"] = df[imeStolpca]
            break
        
        if imeStolpcaLower in LETO:
            df["__year"] = df[imeStolpca]
        
