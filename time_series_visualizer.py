import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date']).set_index('date')

# Clean data
### Remove values in the top and bottom 2.5% of the data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    ### Make a copy of the dataframe
    df_line = df.copy()
    ### Set up the figure and set to appropriate size
    fig, ax = plt.subplots(figsize = (11,4))
    ### Plot data, set line colour
    ax.plot(df_line['value'], color = 'maroon')
    ### Set title and labels 
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    ### Make a copy of the dataframe
    df_bar = df.copy()
    ### Make columns for "year" and "month"
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    ### Make a pivot table using the modified dataframe to allow for aggregation using "mean"
    df_bar = pd.pivot_table(df_bar, values = 'value', index = 'year', columns = 'month', aggfunc = 'mean')

    # Draw bar plot
    ### Set up figure and set to appropriate size
    fig, ax = plt.subplots(figsize = (5,5))
    ### Plot data in bar chart 
    df_bar.plot(ax = ax, kind = 'bar')
    ### Re-label legend and x/y axis 
    ax.legend(labels = ["January", "February", "March", "April", "May", "June",     "July", "August", "September", "October", "November", "December"])
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    ### Set up figure, including two plots 
    fig, ax = plt.subplots(1,2, figsize = (15,5))
    ### Plot the first box plot
    sns.boxplot(ax = ax[0],x = 'year', y = 'value', data = df_box)
    ### Plot the second plot
    sns.boxplot(ax = ax[1], x = 'month', y ='value', data = df_box)
    ### Relabel axis and titles 
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ### Format xticks 
    ax[0].xaxis.set_major_formatter(plt.FixedFormatter(["2016", "2017", "2018", "2019"]))
    ax[1].xaxis.set_major_formatter(plt.FixedFormatter(["Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]))

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
