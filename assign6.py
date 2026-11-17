import pandas as pd
data={"NAMES":["Arnav","rohan","anushika","hemant","vikas"],
      "MARKS":[85,72,nan,90,72],
      "CITY":["pune","mumbai","pune","delhi","mumbai"]
     }
df=pd.DataFrame(data)
print("Original Data:")
print(df)
print("\nDataSet Information")
df.info()
print(df.describe())
df["Marks"]=df["Marks].fillna(df["Marks"].mean())
df=df.drop_duplicates()
result=df.loc[df["Marks"]>72]
print("\n After Data Preprocessing")
print(df)
print("\n Students with marks greater than 72:")
print(result)
