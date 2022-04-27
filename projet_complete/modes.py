'''
    This file contains some constants to help manage the app's two
    display modes, Percent and Count.
'''

MODES = dict(canada='Canada', switzerland='Switz', nfl="Newfoundland and Labrador")
# We've changed the 'percent' column names according to the preprocessing
MODE_TO_COLUMN = {MODES['canada']: 'Canada', MODES['switzerland']: 'Switzerland', MODES['nfl']: "Newfoundland and Labrador"} 
FRENCH_MODE_TO_COLUMN = {MODES['canada']: 'le Canada', MODES['switzerland']: 'la Suisse', MODES['nfl']: "Newfoundland et Labrador"} 