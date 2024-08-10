import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Part I: create a horizontal bar chart based on finding the top 12 causes (by count of occurances) of traffic accidents to display in a Streamlit app 

# Create a direct download URL
#file_id = '1DW_oMscvurVmphPDuVYLQ2r0C9co59d8'
download_url = https://drive.google.com/uc?export=download&id=1DW_oMscvurVmphPDuVYLQ2r0C9co59d8


# Read the CSV file from Google Drive
df = pd.read_csv(download_url, sep=';', header=0, encoding='utf-8')

# Drop multiple rows based on a list of values
df.drop(df[df['CONTRIBUTING_FACTOR_VEHICLE_1'].isin(['Unspecified', 'Other Vehicular'])].index, inplace=True)

# Count the occurrences of each contributing factor
factor_counts = df['CONTRIBUTING_FACTOR_VEHICLE_1'].value_counts()

# Get the top 12 contributing factors
top_factors = factor_counts.head(12)

# Convert the Series to a DataFrame for easier plotting with Seaborn
top_factors_df = top_factors.reset_index()
top_factors_df.columns = ['Contributing Factor', 'Count']

# Streamlit app setup
st.title('Top 12 Contributing Factors for Traffic Accidents')
st.header('New York (2013 - 2023)', divider="gray")

# Create the bar plot
fig, ax = plt.subplots(figsize=(20, 15))
sns.barplot(x='Count', y='Contributing Factor', data=top_factors_df, palette='viridis_r', ax=ax)

# Set the title and labels
#ax.set_title('Top 12 Contributing Factors for Traffic Accidents in New York (2013 - 2023)')
ax.set_xlabel('Total Accidents')
ax.set_ylabel('Contributing Factor')

# Rotate the x labels for better readability
plt.xticks(rotation=0)

# Display the plot in Streamlit
st.pyplot(fig)

# Cite source
st.text('source: https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes')


st.header("Can 'Self-Driving Cars' help reduce accidents? ")
st.markdown("**Specifically:** which categories of accidents could be reduced the most?")
st.markdown("To simplify, I grouped the 12 contributing factors into two categories: ")
st.markdown("1. Technical / Skills / Other, or, **EMOTION NEUTRAL** events, which include:")
st.markdown("- 'Backing Unsafely', 'Fatigued/Drowsy' and 'Driver Inexperience'")
st.markdown("2. Driver Attitude, or **EMOTION FUELED** events, which include:")
st.markdown("- 'Failure to Yield Right-of-Way', 'Following Too Closely', 'Passing or Lane Usage Improper', 'Passing Too Closely' , 'Turning Improperly', 'Unsafe Lane Changing', 'Traffic Control Disregarded', and 'Unsafe Speed' ")
st.markdown("'Driver Inattention/Distraction' is displayed separately for comparison.")


# Part II: group top 'contributing factors' and display as a Matplotlib pie chart on the same Streamlit app

# Create a direct download URL
file_id = '1DW_oMscvurVmphPDuVYLQ2r0C9co59d8'
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

# Read the CSV file from Google Drive
df = pd.read_csv(download_url)

# Drop rows which do not list a 'contributing factor'
df.drop(df[df['CONTRIBUTING_FACTOR_VEHICLE_1'].isin(['Unspecified', 'Other Vehicular'])].index, inplace=True)

# Define a dictionary to map original categories to new groups, including 'Driver Inattention/Distraction'
category_map = {
    'Failure To Yield Right-Of-Way': 'Driver Attitude',
    'Following Too Closely': 'Driver Attitude',
    'Passing Or Lane Usage Improper': 'Driver Attitude',
    'Passing Too Closely': 'Driver Attitude',
    'Turning Improperly': 'Driver Attitude',
    'Unsafe Lane Changing': 'Driver Attitude',
    'Traffic Control Disregarded': 'Driver Attitude',
    'Unsafe Speed': 'Driver Attitude',
    'Backing Unsafely': 'Technical/Skills',
    'Fatigued/Drowsy': 'Technical/Skills',
    'Driver Inexperience': 'Technical/Skills',
    'Driver Inattention/Distraction': 'Driver Inattention/Distraction',
}

# Standardize the column by trimming spaces and converting to title case
df['CONTRIBUTING_FACTOR_VEHICLE_1'] = df['CONTRIBUTING_FACTOR_VEHICLE_1'].str.strip().str.title()

# Filter the DataFrame to only include rows with contributing factors in the category_map keys
df_filtered = df[df['CONTRIBUTING_FACTOR_VEHICLE_1'].isin(category_map.keys())]

# Replace the contributing factor categories with the new groups
df_filtered['Grouped Factor'] = df_filtered['CONTRIBUTING_FACTOR_VEHICLE_1'].replace(category_map)

# Count the occurrences of each grouped factor
grouped_factor_counts = df_filtered['Grouped Factor'].value_counts()

# Convert the Series to a DataFrame for easier plotting
grouped_factors_df = grouped_factor_counts.reset_index()
grouped_factors_df.columns = ['Grouped Factor', 'Count']

# Using grouped_factors_df setup debug statements
labels = grouped_factors_df['Grouped Factor']
sizes = grouped_factors_df['Count']

# Print the debug statements to verify values in Python match SQL statements
print("Labels:", labels)
print("Sizes:", sizes)
print("Total:", sum(sizes))
print("Percentages:", [size / sum(sizes) * 100 for size in sizes])


# Plot the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#40867f','#c3bd44','#434976'])
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# Display the plot in Streamlit
st.pyplot(fig)

st.header("Conclusion")
st.markdown("Clearly, 'Self-Driving Cars' can help reduce accidents due to 'Technical / Skills / Other' issues (157,182 accidents) however at 14.6% it is not a very significant portion of the total")
st.markdown("Similarly, 'Driver Inattention/Distraction' (417,718 accidents) can be reduced, this time however by a more substantial amount or 38.7%")
st.markdown("However, 'Driver Attitude' (504,948 accidents) is now the largest group at 46.8%")
st.markdown("Should the focus be on this group of accidents (**:red[e.g. 'I own the road, get out of my way!']**) to help promote the adoption of 'Self-Driving Cars'?")


st.header('Data Analysis Tools Used')
st.markdown('**Dataset:** approximately 2 million rows of information (a .csv file, approx. 450MB)')
st.markdown('**SQLite / DBeaver:** database / frontend for exploring the dataset with SQL')
st.markdown('**Python:** transforming the .csv into a .db file, creating the basic script, debugging')
st.markdown('**Pandas, Matplotlib:** Data manipulation, calculations, pie chart visualization')
st.markdown('**Seaborn:** creating the main visualization')
st.markdown('**Streamlit:** Python framework to share the script, e.g. web app')
st.markdown('**Github:** developer platform for hosting the script')
st.markdown('**Google Drive:** large file storage for the script to access the data')



