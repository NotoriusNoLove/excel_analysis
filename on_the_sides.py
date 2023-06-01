import numpy as np
import pandas as pd
import plotly as plt


df = pd.read_excel("data.xlsx", sheet_name="Data Tables")


def target_income(df: classmethod, year: int):
    return round(sum(df[df['Year'] == year]['Target Income']))


def real_income(df: classmethod, year: int):
    return round(sum(df[df['Year'] == year]['Income']))


def income_percent(df: classmethod, year: int):
    df = df[df['Year'] == year]

    df_sum = df.agg({"Counts": "sum"})
    df_percents = df.groupby(["Income sources"]).agg(
        {"Counts": "sum"}).div(df_sum).mul(100).round()
    df_counts = df.groupby(["Income sources"]).agg({"Counts": "sum"})

    return pd.concat([df_percents, df_counts], axis=1)


def get_b2b_and_b2c(df: classmethod, year: int):
    df_b2b = df[df['Marketing Strategies'] == "B2B"]['Income'].sum().round()
    df_b2c = df[df['Marketing Strategies'] == "B2C"]['Income'].sum().round()
    # b2b_percent = round(df_b2b/(df_b2c + df_b2b)*100)
    # b2c_percent = round(df_b2c/(df_b2c + df_b2b)*100)
    return (df_b2b, df_b2c)


def profits_sum(df: classmethod, year: int):
    df = df[df['Year'] == 2020]['operating profit']
    return df.sum().round()


def profits_chart(df: classmethod, year: int):
    df = df[df['Year'] == 2020]
    return df[['Month', 'operating profit']].groupby('Month').sum().round().sort_values(by='operating profit', ascending=False)
