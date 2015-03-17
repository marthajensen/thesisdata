# generate a time series plot for a species from the portal databse
#run using:
#python time_series_plot.py DM

import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import sys

genus = sys.argv[1]
species = sys.argv[2]
engine = sqlalchemy.create_engine('sqlite:///portal_mammals.sqlite')
data = pd.read_sql_query('''SELECT year, COUNT(species) as abundance
                            FROM surveys
                            JOIN species ON surveys.species_id=species.species_id
                            WHERE species.genus = "{}"
                            AND species.species = "{}"
                            GROUP BY year;'''.format(genus,species),engine)
							


plt.plot(data["year"], data["abundance"],'bs')
plt.xlabel('year')
plt.ylabel("abundance")
plt.title('abundance time series for {} {}'.format(genus,species))
plt.show()
