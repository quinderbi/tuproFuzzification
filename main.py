import pandas as pd
from fuzzification import *
from inference import *
from defuzizfication import *

df = pd.read_excel('supplier.xlsx')
listSupplierPoint = []
for index, row in df.iterrows():

    harga = row["harga"]
    priceFuzzi = fuzzificationPrice(harga)

    kualitas = row["kualitas"]
    qualityFuzzi = fuzzificationQuality(kualitas)

    outputInference = inference(priceFuzzi, qualityFuzzi)

    SupplierPoint = defuzzification(outputInference)

    listSupplierPoint.append(SupplierPoint)

df["SupplierPoint"] = listSupplierPoint
df.sort_values(by=['SupplierPoint'], inplace=True, ascending=False)
print(df.head())

df.head().to_excel("hasilakhir.xlsx", index=False)
