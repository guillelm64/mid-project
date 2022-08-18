def lower_lower_clear(df):

    df2 = df.copy()

    df2.columns = df2.columns.str.replace(' ', '_')
    df2.columns = df2.columns.str.lower()
    df2.columns = df2.columns.str.replace('#_', '')

    return df2