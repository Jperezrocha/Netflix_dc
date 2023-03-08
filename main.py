# Create the years and durations lists
years = list(range(2011,2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

#Create a dictionary with the two lists
movie_dict = {'years': years, 'durations': durations}
print(movie_dict)

import pandas as pd
#Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

# Import matplotlib.pyplot
import matplotlib.pyplot as plt
fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(years, durations)
plt.title('Netflix Movie Durations 2011-2020')
plt.show()

