import numpy as np
import matplotlib.pyplot as plt
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("==== Zomato sales analysis ==== ")
print("Sales data shape :",sales_data.shape)
print("SAMPLE DATA FOR THE FIRST 3 RESTURANTS :\n",sales_data[0:3])
print("SAMPLE SALES FOR ALL RESTURANTS :\n",sales_data[:,1:5])
print("The total sales per year will be :\n")
print(np.sum(sales_data,axis=0))  #But ismein serial number bhi jud gaya hai hence we will have to FIND ANOTHER WAY.
print("The total sales per year EXCLUDING THE SERIAL NUMBERS will be :\n")
print(np.sum(sales_data[:,1:],axis=0))
print("THE MINIMUM SALES FOR EACH COMPANY :\n")
print(np.min(sales_data[:,1:],axis=1))
print("THE MAXIMUM SALES FOR EVERY YEAR :\n")
print(np.max(sales_data[:,1:],axis=0))
print(np.sum(sales_data[:,1:6],axis=0))
cumsum_matrix=np.cumsum(sales_data[:,1:],axis=1)
print("THE CUMMULATIVE SUM WILL BE:\n")
print(cumsum_matrix)
plt.figure(figsize=(4,5))  #this code determines the display size.
plt.plot(np.mean(cumsum_matrix,axis=0))
plt.title("MEAN CUMMULATIVE SALES EVERY YEAR ACROSS ALL COMPANIES")
plt.xlabel("YEAR")
plt.ylabel("MEAN CUMMULATIVE SALES")
plt.grid(True)
plt.show()










