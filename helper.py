import pandas as pd


# make a function that will take all the column names ["OBČINE", "Občina", "OB�INE", "Kohezijska / Statistična regija", "Kohezijska / statistična regija", "Kohezijska / \nstatistična regija", "Urad za delo"]
# and turn those into a new column name "regija"

REGIJA = {"občine", "občina", "ob�ine", "urad za delo"}

LETO = {"leto", "year"}

def normaliziraj_imena_stolpcev(df):
    # find all the columns that have the names in REGIJA and create a new column "regija"
    for imeStolpca in df.columns:
        print("Col name: ", imeStolpca);
        imeStolpcaLower = imeStolpca.lower().strip()
        print("Col name: ", imeStolpca);
        print("Col name: ", imeStolpcaLower);
        if imeStolpca in REGIJA:
            df["__region"] = df[imeStolpca]
            break
        
        if imeStolpcaLower in LETO:
            df["__year"] = df[imeStolpca]
        
