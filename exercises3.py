# ==========================================
# Week 3: Visualizing Data with Matplotlib
# ==========================================
# Save this file as exercises3.py
# Topics:
#   * Installing Matplotlib
#   * Loading data (basic pandas example)
#   * Line and scatter plots
#   * Customizing titles, labels, colors
#   * Using colormaps and sizes
#   * Bar charts
# Learning Objectives:
#   * Represent numerical data visually with Matplotlib.
#   * Customize plots for clarity and presentation.
#   * Choose appropriate chart types for your data.

# ==========================================
# Exercise 1: Installing Matplotlib
# ------------------------------------------
# In your terminal or notebook, run the following command:
#   pip install matplotlib pandas
# (No code to write here — just ensure you can import these libraries below)
              #done

# ==========================================
# Exercise 2: Importing Libraries
# ------------------------------------------
# Import matplotlib.pyplot as plt
# Import pandas as pd
# Print a confirmation message that they are loaded.
import matplotlib.pyplot as plt
import pandas as pd
print("matplotli.pyplot and pandas are loaded")

# ==========================================
# Exercise 3: Line Plot
# ------------------------------------------
# Create a list of x-values [1, 2, 3, 4, 5] and y-values [2, 4, 6, 8, 10].
# Use plt.plot() to plot x vs y.
# Add a title, and labels for x and y axes.
# Show the plot using plt.show().
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.title("plot of x and y values")
plt.xlabel("numbers")
plt.ylabel("even numbers")
plt.show()

# ==========================================
# Exercise 4: Scatter Plot
# ------------------------------------------
# Create two lists:
#   x_values = [1, 2, 3, 4, 5]
#   y_values = [2, 3, 5, 7, 11]
# Use plt.scatter() to plot the data.
# Add axis labels and a title.
# Show the plot.
x_values = [1,2,3,4,5]
y_values = [2,3,5,7,11]
plt.scatter(x_values,y_values)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("I am not sure what to give")
plt.show()

# ==========================================
# Exercise 5: Customizing Plots
# ------------------------------------------
# Create a scatter plot again but:
#   * Use a custom color (e.g., 'green')
#   * Set point size to 100
#   * Add a grid to the chart
#   * Add a title: "Prime Numbers Growth"
x_values = [1,2,3,4,5]
y_values = [2,3,5,7,11]
plt.scatter(x_values,y_values, color="green", s=100)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Prime Numbers Growth")
plt.grid()
plt.show()

# ==========================================
# Exercise 6: Using a Colormap
# ------------------------------------------
# Create a scatter plot with 50 points where x = range(1, 51)
# and y = [value**2 for value in x].
# Use the 'plasma' colormap and scale point colors to y.
# Add a colorbar and label it.
x = list(range(1, 51))
y = [value**2 for value in x]

plt.scatter(x,y, c=y, cmap="plasma", s=50)  
#c=y decides the color of each dot. tells color each point based on y value
#cmpa = "plasma", choose the color style 
#other cmaps are magma, autumn, turbo, cividis, virirdis, inferno, hot, spring etc
plt.colorbar(label="y = x^2")
#plt.colorbar() adds the color legend
#y=x^2 names the bar

plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Scatter Plot with Plasma Colormap")
plt.show()

# ==========================================
# Exercise 7: Bar Chart
# ------------------------------------------
# Create two lists:
#   categories = ['Apples', 'Bananas', 'Cherries']
#   values = [10, 15, 7]
# Use plt.bar() to display a bar chart.
# Add a title and axis labels.
categories = ['apples', 'bananas', 'cherries']
values = [10,15,7]
plt.bar(categories, values)
plt.xlabel("categories")
plt.ylabel("values")
plt.title("Prices of food items")
plt.show()

# ==========================================
# Exercise 8: Loading Data with pandas
# ------------------------------------------
# Create a simple DataFrame using pandas:
#   data = {'Year': [2020, 2021, 2022, 2023], 'Sales': [150, 200, 250, 300]}
# Plot 'Year' on the x-axis and 'Sales' on the y-axis using plt.plot().
# Add appropriate labels and title.
data = {
    "Year": [2020,2021,2022,2023],
    "Sales": [150,200,250,300]
}

df = pd.DataFrame(data)
x = df["Year"]
y = df["Sales"]

plt.plot(x,y)
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Years and Sales graph")
plt.show()

# ==========================================
# Final Challenge: Combining Skills
# ------------------------------------------
# Create a list of 20 x-values (1 to 20) and their squares.
# Plot a scatter chart with:
#   * Blue points sized based on y-values
#   * A title: "Square Numbers Visualization"
#   * Axis labels and grid
#   * Use 'viridis' colormap
# Save the plot as 'squares_plot.png' using plt.savefig().
x = list(range(1,21))
y = [value**2 for value in x]
plt.scatter(x,y, c=y, cmap = "viridis", s=50)
plt.title("Square Numbers Visualization")
plt.xlabel("number")
plt.ylabel("square of number")
plt.grid()
plt.savefig("square_plot.png")
plt.show()