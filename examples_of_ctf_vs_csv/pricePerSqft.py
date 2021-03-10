import csv 

# a program that computes the price per square foot of sacramento real estate transactions 
# and outputs them to a csv file

with open('Sacramentorealestatetransactions.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter = ',')
    header = next(reader)



    with open("price_per_sqft.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for row in reader:
            if(int(row[6]) == 0): # if the sqft is listed as zero just put the home price to avoid division by zero 
                pricePerSqFoot = int(row[9])
            else:
                pricePerSqFoot = int(row[9]) / int(row[6])
            
            writer.writerow([pricePerSqFoot]) 
