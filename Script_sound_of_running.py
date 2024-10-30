import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pandas as pd

#-- Create the list of musical notes

scale=[]
for k in range(35, 65):
    note=440*2**((k-49)/12)
    if k%12 != 0 and k%12 != 2 and k%12 != 5 and k%12 != 7 and k%12 != 10:
        scale.append(note) # add musical note (skip half tones)
n_notes = len(scale) # number of musical notes


#-- Open the .csv file
url = "https://raw.githubusercontent.com/jsaraviadrago/data-runner/refs/heads/main/Activities_07082024_VF.csv"

df = pd.read_csv(url, sep = ",")

# Filter just for the columns needed and clean the columns (there are NAN in Avg HR)
df2 = df[['Distance', 'Calories', 'Avg HR']]
df2 = df2.dropna()

#-- Create the notes
y = df2['Distance']
min_y = np.min(y)
max_y = np.max(y)
df2['yf'] = 0.999*n_notes*(y-min_y)/(max_y-min_y) # append it to the data frame

z = df2['Calories']
min_z = np.min(z)
max_z = np.max(z)
df2['zf'] = 0.1 + 0.4*(z-min_z)/(max_z-min_z)  # append it to the data frame

# volume of each note
v = df2['Avg HR']
min_v = np.min(v)
max_v = np.max(v)
df2['vf'] = 500 + 2000 * (1 - (v - min_v) / (max_v - min_v)) # append it to the data frame

# I created inside the data frame, so I can get rid of all negative zf values and solve the issue creating the music.
df2 = df2.loc[df2['zf'] >= 0]

# Just getting the number of observations after filtering
size = df2.shape[0]
x = np.arange(size)

# Just to make the sound waves later I have to convert the columns into arrays
yf = df2['yf'].to_numpy()
zf = df2['zf'].to_numpy()
vf = df2['vf'].to_numpy()

#-- Just plot the new transformed notes
mpl.rcParams['axes.linewidth'] = 0.3
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.rcParams['axes.linewidth'] = 0.1
plt.plot(x, y, color='red', linewidth = 0.3)
plt.plot(x, z, color='blue', linewidth = 0.3)
plt.plot(x, v, color='green', linewidth = 0.3)
plt.legend(['frequency','duration','volume'], fontsize="7",
    loc ="upper center", ncol=3)
plt.show()

#-- Turn the data into music

def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration))
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

wave=[]
for t in x: # loop over dataset observations, create one note per observation
    note = int(yf[t])
    duration = zf[t]
    frequency = scale[note]
    volume = vf[t]  ## 2048
    new_wave = get_sine_wave(frequency, duration = zf[t], amplitude = vf[t])
    wave = np.concatenate((wave,new_wave))
#wavfile.write('sound_runs.wav', rate=44100, data=wave.astype(np.int16))