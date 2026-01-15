# import pandas
#  import matplotlib 
import pandas as pd 
import matplotlib.pyplot as plt

# load the csv file
df = pd.read_csv("data/api_data_aadhar_enrolment_0_500000.csv")

print("first five rows:")
print(df.head())

# column
print("\nColumns in dataset:")
print(df.columns)

age_columns = ["age_0_5","age_5_17","age_18_greater"]

# sum of all age group so get total number 
age_total = df[age_columns].sum()
for age ,  value in age_total.items():
     print(f"{age}: {value}")



# age percent contribution 

age_percent = (age_total/ age_total.sum())*100.
print("\nAge-wise percentage contribution:")
for age, value in age_percent.round(2).items():     
     print(f"{age}: {value}%")

    #matplot code


age_groups = age_total.index
values = age_total.values

# bar chart
plt.figure()
plt.bar(age_groups,values)
for i, percent in enumerate(age_percent.round(2)):
    plt.text(i, values[i], f"{percent}%", ha='center', va='bottom')
# labels and titles

plt.xlabel("Age Group")
plt.ylabel("Total Enrolment")
plt.title("Age-wise Aadhaar Enrolment Distribution")

# save graph

plt.savefig("age_wise_enrolment.png")
# show graph

plt.show()