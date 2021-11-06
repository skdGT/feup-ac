def parse_date(date):
    year = int(str(date)[0:2])
    month = int(str(date)[2:4])
    day = int(str(date)[4:6])
    return year, month, day


def parse_client_dates(df):
    birth_day = []
    birth_month = []
    birth_year = []
    genders = []

    for birth_number in df["birth_number"]:
        year = int(str(birth_number)[0:2])
        month = int(str(birth_number)[2:4])
        day = int(str(birth_number)[4:6])
        # check if the client is female or male
        if month > 12:
            genders.append("Female")
            month = month - 50
        else:
            genders.append("Male")

        birth_day.append(day)
        birth_month.append(month)
        birth_year.append(year)

    # Add the new columns to the dataframe
    df["birth_day"] = birth_day
    df["birth_month"] = birth_month
    df["birth_year"] = birth_year
    df["gender"] = genders

    # Drop the unnecessary column
    df = df.drop(columns="birth_number", axis=1)
    return df
