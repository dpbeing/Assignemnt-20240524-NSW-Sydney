import json


def save_data_as_json(df, file_path):
    """
    Save the transformed data as a JSON file.

    :param employees: List of Employee objects.
    :param file_path: Path to the JSON file.
    :return: None
    """
    
    
    # Convert Dataframe to dictonoary
    data_dict = df.to_dict(orient='records')

    # Write the dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    print(f"Data successfully saved to '{file_path}'")
