import csv
from pathlib import Path

from statistics import mean

path = Path('sandusky_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
targeted_dates = ["18", "19", "20", "21", "22"]
highs, lows, prcp = [], [], []
year = 2012
while year != 2023:
    for row in reader:
        date = (row[header_row.index("DATE")])
        if f"{year}" in date and "-07-" in date[4:] and date[8:] in targeted_dates \
                and row[header_row.index("STATION")] == "USW00014846":
            high = (row[header_row.index("TMAX")])
            low = (row[header_row.index("TMIN")])
            rain = (row[header_row.index("PRCP")])
            highs.append(high)
            lows.append(low)
            prcp.append(rain)

    path = Path('merge-csv.com__680906033774b.csv')
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    w_dir, w_spd = [], []
    d_arv, s_arv = [], []
    day = 18

    cntn = True
    while cntn:
        day += 1
        for row in reader:
            time = row[0]

            try:
                ws_avr = float(row[7])
                wd_avr = float(row[6])

            except ValueError:
                pass
            if F"{year}" in time:

                if f"{day}" in time[8:10]:
                    d_arv.append(wd_avr)
                    s_arv.append(ws_avr)
        w_dir.append(mean(d_arv))
        w_spd.append(mean(s_arv))
        if day == 22:
            cntn = False

    print(F"{year}'s weather data: {"Highs:", highs, "Lows:", lows, "Rain:", prcp}")
    year +=1




