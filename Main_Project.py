import pandas as pd
filepath = '//home//workspace//'
import os
os.chdir(filepath)

import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) mode of analysis - whether the analysis should be by day, month or all of the data for the selected city
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n\n Hello! Let\'s explore some US bikeshare data! \n We will now ask you a few questions to tailor your analysis accordingly \n')
    # Ask for user input for city (chicago, new york city, washington)
    city = ''
    filter_type = ''
    day_of_week = ''
    month = ''

    while city not in ('chicago', 'new york city', 'washington'):
        city = input("Would you like to see analysis for Chicago, New York City or Washington? ").lower()
    if city =='chicago':
        print ("\n You have selected Chicago! \n")
    elif city =='new york city':
        print ("\n You have selected New York City! \n")
    elif city =='washington':
        print ("\n You have selected Washington! \n")

    # Ask for user input to choose filter by month, day or no filter
    while filter_type not in ('month','day', 'none'):
        filter_type = input("Would you like to analyze a specific month, day or the full period of data (type month, day or none): ").lower()
    if filter_type == 'month':
        print("\n You have selected to see trends for a given month \n")
    elif filter_type == 'day':
        print("\n You have selected to see trends for a given day of week \n")
    elif filter_type == 'none':
        print("\n You have selected to see trends across the whole data set \n")

    # Ask for user input to choose months
    if filter_type == 'month':
        while month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            month = input("Please choose the month you would like to analyse (please type - January, February, March, April, May or June ): ").lower()
        print("\n You have selected {} as your city and {} as your month to analyse. \n So let's see look at the trends for {} in the month of {} \n".format(city.title(),month.title(),city.title(),month.title()))
    else:
        month = 'all'


    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_type == 'day':
        while day_of_week not in ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday'):
            day_of_week = input("Please choose the day of the week you would like to analyse (please type - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ").lower()
        print("\n You have selected {} as your city and {} as your day of the week to analyse. \n So let's look at the trends for {} on a {} \n".format(city.title(),day_of_week.title(),city.title(),day_of_week.title()))
    else:
        day_of_week = 'all'

    if month == 'all' and day_of_week == 'all':
        print("\n You have selected {} as your city and no filters on month or day. \n So let's look at the trends for {} for the whole of the year to date \n".format(city.title(),city.title()))

    print('-'*100)
    return city, filter_type, month, day_of_week

def load_data(city, filter_type, month, day_of_week):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) filter_type - whether analysis should be by month, by day or not at all
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day_of_week - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day_of_week != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_of_week.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month
    month_num,count = most_common(df,'month')
    #Return the month name
    name = datetime.date(1900, month_num, 1).strftime('%B')
    print("{} was the most popular month of travel with a count of {} trips".format(name,str(count)))

    #Display the most common day of week
    name,count = most_common(df,'day_of_week')
    print("{} was the most popular day of travel with a count of {} trips".format(name,str(count)))

    # Display the most common start hour
    #Convert to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'],format='%Y/%m/%d')
    df['End Time'] = pd.to_datetime(df['End Time'],format='%Y/%m/%d')
    #Extract hour
    df['hour'] = df['Start Time'].dt.hour
    name,count = most_common(df,'hour')
    print("{} was the busiest hour with a count of {} trips".format(name,str(count)))
    print("\nProcessing of 'The Most Frequent Times of Travel' statistics took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trips."""
    print('\nCalculating Popular Stations and Trips...\n')
    start_time = time.time()
    #Most Common Start Station
    name,count = most_common(df,'Start Station')
    print("Most common starting station was {} with a count of {} trips".format(name,str(count)))
    #Most Common Ending Station
    name,count = most_common(df,'End Station')
    print("Most common ending station was {} with a count of {} trips".format(name,str(count)))
    df['journey'] = "From " + "'" + df['Start Station'] + "'" + " To " + "'" + df['End Station'] + "'"
    #Most Common Ending Station
    name,count = most_common(df,'journey')
    print("Most common journey was {} with a count of {} trips".format(name,str(count)))

    print("\nProcessing of 'The Most Popular Stations and Trips' statistics took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Returns duration stats"""
    print('\nCalculating Trip Duration Stats...\n')
    start_time = time.time()
    df['Journey Time'] = df['End Time'] - df['Start Time']
    total_journeys = df.shape[0]
    total_journey_time = df['Journey Time'].sum()
    longest_journey_time = df['Journey Time'].max()
    shortest_journey_time = df['Journey Time'].min()
    average_journey_time = df['Journey Time'].mean()
    print("The total journey time of all of the trips for your selected city and time period was {} mins!!!".format(total_journey_time))
    print("The total number of trips for your selected city and time period was {}".format(total_journeys))
    print("The average journey time for your selected city and time period was {} mins".format(average_journey_time))
    print("The shortest journey time was {} mins whilst the longest journey time was {} mins".format(shortest_journey_time,longest_journey_time))
    print("\nProcessing of 'Trip duration' statistics took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\n Here is count of user types by journey... \n")
    if city !='washington':
        print(df['User Type'].value_counts())
    else:
        print("Statistics on user types are unavailable for this city")


    # Display counts of gender
    print("\n Here is the gender counts by journey... \n")
    if city !='washington':
        print(df['Gender'].value_counts())
    else:
        print("Statistics for gender are unavailable for this city")
    # Display earliest, most recent, and most common year of birth
    print("\n Here is the age profile for the journeys... \n")
    if city !='washington':
        youngest_birth_year = df['Birth Year'].max()
        oldest_birth_year = df['Birth Year'].min()
        most_common_birth_year = df['Birth Year'].mode()
        print("\nThe youngest person who travelled was born in {},".format(int(youngest_birth_year)))
        print("whilst the oldest person was born in {} and ".format(int(oldest_birth_year)))
        print("the most common birth year for a traveller was {}.\n".format(int(most_common_birth_year)))
    else:
        print("Statistics for age profile are unavailable for this city.")

    print("\nProcessing of 'User' statistics took %s seconds." % (time.time() - start_time))
    print('-'*100)

def most_common(df,column_name):
    """
    Returns the most common result based on descending counts using value_counts method

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month and day
        (str) column_name - field to evaluate the most common with count
    Returns:
        name - most common value from the column_name
        count - associated count
    """
    result_series = df[column_name].value_counts()
    name = result_series.index[0]
    count = result_series.iloc[0]
    return name, count

def raw_data(df):
    """Returns the most common result based on descending counts using value_counts method"""
    i = 1
    raw_data_flag = "yes"
    while raw_data_flag =="yes":
        raw_data_flag  = input("Would you like to see the raw data?): ").lower()
        if i==1 and raw_data_flag == "yes":
            print(df.iloc[0:10])
        elif i>1 and raw_data_flag == "yes":
            start_row = (i-1)*10
            end_row = (i)*10
            print(df.iloc[start_row:end_row])
        elif i==1 and raw_data_flag =="no":
            print("No raw data has been requested...")
        i=i+1

def main():
    while True:
        # set filters
        city, filter_type, month, day = get_filters()
        df = load_data(city,filter_type, month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        print("\n That concludes the analysis for {} !".format(city.title()))
        print('-'*100)
        print('-'*100)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
