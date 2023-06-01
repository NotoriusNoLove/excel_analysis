from on_the_sides import *


def avg_monthly_income(df: classmethod, year: int):
    df = df[df['Year'] == year]
    df = df[['Month', 'Income']].groupby('Month').sum().round()
    return df['Income'].mean().round()


def income_archive(*args, **kwargs):
    return round(real_income(*args, **kwargs)/target_income(*args, **kwargs)*100)


def second_circle(df: classmethod, year: int, income_sources: str):
    df = df[df['Year'] == year]
    df = df[df['Income sources'] == income_sources][['Income']].sum()
    return df


print(income_percent(df, 2020))
