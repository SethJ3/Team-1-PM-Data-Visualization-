import csv
from datetime import datetime
from pathlib import Path
from plotly.subplots import make_subplots
from data_info import getting_weather_data

year = input(F"What year wdo you want to see? (2012-2022)")
year = int(year)
targeted_dates = ["18", "19", "20", "21", "22"]

#y values set as y values fix
fig = make_subplots(
    rows=1, cols=4,
    subplot_titles=("Highs and lows\nIn Celcius", "Rain\nIn Inches",
                    "Wind speed\nIn Knots", "Wind direction in degrees"), shared_yaxes=False
)
fig.add_bar(x=targeted_dates, y = getting_weather_data(year)["Lows"], row=1, col=1, showlegend=False)
fig.add_bar(x=targeted_dates, y = getting_weather_data(year)["Highs"], row=1, col=1, showlegend=False)
fig.add_bar(x=targeted_dates, y = getting_weather_data(year)["Rain"], row=1, col=2, showlegend=False)
fig.add_bar(x=targeted_dates,
            y = (getting_weather_data(year)["Wind Speed"]), row=1, col=3, showlegend=False)
fig.add_bar(x=targeted_dates,
            y = (getting_weather_data(year)["Wind Direction"]), row=1, col=4, showlegend=False)
fig.update_layout(title=f"{year}'s weather data")
fig.show()
