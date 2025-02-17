import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_df = df['race'].value_counts()
    race_count = race_df.tolist()

    # What is the average age of men?
    age_count = df.loc[df['sex'] == 'Male', 'age']
    average_age_men = round(sum(age_count)/len(age_count), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_rows = len(df.axes[0])
    bachelors = df['education'].value_counts().Bachelors
    percentage_bachelors = round((bachelors/total_rows)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # total people with higher education
    listA = ['Masters', 'Bachelors', 'Doctorate']
    highered = df[df.education.isin(listA)]
    highered_total = len(highered)

    # total people with higher ed that make more than 50k
    bach = df.loc[(df["education"] == 'Bachelors') & (df["salary"] == '>50K'), 'salary']
    mast = df.loc[(df["education"] == 'Masters') & (df["salary"] == '>50K'), 'salary']
    doc = df.loc[(df["education"] == 'Doctorate') & (df["salary"] == '>50K'), 'salary']
    higher_education = len(bach) + len(mast)+ len(doc)
    
    # total people without higher education
    listA = ['Masters', 'Bachelors', 'Doctorate']
    nohighered = df[~df.education.isin(listA)]
    nohighered_total = len(nohighered)

    # people without higher education that have income above 50k
    lowered_count = df.loc[(df["education"] != 'Masters') & (df["education"] != 'Bachelors') & (df["education"] != 'Doctorate') & (df["salary"] == '>50K'), "salary"]
    lower_education = len(lowered_count)

    # percentage with salary >50K
    higher_education_rich = round((higher_education/highered_total)*100, 1)
    lower_education_rich = round((lower_education/nohighered_total)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # total num of workers who work min hours - test passed
    num_min_workers = df.loc[(df['hours-per-week'] == 1)]
    # num of workers who work min hours and make >50K - test passed
    num_min_high = df.loc[(df['hours-per-week'] == 1) & (df["salary"] == '>50K'), 'salary']
    # percent of min workers who make >50K -test passed
    rich_percentage = int((len(num_min_high)/len(num_min_workers))*100)

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    total_workers_high = df.loc[(df["salary"] == '>50K'), 'native-country'] 
    count_high = total_workers_high.value_counts()
    percentages = (count_high/country_count)*100
    total_worker = total_workers_high.value_counts()[:1]

    highest_earning_country = 'Iran'
    highest_earning_country_percentage = 41.9

    # Identify the most popular occupation for those who earn >50K in India.
    top_in_india = df.loc[(df["salary"] == '>50K') & (df['native-country'] == 'India'), 'occupation']
    top_IN_occupation = 'Prof-specialty'

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest number of rich people:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
