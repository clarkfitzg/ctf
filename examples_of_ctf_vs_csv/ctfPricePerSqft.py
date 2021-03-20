import ctf

# a program that computes the price per square foot of sacramento real estate transactions 
# and outputs them to ctf 

reader = ctf.reader('Sacramentorealestatetransactions.ctf'):

writer = ctf.writer("price_per_sqft.ctf"):


# as you can see I am using the index of row, i.e row[6], but how would ctf handle it? Same way? 

for row in reader:
    if(int(row[6]) == 0): # if the sqft is listed as zero just put the home price to avoid division by zero 
        pricePerSqFoot = int(row[9])
    else:
        pricePerSqFoot = int(row[9]) / int(row[6])
    
    writer.writerow(pricePerSqFoot) 
