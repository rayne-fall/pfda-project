# PFDA Project - Autumn 2024

This repository contains my project work for the Autumn 2024 Programming for Data Analytics module at Atlantic Technological University. The repository contains a Jupyter notebook as well as a Python script and CSV file.

## Contents

- [project.iynb](project.ipynb): A Jupyter notebook containing my analysis of windspeed data and windfarming in Co. Wexford.
- [hly1775.csv](hly1775.csv): A CSV file containing weather data recorded at the Johnstown Castle weather station in Co. Wexford between 12 August 2003 and 1 December 2024.
- [mean-windspeed-plot.py](mean-windspeed-plot.py): A Python script which loads the data from [hly1775.csv](hly1775.csv) and outputs a scrollable plot showing the mean daily windspeed.
- [requirements.txt](requirements.txt): A text file listing the required modules for running the Jupyter notebook and Python script.


## Running the programs

The contents of the repository can be run either locally using [Anaconda](https://www.anaconda.com/download) and [Visual Studio Code](https://code.visualstudio.com/) or online using [GitHub Codespaces](https://github.com/features/codespaces). 

### Running locally

1. Clone the repository.
1. Use Anaconda to set up the virtual environment.
1. Launch Visual Studio Code.
1. Install the modules listed in the [requirements.txt](requirements.txt) file.
1. Run the script/notebook.

### Running on GitHub Codespaces
1. Click the green "Code" button at the top of the repository page.
1. Click "Open with Codespaces".
1. Run the script/notebook in the browser.

## Known issues
1. [mean-windspeed-plot.py](mean-windspeed-plot.py) is intended to output a scrollable version of plot 4.1 from [project.iynb](project.ipynb). However, the "Previous" and "Next" buttons are currently non-functional, with the plot only able to display the first hundred datapoints as a result.

## References
1. https://www.met.ie/climate/available-data/historical-data (original source for data)
1. https://experience.arcgis.com/experience/adeb20a08bdd477082a3975b3483cce6 (map of the windfarms in Ireland)
1. https://www.seai.ie/sites/default/files/publications/energy-in-ireland-2024.pdf (SEAI's 2024 report on energy in Ireland)
1. https://stackoverflow.com/questions/75659606/to-get-trend-lines-equation-polynomial-order-2 (plotting polynomial trendline)
1. https://www.nhc.noaa.gov/gccalc.shtml (longitude/latitude distance calculator)
1. https://www.met.ie/climate/weather-observing-stations (Johnstown Castle weather station details)
1. https://www.thewindpower.net/windfarm_en_411_carnsore.php (Carnsore Point windfarm details)
1. https://www.geeksforgeeks.org/python-scroll-through-plots/ (how to make plots scrollable)
1. https://seaiopendata.blob.core.windows.net/wind/WindFarmsConnectedJune2022.csv (list of windfarms in Ireland)
1. https://data.gov.ie/dataset/wind-farms-in-ireland (explanation of cuations to be noted when referencing list of windfarms)