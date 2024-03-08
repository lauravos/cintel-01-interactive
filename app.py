import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render


#add title
ui.page_opts(title="Gagnon PyShiny App with Plot", fillable=True)

#Create sidebar with a slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 100, 25)

#Define a plot function for rendering a histogram
@render.plot(alt="A histogram")
def histogram():
    #set random seed
    np.random.seed(3)
    #generate data for histogram
    randomData = 100 + 15 * np.random.randn(437)
    #plot histogram
    plt.hist(randomData, input.selected_number_of_bins(), density=True)
    plt.title("Histogram")

#make a scatterplot
@render.plot(alt="A scatterplot")
def scatterplot():
    #set random seed
    np.random.seed(3)
    #generate data for scatterplot
    x = np.random.randn(50)
    y = np.random.randn(50)
    #plot scatterplot
    plt.scatter(x,y)
    plt.title("Scatterplot")
