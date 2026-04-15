import pandas as pd

df = pd.read_csv("./datasets/sample_employee_data.txt")
# print(df)

df.iloc[0:, 0:].to_csv("./datasets/emp_data.csv")

# from df get only Firstname and Email

# sub_df = df[["Firstname", "Email"]]
# print(sub_df)


# sub_df = df[["Lastname", "Phone"]]
# print(sub_df)

# sub_df = df[["Firstname", "Email", "Phone", "Country"]]
# print(sub_df)


# Get me initial 5 records only.

# sub_df = df.iloc[0:10]    # When you slice Rows
# print(sub_df)


# Get me records from first 2 columns
# sub_df = df.loc[0:5, ["Firstname", "Salary"]]
# print(sub_df)


# sub_df = df.iloc[0:5, 4:7]
# print(sub_df)

# Conditional Slicing (Hybrid):-

# From Initial 10 rows get me only those Employees whose age is lesser than 25

# sub_df = df.iloc[0:10][df["Age"]> 35]
# print(sub_df)

# Get me those employees whose salary is less than 50000

# df_salary_less_than_50000 = df[df["Salary"]<50000]
# print(df_salary_less_than_50000)

# Get me all those employees whose salary is greater than 50000 and gender is Male

# df_sal_gender = df[(df["Salary"] > 50000) & (df["Gender"]=="Male")]
# print(df_sal_gender)


# Get me  all those Female Employess Who are 
# from USA a and from HR Department

# sub_df = df[(df["Gender"]== "Female") & (df["Country"]=="USA") & (df["Department"]=="HR")]
# print(sub_df)

# print(df[["Age", "Salary", "Experience"]].describe())

