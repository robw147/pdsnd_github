### Date created
Project created on 19th November 2019
Readme created on 19th December 2019

### Project Title
Bikeshare project

### Description
This Python code analyses city bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Based on your choices it will answer different interesting questions about it by computing descriptive statistics. Analysis is performed via an interactive experience in the terminal to present these statistics.

## Statistics Computed

**#1 Popular times of travel** (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

**#2 Popular stations and trip**

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

- total travel time
- average travel time

**#4 User info**

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## An Interactive Experience

The main_project.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

## Pre-requisites
Python 3.6
See requirements.txt for required Python packages

### Files used
main_project.py

### Credits

Data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

Capital Bikeshare is metro DC's bikeshare service, with 4,300 bikes and 500+ stations across 7 jurisdictions including Washington, DC.  Data for Washington DC was downloaded from [here](https://www.capitalbikeshare.com/system-data)

Citi Bike is the nation's largest bike share program, with 12,000 bikes and 750 stations across New York City, including Manhattan, Brooklyn, Queens and Jersey City. It was designed for quick trips with convenience in mind, and it’s a fun and affordable way to get around town. Data for New York City  was downloaded from [here](https://www.citibikenyc.com/system-data).

Divvy is Chicago's bike share system, with over 600 stations and 6,000+ bikes across Chicago. Divvy bikeshare data was downloaded from [here](https://www.divvybikes.com/system-data)

Thanks also to Udacity for commisioning this project.
