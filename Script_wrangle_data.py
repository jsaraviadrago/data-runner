import pandas as pd
import seaborn as sn
import numpy as np

# read the data
data_runs = pd.read_csv("C:\\Users\\JuanCarlosSaraviaDra\\Dropbox\\Garmin\\Activities_07082024.csv", sep = ";")

# Extract only the columns that will be used
data_runs = data_runs[['Activity Type', 'Date', 'Distance', 'Calories', 'Time', 'Avg HR', 'Max HR', 'Avg Run Cadence', 'Max Run Cadence', 'Avg Pace', 'Best Pace', 'Total Ascent', 'Total Descent', 'Avg Stride Length', 'Number of Laps', 'Moving Time', 'Elapsed Time',  'Min Elevation', 'Max Elevation']]

# Filter only the usefull activities
data_runs = data_runs[data_runs['Activity Type'].str.contains("Running", na = False)]
data_runs = data_runs[~data_runs['Activity Type'].str.contains("Indoor Running", na = False)]

# Get rid of the dashes
data_runs.replace('--', np.nan, inplace=True)

# Change values into right format in this case numeric
columns = ['Distance','Calories', 'Avg HR', 'Max HR', 'Avg Run Cadence', 'Max Run Cadence', 'Total Ascent','Total Descent', 'Avg Stride Length', 'Number of Laps', 'Min Elevation', 'Max Elevation']

# Change to numeric
data_runs[columns] = data_runs[columns].apply(pd.to_numeric, errors='coerce', axis = 1)

# Get the values for date format
columns_date_time = ['Date', 'Time', 'Moving Time', 'Elapsed Time']

# Change to datetime
data_runs[columns_date_time] = data_runs[columns_date_time].apply(pd.to_datetime, format = 'mixed',
                                                                  errors='coerce', axis = 1)

# Change type Pace for minutes and seconds
columns_Pace = ['Avg Pace', 'Best Pace']

# Change to minutes and seconds
data_runs[columns_Pace] = data_runs[columns_Pace].apply(pd.to_datetime, format = '%M:%S', errors = 'coerce',
                                                        axis = 1)

data_runs['Avg Pace_min'] = data_runs['Avg Pace'].dt.time

data_runs['time_in_minutes'] = data_runs['Avg Pace_min'].apply(lambda x: x.minute + x.second / 60.0 + x.hour * 60)

data_runs.to_csv("C:\\Users\\JuanCarlosSaraviaDra\\Dropbox\\Garmin\\Activities_07082024_VF.csv")

