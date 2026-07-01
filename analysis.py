import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

train = pd.read_csv("data/DailyDelhiClimateTrain.csv")
test = pd.read_csv("data/DailyDelhiClimateTest.csv")
df = pd.concat([train, test], ignore_index=True)
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df = df.drop_duplicates(subset=["date"])


conn = sqlite3.connect("data/daily_delhi_climate.db")
df.to_sql("daily_delhi_climate", conn, if_exists="replace", index=False)


monthly_avg = pd.read_sql("""
    SElECT month, AVG(meantemp) as avg_meantemp, AVG(humidity) as avg_humidity, AVG(wind_speed) as avg_wind_speed
    FROM daily_delhi_climate
    GROUP BY month
    ORDER BY month           
                          """, conn)

yearly_trend = pd.read_sql("""
    SELECT year, AVG(meantemp) as avg_meantemp, AVG(humidity) as avg_humidity, AVG(wind_speed) as avg_wind_speed
    FROM daily_delhi_climate
    WHERE year < 2017
    GROUP BY year
                           """, conn)

extreme_days = pd.read_sql("""
    SELECT date, meantemp, humidity, wind_speed
    FROM daily_delhi_climate
    ORDER BY meantemp DESC
    LIMIT 10                       
                           """, conn)

# Visualisations

#Chart 1: Monthly Average Temperature/Humidity
fig, ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()
ax1.bar(monthly_avg["month"], monthly_avg["avg_meantemp"], color="tomato", alpha=0.7, label="Temp")
ax2.plot(monthly_avg["month"], monthly_avg["avg_humidity"], color="blue", marker="o", label="Humidity")
ax1.set_xlabel("Month")
ax1.set_ylabel("Average Temperature (°C)")
ax2.set_ylabel("Average Humidity (%)")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.title("Monthly Average Temperature and Humidity")
plt.savefig("charts/monthly_avg_temp_humidity.png")

#Chart 2: Yearly Trend of Temperature/Humidity
plt.figure(figsize=(8,5))
plt.plot(yearly_trend["year"], yearly_trend["avg_meantemp"], color="tomato", marker="o", label="Temp")
plt.title("Delhi Yearly Average Temperature Trend")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.savefig("charts/yearly_avg_temp_trend.png")

#Chart 3: Correlation Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Climate Variables")
plt.tight_layout
plt.savefig("charts/correlation_heatmap.png")

