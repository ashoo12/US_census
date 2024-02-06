import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
# This might be helpful:
from collections import Counter

pd.options.display.float_format = '{:,.2f}'.format

# load the data
df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

#  shape of the DataFrames
print(f'df_hh_income shape:{df_hh_income.shape}')
print(f'df_pct_poverty shape:{df_pct_poverty.shape}')
print(f'df_pct_completed shape:{df_pct_completed_hs.shape}')
print(f'df_share_race_city shape:{df_share_race_city.shape}')
print(f'df_fatalities shape:{df_fatalities.shape}')

# How many rows and columns do they have?
no_of_rows_df_hh_income=df_hh_income.shape[0]
print(f'no_of_rows_df_hh_income:{no_of_rows_df_hh_income}')
no_of_columns_df_hh_income=df_hh_income.shape[1]
print(f'no_of_columns_df_hh_income:{no_of_columns_df_hh_income}')

no_of_rows_df_pct_poverty=df_pct_poverty.shape[0]
print(f'no_of_rows_df_pct_poverty:{no_of_rows_df_pct_poverty}')
no_of_columns_df_pct_poverty=df_pct_poverty.shape[1]
print(f'no_of_columns_df_pct_poverty:{no_of_columns_df_pct_poverty}')

no_of_rows_df_pct_completed_hs=df_pct_completed_hs.shape[0]
print(f'no_of_rows_df_pct_completed_hs:{no_of_rows_df_pct_completed_hs}')
no_of_columns_df_pct_completed_hs=df_pct_completed_hs.shape[1]
print(f'no_of_columns_df_pct_completed_hs:{no_of_columns_df_pct_completed_hs}')

no_of_rows_df_share_race_city=df_share_race_city.shape[0]
print(f'no_of_rows_df_share_race_city:{no_of_rows_df_share_race_city}')
no_of_columns_df_share_race_city=df_share_race_city.shape[1]
print(f'no_of_columns_df_share_race_city:{no_of_columns_df_share_race_city}')

no_of_rows_df_fatalities=df_fatalities.shape[0]
print(f'no_of_rows_df_fatalities:{no_of_rows_df_fatalities}')
no_of_columns_df_fatalities=df_fatalities.shape[1]
print(f'no_of_columns_df_fatalities:{no_of_columns_df_fatalities}')

# What are the column names
print(f'df_hh_income column names :{df_hh_income.columns}')
print(f'df_pct_poverty column names:{df_pct_poverty.columns}')
print(f'df_pct_completed column names:{df_pct_completed_hs.columns}')
print(f'df_share_race_city column names:{df_share_race_city.columns}')
print(f'df_fatalities column names:{df_fatalities.columns}')

# Are there any NaN values or duplicates?
nan_values_df_hh_income=df_hh_income.isna().sum().sum()
duplicated_values_df_hh_income=df_hh_income.duplicated().sum()
print(f'nan_values_df_hh_income:{nan_values_df_hh_income}\nduplicated_values_df_hh_income:{duplicated_values_df_hh_income}')
# substitutin of 0 inplace of nan values
df_hh_income.fillna(0,inplace=True)
nan_values_df_pct_poverty=df_pct_poverty.isna().sum().sum()
duplicated_values_df_pct_poverty=df_pct_poverty.duplicated().sum()
print(f'nan_values_df_pct_poverty:{nan_values_df_pct_poverty}\nduplicated_values_df_pct_poverty:{duplicated_values_df_pct_poverty}')
nan_values_df_pct_completed_hs=df_pct_completed_hs.isna().sum().sum()
duplicated_values_df_pct_completed_hs=df_pct_completed_hs.duplicated().sum()
print(f'nan_values_df_pct_completed_hs:{nan_values_df_pct_completed_hs}\nduplicated_values_df_pct_completed_hs:{duplicated_values_df_pct_completed_hs}')
nan_values_df_share_race_city=df_share_race_city.isna().sum().sum()
duplicated_values_df_share_race_city=df_share_race_city.duplicated().sum()
print(f'nan_values_df_share_race_city:{nan_values_df_share_race_city}\nduplicated_values_df_share_race_city:{duplicated_values_df_share_race_city}')
nan_values_df_fatalities=df_fatalities.isna().sum().sum()
duplicated_values_df_fatalities=df_fatalities.duplicated().sum()
print(f'nan_values_df_fatalities:{nan_values_df_fatalities}\nduplicated_values_df_fatalities:{duplicated_values_df_fatalities}')
# substitutin of 0 inplace of nan values
df_fatalities.fillna(0,inplace=True)
print(df_fatalities.value_counts())


# # Chart the Poverty Rate in each US State
poverty_rate_us_state=df_pct_poverty.groupby('Geographic Area')['poverty_rate'].size().sort_values(ascending=False).reset_index()
print(poverty_rate_us_state)

# Create a bar chart that ranks the poverty rate from highest to lowest by US state. Which state has the highest poverty rate? Which state has the lowest poverty rate? Bar Plot
sns.barplot(data=poverty_rate_us_state,y='poverty_rate',x='Geographic Area')
plt.xlabel('US States')
plt.xticks(rotation=90)
plt.ylabel('Poverty Rate')
plt.title('poverty rate from highest to lowest by US state')
plt.show()

