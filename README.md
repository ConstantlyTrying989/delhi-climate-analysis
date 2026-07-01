# 🌡️ Delhi Climate Analysis

A data analysis project exploring daily climate patterns in Delhi from 2013 to 2017; looking at how temperature, humidity, wind speed, and pressure change across seasons and years.

Built as a portfolio project to practise real-world data workflows: cleaning messy data, querying it with SQL, and communicating findings through visualisations.

---

## Descriptions of the Charts

- **Seasonal patterns** — how temperature and humidity shift month by month
- **Year-on-year trends** — whether average temperatures changed over the dataset period
- **Feature relationships** — which variables correlate with each other (e.g. does high humidity mean lower temperature?)
- **Extreme days** — the hottest days on record in the dataset

---

## Principal findings

- Delhi has a sharp seasonal cycle: temperatures peak around May–June, while humidity spikes during the monsoon months (July–September)
- Temperature and humidity are negatively correlated — the hottest months tend to be drier
- Wind speed and pressure show weaker relationships with temperature

---

## Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data loading, cleaning, transformation |
| SQLite | SQL queries on the cleaned dataset |
| Matplotlib & Seaborn | Visualisations |
| Git | Version control |

---

## Project structure

```
delhi-climate/
├── data/
│   ├── DailyDelhiClimateTrain.csv
│   └── DailyDelhiClimateTest.csv
├── charts/
│   ├── monthly_temp_humidity.png
│   ├── yearly_trend.png
│   └── correlation_heatmap.png
├── analysis.py
└── README.md
```

---

## How to run it

```bash
git clone https://github.com/ConstantlyTrying989/delhi-climate-analysis
cd delhi-climate-analysis
pip install pandas matplotlib seaborn
python analysis.py
```

Charts will be saved to the `charts/` folder.

---

## Dataset

[Daily Climate Time Series Data – Delhi](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data) via Kaggle.