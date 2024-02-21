import pandas as pd


def calculate_demographic_data(print_data=True):
    """
    In this challenge you must analyze demographic data using Pandas. You are given a dataset
    of demographic data that was extracted from the 1994 Census database. Here is a sample of
    what the data looks like:

    |    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
    |---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
    |  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
    |  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
    |  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
    |  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
    |  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

    You must use Pandas to answer the following questions:

    How many people of each race are represented in this dataset? This should be a Pandas series
    with race names as the index labels. (race column)
    What is the average age of men?
    What is the percentage of people who have a Bachelor's degree?
    What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make
    more than 50K?
    What percentage of people without advanced education make more than 50K?
    What is the minimum number of hours a person works per week?
    What percentage of the people who work the minimum number of hours per week have a salary of
    more than 50K?
    What country has the highest percentage of people that earn >50K and what is that percentage?
    Identify the most popular occupation for those who earn >50K in India.

    Use the starter code in the file demographic_data_analyzer.py. Update the code so all variables
    set to None are set to the appropriate calculation or code. Round all decimals to the nearest tenth.
    """
    
    
    
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)   # get the average

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts()['Bachelors'] / df.shape[0] * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    edu_mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate') | (df['education'] == 'Masters')
    sal_mask =  (df['salary'] == '>50K')
    final_mask = edu_mask & sal_mask
    higher_education_rich = round(df[final_mask].shape[0] / df[edu_mask].shape[0] * 100, 1)
    
    #Lower Education Rich
    edu_mask = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') & (df['education'] != 'Masters')
    final_mask = edu_mask & sal_mask
    lower_education_rich = round(df[final_mask].shape[0] / df[edu_mask].shape[0] * 100, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    bool_mask = (df['salary'] == '>50K') & (df['hours-per-week'] == df['hours-per-week'].min())
    rich_percentage = df[bool_mask].shape[0] / df.shape[0] * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    df = df[df['native-country'] == 'India']    #filtering only india
    df = df[df['salary'] == '>50K']             #filtering only >50K
    top_IN_occupation = df['occupation'].value_counts().idxmax()    #counting the most popular occupation

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
