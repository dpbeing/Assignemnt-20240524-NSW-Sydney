import pandas as pd

def read_csv(file_path):
    """
    Reads a pipe-separated file and returns a Pandas DataFrame with specified column names and data types.

    :param file_path: Path to the file to be read.
    :return: DataFrame containing the file's content with specified data types.
    """
    # Define column names and data types
    column_names = [
        'FirstName', 'LastName', 'Company', 'BirthDate', 'Salary',
        'Address', 'Suburb', 'State', 'Post', 'Phone', 'Mobile', 'Email'
    ]
    column_types = {
        'FirstName': 'string',
        'LastName': 'string',
        'Company': 'string',
        'BirthDate': 'string',  # We will handle date parsing in transform part
        'Salary': 'float',
        'Address': 'string',
        'Suburb': 'string',
        'State': 'string',
        'Post': 'int',
        'Phone': 'int',
        'Mobile': 'int',
        'Email': 'string'
    }
    
    # Read the file using Pandas
    df = pd.read_csv(file_path, sep='|', names=column_names, dtype=column_types, header=None)
    #df.head(10)
    return df
