import csv
from datetime import datetime
from pathlib import Path
from plotly.subplots import make_subplots

#highs is daily high, lows is daily lows, prcp is daily rain

path = Path('sandusky_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
targeted_dates = ["18", "19", "20", "21", "22"]
highs, lows, prcp = [], [], []
for row in reader:
        date = (row[header_row.index("DATE")])
        if "2012" in date and "-07-" in date[4:] and date[8:] in targeted_dates\
                and row[header_row.index("STATION")] == "USW00014846":
            high = (row[header_row.index("TMAX")])
            low = (row[header_row.index("TMIN")])
            rain = (row[header_row.index("PRCP")])
            highs.append(high)
            lows.append(low)
            prcp.append(rain)

#y values set as y values fix
fig = make_subplots(
    rows=1, cols=3,
    subplot_titles=("Highs and lows\nIn Celcius", "Rain\nIn Inches", "Wind speed and Direction\nIn Knots + Degrees"), shared_yaxes=False
)
fig.add_bar(x=targeted_dates, y=[highs,lows], row=1, col=1)
fig.add_bar(x=targeted_dates, y=prcp, row=1, col=2)
fig.show()