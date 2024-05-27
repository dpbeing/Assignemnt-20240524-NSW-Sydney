from read_data import read_csv
from transform_data import transform_data
from load_data import save_data_as_json
def main():
    # Read data
    print("Reading data from CSV...")
    raw_data = read_csv('/Users/deep/Assignemnt-20240524-NSW-Sydney/data/member-data.csv')
    # Transform data
    print("Transforming data...")
    transformed_data = transform_data(raw_data)
    print(transformed_data)
    # Save data to JSON
    print("Saving data to JSON file...")
    save_data_as_json(transformed_data,'/Users/deep/Assignemnt-20240524-NSW-Sydney/data/output-data.json')

    
if __name__ == '__main__':  
    main()