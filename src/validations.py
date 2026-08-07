def check_nulls(df):
    return {c: df.filter(df[c].isNull()).count() for c in df.columns}
