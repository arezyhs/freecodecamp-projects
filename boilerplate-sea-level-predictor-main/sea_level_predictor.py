import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Use Pandas to import the data from epa-sea-level.
    df = pd.read_csv('epa-sea-level.csv')
    
    # Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = pd.Series([i for i in range(1880, 2051)])
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, 'r')
    
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    new_df = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_values2 = pd.Series([i for i in range(2000, 2051)])
    y_values2 = slope * x_values2 + intercept
    plt.plot(x_values2, y_values2, 'g')
    
    # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')    
    return plt.gca()

   