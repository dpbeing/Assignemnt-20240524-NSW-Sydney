from read_data import read_csv
from transform_data import transform_data

def main():
    # Read data
    raw_data = read_csv('/Users/deep/Assignemnt-20240524-NSW-Sydney/data/member-data.csv')
    # Transform data
    transformed_data = transform_data(raw_data)
    print(transformed_data)
    
if __name__ == '__main__':  
    main()