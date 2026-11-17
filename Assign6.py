import pandas as pd
data={"NAMES":["Arnav","rohan","anushika","hemant","vikas"],
      "MARKS":[85,72,None,90,72],
      "CITY":["pune","mumbai","pune","delhi","mumbai"]
     }
df=pd.DataFrame(data)
print("Original Data:")
print(df)
print("\nDataSet Information")
df.info()
print(df.describe())
df["MARKS"]=df['MARKS'].fillna(df["MARKS"].mean())
df= df.drop_duplicates()
result=df.loc[df["MARKS"]>72]
print("\nAfter Data Preprocessing")
print(df)
print("\nStudents with marks greater than 72:")
print(result)