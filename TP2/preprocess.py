'''
    Contains some functions to preprocess the data used in the visualisation.
'''
from audioop import reverse
from ipaddress import collapse_addresses
from numpy import column_stack
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act

    # add the desired columns to the dataframe
    my_df = my_df.drop(['Scene','Line'], axis = 1)
    my_df["PlayerLine"]=''
    my_df["PlayerPercent"]=''
    # for each act, modify the dataframe by adding the new information
    
    for act in range(1,6):
        # get list of players for the current act
        players = my_df.loc[my_df['Act'] == act]['Player'].unique()
        # get total number of lines for the current act
        total_lines = my_df.loc[my_df['Act'] == act]['Act'].count()
        # cycle through players to count their lines
        for player in players:
            # create tmp dataframe containing every line of the current act
            tmp = my_df.loc[my_df['Act'] == act]
            # counting lines for the current player in the current act
            n_lines = tmp.Player.value_counts()[player]
            # create new entry and put it to the top of the dataframe
            my_df.loc[-1] = [act, player, n_lines, 100*n_lines/total_lines]
            my_df.index = my_df.index + 1
            my_df = my_df.sort_index()
    # remove all the useless columns (the ones without anything in the PlayerLine column)
    my_df.drop(my_df[ my_df['PlayerLine'] == '' ].index, inplace=True)
    
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    
    # redefine the columns
    my_df = my_df.rename(columns={"PlayerLine": "LineCount", "PlayerPercent": "LinePercent"})

    # we compute the number of lines in total each players by iterating on players
    top_players = list()
    for player in pd.unique(my_df["Player"]).tolist():
        tmp = my_df[my_df["Player"] == player]
        lineCount = tmp['LineCount'].sum()
        top_players.append((player, lineCount))
    
    # we store the 5 players that speaks the most
    top_players =  [x[0] for x in sorted(top_players, key=lambda tup: tup[1], reverse=True)[:5]]

    # In each act we compute the number of lines for the top 5 speakers and the others
    for act in range(pd.unique(my_df["Act"]).shape[0]):
        tmp = my_df[my_df["Act"] == act+1]
        
        # extract people who are not top speakers
        tmp_2 = tmp.copy()
        for player in top_players:
            tmp_2.drop( tmp_2[ tmp_2['Player'] == player ].index , inplace=True)
        
        # define a dataframe row for others
        data = {'Act':act+1, 'Player': 'OTHERS', 'LineCount': tmp_2['LineCount'].sum(), 'LinePercent':tmp_2['LinePercent'].sum()}

        # we create a new daataframe by adding first the information of th top 5 speakers
        tmp_3=pd.DataFrame()
        for player in top_players:
            tmp_3 = tmp_3.append(tmp[tmp['Player'] == player])
        
        # we add the data row of the others
        tmp_3 = tmp_3.append(data, ignore_index=True)

        # order alphabetically the dataframe
        tmp_3 = tmp_3.sort_values(by='Player')

        # we update the final dataframe by adding the current act information to it
        my_df = my_df[my_df['Act'] != act+1]
        my_df = my_df.append(tmp_3)    
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    my_df['Player'] = my_df['Player'].str.title()
    return my_df
