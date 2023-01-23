'''
    Contains some functions to preprocess the data used in the visualisation.
'''
from curses import start_color
from re import S
from tkinter.messagebox import YES
import pandas as pd
import numpy as np


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # Convert dates 
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])

    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # Filter by dates from the year "start" to the year end
    dataframe = dataframe[(dataframe['Date_Plantation'] >= str(start)+'-01-01') & (dataframe['Date_Plantation'] <= str(end)+'-12-31')]

    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighbosrhood each year.
    '''
    # Summarize df
    dataframe['year']= dataframe['Date_Plantation'].dt.year
    processed_df = (dataframe.groupby(['Arrond_Nom','year'])).size().reset_index(name='Counts')
    return processed_df


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # Restructure df through a pivot and fill empty cells with 0
    yearly_df = yearly_df.pivot(
        index='Arrond_Nom',
        columns='year',
        values='Counts').replace(np.NaN, 0)
    return yearly_df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''

    # Get daily number of planted tree by the given year and name ('arrond' and 'year')
    daily_info_df = dataframe[dataframe['Date_Plantation'].dt.year==year]
    daily_info_df = daily_info_df[daily_info_df['Arrond_Nom']==arrond]
    daily_info_df = daily_info_df.groupby(['Date_Plantation']).size().reset_index(name='Counts')
    

    # filling the dataframe with 0 on days where no trees were planted
    days=pd.date_range(daily_info_df.Date_Plantation.min(),daily_info_df.Date_Plantation.max())
    daily_info_df = daily_info_df.set_index(['Date_Plantation'])\
            .reindex(days, fill_value=0)\
            .reset_index()\
            .set_axis(daily_info_df.columns, axis=1, inplace=False)

    return daily_info_df
