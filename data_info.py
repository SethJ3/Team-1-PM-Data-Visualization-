import csv
from pathlib import Path

from statistics import mean
def getting_weather_data(year):
    #Highs Lows Rain
    path = Path('sandusky_weather_2012_2022.csv')
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)
    #filtering out the not relevant days
    targeted_dates = ["18", "19", "20", "21", "22"]
    highs, lows, prcp = [], [], []
    year = int(year)
    for row in reader:
        date = (row[header_row.index("DATE")])
        #making sure that only data from july 18th - 19th and the specified year get used
        if f"{year}" in date and "-07-" in date[4:] and date[8:] in targeted_dates \
                and row[header_row.index("STATION")] == "USW00014846":
            high = (row[header_row.index("TMAX")])
            low = (row[header_row.index("TMIN")])
            rain = (row[header_row.index("PRCP")])
            highs.append(high)
            lows.append(low)
            prcp.append(rain)
    #getting the info for wind
    path = Path('merge-csv.com__680906033774b.csv')
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    w_dir, w_spd = [], []
    #d_arv is direction average and s_arv is speed average 
    #They are used to append to w_dir and w_spd
    d_arv, s_arv = [], []
    day = 18
    for row in reader:
        time = row[0]

        try:
            ws_avr = float(row[7])
            wd_avr = float(row[6])

        except ValueError:
            pass
        # filtering relevant data
        if F"{year}" in time:
                if f"{18}" in time[8:10]:
                    d_arv.append(wd_avr)
                    s_arv.append(ws_avr)
                w_dir.append(mean(d_arv))
                w_spd.append(mean(s_arv))
                if f"{19}" in time[8:10]:
                    d_arv.append(wd_avr)
                    s_arv.append(ws_avr)
                w_dir.append(mean(d_arv))
                w_spd.append(mean(s_arv))

                if f"{20}" in time[8:10]:
                    d_arv.append(wd_avr)
                    s_arv.append(ws_avr)
                w_dir.append(mean(d_arv))
                w_spd.append(mean(s_arv))
                if f"{21}" in time[8:10]:
                    d_arv.append(wd_avr)
                    s_arv.append(ws_avr)
                w_dir.append(mean(d_arv))
                w_spd.append(mean(s_arv))
                if f"{22}" in time[8:10]:
                    d_arv.append(wd_avr)
                    s_arv.append(ws_avr)
                w_dir.append(mean(d_arv))
                w_spd.append(mean(s_arv))
        dupe= []
        dupe2 = []
        for i in w_dir:
            if i not in dupe:
                dupe.append(i)
        w_dir = dupe[:]
        for i in w_spd:
            if i not in dupe2:
                dupe2.append(i)
        w_spd = dupe2[:]
    #data info is a dict that contains data
    data_info = {
        "Highs": highs,
        "Lows": lows,
        "Rain": prcp,
        "Wind Speed": w_spd,
        "Wind Direction": w_dir
    }
    return data_info
