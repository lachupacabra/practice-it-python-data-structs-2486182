from csv import reader
from collections import namedtuple
def main():
    #add code here
    #read data/Customer.csv
    #Create workable objects with each line
    with open('data/Customer.csv','r') as file:
        read = reader(file)
        data = []
        namedtuple('Customer',next(read))
        for line in read:
            data.append(*line)
            # print(Customer(*line))
    print(data)
    return data

if __name__ == "__main__":
    main()
