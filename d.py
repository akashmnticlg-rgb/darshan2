import pandas as pd 
import matplotlib.pyplot as plt 
data=pd.read_csv(r"C:\Users\MNTI-14\Downloads\auto-mpg.csv")
df=pd.DataFrame(data)
print(df)
print(df.head(10))
print(df.describe())
car_year=df['model year'].count()
print(car_year)
x=['2020','2021','2022','2023','2024']
y=[6,5,8,2,4]
plt.bar(x,y)
plt.xlabel("year")
plt.ylabel("car manufacture")
plt.title("car mpg")
plt.show()



