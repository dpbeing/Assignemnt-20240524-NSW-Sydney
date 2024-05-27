import pandas as pd
from datetime import datetime

def transform_data(df):
    """
    Transforms the input DataFrame by applying the specified transformations.
    
    :param df: DataFrame containing the raw data.
    :return: List of Employee objects with transformed data.
    """
    # Convert BirthDate to DD/MM/YYYY format
    df['BirthDate'] = pd.to_datetime(df['BirthDate'], format='%d%m%Y', errors='coerce')
    df['BirthDate'] = df['BirthDate'].dt.strftime('%d/%m/%Y')

    # Format Salary
    df['Salary'] = df['Salary'].apply(lambda x: f"${x:,.2f}")

    # Clean FirstName and LastName
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()

    # Merge FirstName and LastName into FullName
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']

    # Calculate Age as of Mar 1st, 2024
    reference_date = datetime(2024, 3, 1)
    df['Age'] = pd.to_datetime(df['BirthDate'], format='%d/%m/%Y', errors='coerce').apply(
        lambda x: reference_date.year - x.year - ((reference_date.month, reference_date.day) < (x.month, x.day))
    )

    # Add SalaryBucket
    def categorize_salary(salary):
        salary_float = float(salary.replace('$', '').replace(',', ''))
        if salary_float < 50000:
            return 'A'
        elif salary_float <= 100000:
            return 'B'
        else:
            return 'C'

    df['SalaryBucket'] = df['Salary'].apply(categorize_salary)
    df['Address'] = df.apply(lambda row: {
        'Street': row['Address'],
        'Suburb': row['Suburb'],
        'State': row['State'],
        'Post': row['Post']
    }, axis=1)
    # Drop FirstName and LastName columns
    df = df.drop(columns=['FirstName', 'LastName'])
    return df