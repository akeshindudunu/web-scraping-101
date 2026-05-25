#convert string to numeric(eg:"Three" to 3)
def convert(df, column):
    # Map the words to numbers and assign it BACK to the column
    mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df[column] = df[column].replace(mapping)
    return df

#convert string to boolean
def convert_to_boolean(df, column):
    mapping = {"In": True, "Out": False}
    df[column] = df[column].replace(mapping)
    return df