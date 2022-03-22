import time
import pandas as pd
import numpy as np
import statistics

CITY_DATA = { 'c': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

DAY_DATA = { 'mon': 0,
             'tue': 1,
             'wed':2,
             'thu':3,
             'fri':4,
             'sat':5,
             'sun':6,
             'all':7}

MONTH_DATA = {'jan': 1,
             'feb': 2,
             'mar':3,
             'apr':4,
             'may':5,
             'jun':6,
             'all':7}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=""
    month=""
    day=""

    while city not in CITY_DATA:
        try:
            city=input('Please select a city: Type "c" for Chicago, "ny" for New York city, or "w" Washington\n').lower()
        except ValueError:
            print('This anwser is not valid!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in MONTH_DATA:
        try:
            month=input('Please select a month: "jan", "feb", "mar", "apr", "may" or "jun". You could type all for all\n')
        except ValueError:
            print('This anwser is not valid!')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in DAY_DATA:
        try:
            day=input('Please select a day: "mon", "tue", "wed", "thu", "fri" or "sat" or "sun". You could type all for all\n')
        except ValueError:
            print('This anwser is not valid!')
    print('-'*40)
    print("You selected the city of {} for {} month(s) for {} day(s)\n".format(city,month,day))
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time New'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time New'].dt.month
    df['day_of_week'] = df['Start Time New'].dt.weekday
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time New'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == MONTH_DATA[month]]

    # filter by day of week if applicable
    if day != 'all':
        # filter by month to create the new dataframe
        df = df[df['day_of_week'] == DAY_DATA[day]]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        popular_month = df['month'].mode()[0]
        print('Most Frequent Month:', popular_month)
    # TO DO: display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print('Most Frequent Day of the week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['stations'] = df['Start Station']+ ' and ' + df['End Station']
    popular_stations = df['stations'].mode()[0]
    print('Most Frequent Combinaison of Start and End station:', popular_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time (in seconds): ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time (in seconds): ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of users types\n', user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))

    # TO DO: Display counts of gender
def user_stats2(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats2...\n')
    start_time = time.time()
    df['Gender'] = df['Gender'].fillna('Unknown')
    user_gender = df['Gender'].value_counts()
    print('Count of users Genders\n', user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    df['Birth Year'] = df['Birth Year'].dropna()
    earliest_year = int((df['Birth Year']).min())
    print('Earliest year of birth:', earliest_year)
    recent_year = int((df['Birth Year']).max())
    print('Most recent year of birth:', recent_year)
    common_year = int(df['Birth Year'].mode()[0])
    print('Most common year of birth:', common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def display_data(df):
    """Displays data on user demand - display rows 5 by 5"""
    count = 0
    answer = 'yes'
    while answer != 'no':
        answer = input('\nDo you want to see 5 rows of data? Type "yes" to display data or "no" to exit\n')
        print(df.iloc[count:count+5])
        count +=5

def main():
    while True:
        # Get input from user 
        city, month, day = get_filters()
        # Filter data accordingly 
        df = load_data(city, month, day)
        # Display statistics 
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city != 'w':
            user_stats2(df)
        display_data(df)
        # Loop to restart 
        restart = input('\nWould you like to restart an analysis? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you. Have a good day!\n')
            break


if __name__ == "__main__":
	main()
