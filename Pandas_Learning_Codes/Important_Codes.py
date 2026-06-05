import pandas as pd

df = pd.read_csv("project2-data1.csv")
print(f"DataFrame : \n {df}")
print(f" 5 lines of head of DataFrame :\n  {df.head()}")
print(f" 5 lines of tail of DataFrame :\n  {df.tail()}")
print ( f' values of column profit(10K$) : \n {df["profit(10K$)"]}')
print ( f' values of column population(10K) : \n {df["population(10K)"]}')

# index location

a = int( input(f"inter row number , index (0 to 96) :" ))
b =int( input(f"inter column number , index (0 to 1) :" ))
df_ab = df.iloc[a,b]
print(f" coordinate in row = {a+1} , column = {b+1} : {df_ab}")

# slicing

R_a = int( input(f"inter starting row number , index  0 - 96 ---> " ))
R_b=int( input(f"inter ending row number , index  0 - 96  ---> " ))

C_a = int( input(f"inter starting column number , index  0 - 1 ---> " ))
C_b = int( input(f"inter  ending column number , index  0 - 1  ---> " ))

df_ab = df.iloc[ R_a : R_b + 1 , C_a : C_b + 1]
print(df_ab)
print(f" coordinate in row = {R_a} to {R_b}, column = {C_a} to {C_b}: {df_ab}")

# unique (unrepeated values)
df_a = df["population(10K)"].unique()
print( f' unique values of column  population(10K) :\n {df_a }')

print ( df["population(10K)"] > 20)
print (df [ df["population(10K)"] > 20])
print (df [ df["population(10K)"] > 13])
df2 =df [ df["population(10K)"] > 20]

# save .py to .CSV
df2.to_csv("newdf2.csv")


