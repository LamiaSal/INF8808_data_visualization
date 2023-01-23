'''
    This file contains some constants to help manage the app's two
    display modes, Percent and Count.
'''

MODES = dict(count='Count', percent='Percent')
# We've changed the 'percent' column names according to the preprocessing
MODE_TO_COLUMN = {MODES['count']: 'LineCount', MODES['percent']: 'LinePercent'} 