import pandas as pd

def percents(datacol) :
  return datacol.value_counts(normalize=True) * 100

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', na_values=['?'])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df['sex'] == 'Male'
    average_age_men = round(df.loc[men, 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bpercents = round(percents(df['education']), 1)

    percentage_bachelors = bpercents['Bachelors']

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_ed_list = ['Bachelors', 'Masters', 'Doctorate']
    in_higher_ed = df['education'].isin(higher_ed_list)
  
    higher_education = df[in_higher_ed]
    lower_education = df[~in_higher_ed]

    # percentage with salary >50K
    shpercents = percents(higher_education['salary'])
    higher_education_rich = round(shpercents['>50K'], 1)

    slpercents = percents(lower_education['salary'])
    lower_education_rich = round(slpercents['>50K'], 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_workers['hours-per-week'].count()
    
    mpercents = percents(min_workers['salary'])
    rich_percentage = mpercents['>50K']

    # What country has the highest percentage of people that earn >50K?
    country_sals = percents(df.groupby(['native-country'])['salary']).reset_index(name='percent')
    high_country_sals = country_sals[country_sals['salary'] == '>50K'].set_index('native-country')['percent']
    
    highest_earning_country_percentage = round(high_country_sals.max(), 1)
    highest_earning_country = high_country_sals[round(high_country_sals, 1) == highest_earning_country_percentage].index[0]


    # Identify the most popular occupation for those who earn >50K in India.
    india = df['native-country'] == 'India'
    high_earning = df['salary'] == '>50K'
    high_earners_india = df.loc[(india & high_earning)]
    top_IN_occupation = high_earners_india['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
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