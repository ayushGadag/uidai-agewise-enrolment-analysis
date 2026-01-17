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

# calculations

# state cal
df["total_enrolment"] = (df["age_0_5"]+df["age_5_17"]+df["age_18_greater"])

state_total = df.groupby("state")["total_enrolment"].sum()

top_5_states = state_total.sort_values(ascending=False).head(5)

print("\nTop 5 states by Aadhaar enrolment")
for state, value in top_5_states.items():
     print(f"{state}:{value}")

# Bottom 5 states by Aadhaar enrolment (low enrolment)
bottom_5_states = state_total.sort_values().head(5)

print("\nBottom 5 states by Aadhaar enrolment:")
for state,value in bottom_5_states.items():
     print(f"{state}:{value}")



# ---------------- DATE-WISE ANALYSIS ----------------

df["date"] = pd.to_datetime(df["date"],format="mixed", dayfirst=True)

date_total = df.groupby("date")["total_enrolment"].sum()


print("\nDate-wise Aadhaar enrolment (sample):")
print(date_total.head())


# ---------------- AGE-WISE GRAPH ----------------
plt.figure(figsize=(8,5))

age_groups = age_total.index
values = age_total.values

plt.bar(age_groups, values)
plt.xlabel("Age Group")
plt.ylabel("Total Enrolment")
plt.title("Age-wise Aadhaar Enrolment Distribution")

for i, percent in enumerate(age_percent.round(2)):
    plt.text(i, values[i], f"{percent}%", ha='center', va='bottom')

plt.tight_layout()
plt.savefig("age_wise_enrolment.png")
plt.show()

# ---------------- TOP 5 STATES GRAPH ----------------
plt.figure(figsize=(8,5))

states = top_5_states.index
values = top_5_states.values

plt.bar(states, values)
plt.xlabel("States")
plt.ylabel("Total Enrolment")
plt.title("Top 5 States by Aadhaar Enrolment")

for i, value in enumerate(values):
     plt.text(i ,value, f"{value}", ha="center", va="bottom")

plt.tight_layout()
plt.savefig("top_5_states_enrolment.png")
plt.show()

# ---------------- BOTTOM 5 STATES GRAPH ----------------
plt.figure(figsize=(8,5))

states = bottom_5_states.index
values = bottom_5_states.values

plt.bar(states, values, color ="red")
plt.xlabel("States")
plt.ylabel("Total Enrolment")
plt.title("Bottom 5 States by Aadhaar Enrolment")

for i, value in enumerate(values):
     plt.text(i ,value, f"{value}", ha="center", va="bottom")

plt.tight_layout()
plt.savefig("bottom_5_states_enrolment.png")
plt.show()