# Chart the High School Graduation Rate by US State
highschool_graduation_us_state=df_pct_completed_hs.groupby('Geographic Area')['percent_completed_hs'].size().sort_values(ascending=True).reset_index()
print(highschool_graduation_us_state)
# Show the High School Graduation Rate in ascending order of US States. Which state has the lowest high school graduation rate? Which state has the highest?
sns.barplot(data=highschool_graduation_us_state,y='percent_completed_hs',x='Geographic Area')
plt.xlabel('US States')
plt.xticks(rotation=90)
plt.ylabel('Percent_Completed_Highschool')
plt.title('High School Graduation Rate')
plt.show()

# Visualise the Relationship between Poverty Rates and High School Graduation Rates

# Create a line chart with two y-axes to show if the rations of poverty and high school graduation move together.
sns.lineplot(x=highschool_graduation_us_state['Geographic Area'],y=highschool_graduation_us_state['percent_completed_hs'],color='blue',label='High school graduation')
sns.lineplot(x=poverty_rate_us_state['Geographic Area'],y=poverty_rate_us_state['poverty_rate'],label='Poverty_rate',color='pink')
plt.tight_layout()
plt.show()

# Now use a Seaborn .jointplot() with a Kernel Density Estimate (KDE) and/or scatter plot to visualise the same relationship
sns.jointplot(x=poverty_rate_us_state['poverty_rate'],y=highschool_graduation_us_state['percent_completed_hs'],kind='kde')
plt.show()
plt.show()

# Seaborn's .lmplot() or .regplot() to show a linear regression between the poverty ratio and the high school graduation ratio.
sns.regplot(x=poverty_rate_us_state['poverty_rate'],y=highschool_graduation_us_state['percent_completed_hs'])
plt.show()

# Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State
# Visualise the share of the white, black, hispanic, asian and native american population in each US State using a bar chart with sub sections.
df_share_race_city[['share_white','share_black','share_native_american','share_asian','share_hispanic']]=df_share_race_city[['share_white','share_black','share_native_american','share_asian','share_hispanic']].apply(pd.to_numeric,errors='coerce')
race_sections=df_share_race_city.groupby('Geographic area')[['share_white','share_black','share_native_american','share_asian','share_hispanic']].sum()
print(race_sections)
race_sections.plot.bar(figsize=(10,6))
plt.title('Race Distribution by Geographic Area')
plt.xlabel('Geographic Area')
plt.ylabel('Share Percentage')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()

# Create Donut Chart by of People Killed by Race

people_by_race=df_fatalities.groupby('race').size().reset_index(name='count')
print(people_by_race)
# Creating the donut chart
fig = go.Figure(data=[go.Pie(labels=people_by_race['race'], values=people_by_race['count'], hole=.3)])
fig.update_layout(title='People Killed by Race')
fig.show()

# Create a Chart Comparing the Total Number of Deaths of Men and Women
people_by_gender=df_fatalities.groupby('gender').size().reset_index(name='count')
print(people_by_gender)
fig = go.Figure(data=[go.Pie(labels=people_by_gender['gender'], values=people_by_gender['count'], hole=.3)])
fig.update_layout(title='People Killed by Gender')
fig.show()

# Create a Box Plot Showing the Age and Manner of Death
people_of_age_gender=df_fatalities.groupby(['age','manner_of_death']).size().reset_index(name='count')
print(people_of_age_gender)
sns.boxplot(data=people_of_age_gender,y='age',x='manner_of_death')
plt.show()

# Were People Armed?
# In what percentage of police killings were people armed? Create chart that show what kind of weapon (if any) the deceased was carrying. How many of the people killed by police were armed with guns versus unarmed?
people_of_weapon=df_fatalities.groupby('armed').size().reset_index(name='count')
print(people_of_weapon)
sns.barplot(data=people_of_weapon,x='armed',y='count')
plt.xticks(rotation=90)
plt.show()

# How Old Were the People Killed?
# Work out what percentage of people killed were under 25 years old.
people_by_age=df_fatalities.groupby('age').size().reset_index(name='count')
print(people_by_age)
# Filter the DataFrame to include only rows where the age is less than 25
people_under_25 = df_fatalities[df_fatalities['age'] < 25]
# Calculate the total number of people killed in this age group
total_people_under_25 = people_under_25.shape[0]
# Calculate the total number of people killed across all age groups
total_people_killed = df_fatalities.shape[0]
# Calculate the percentage
percentage_under_25 = (total_people_under_25 / total_people_killed) * 100
print(f"The percentage of people killed who were under 25 years old is: {percentage_under_25:.2f}%")

# Create a histogram and KDE plot
sns.displot(df_fatalities, x='age', kind='kde', rug=True)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('Distribution of Ages of People Killed by Police')

# Show the plot
plt.show()

# Create a seperate KDE plot for each race. Is there a difference between the distributions?
people_by_race=df_fatalities.groupby('race').size().reset_index(name='count')
print(people_by_race)

sns.displot(people_by_race,x='count',hue='race')
plt.xlabel('Count')
plt.ylabel('Density')
plt.title('Distribution of Races of People Killed by Police')
plt.show()

# Mental Illness and Police Killings
people_mental_illness=df_fatalities.groupby('signs_of_mental_illness').size()
print(people_mental_illness)

sns.barplot(people_mental_illness)
plt.title('Distribution of mentally illed People Killed by Police')
plt.show()
