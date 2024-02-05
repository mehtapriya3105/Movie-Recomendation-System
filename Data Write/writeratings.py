import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string
db = client["movie"]  # Replace with your database name
collection = db["ratings"]  # Replace with your collection name

# Read data from the DAT file and transform it into a list of dictionaries
data_to_insert = []
id = 1

with open("C:/Users/HP/Desktop/nirma/sem 7/BDA/innovative/ml-1m/ml-1m/ratings.dat", "r") as file:  # Replace with the path to your DAT file
    for line in file:
        # Assuming that your DAT file is in a specific format (e.g., tab-separated values),
        # split each line into fields and create a dictionary
        fields = line.strip().split('::')  # Adjust the delimiter as needed
        if len(fields) >= 4:
            data_dict = {
                "_id": id,
                "UserID": fields[0],  # Replace with actual field names and indices
                "Title": fields[1],
                "Ratings": fields[2],
                "Timestamp": fields[3]
                # Add more fields as needed
            }
            data_to_insert.append(data_dict)
        id = id + 1

# Insert the data into MongoDB
if data_to_insert:
    # Insert the data into MongoDB
    result = collection.insert_many(data_to_insert)
    print("Inserted IDs:", result.inserted_ids)
else:
    print("No data to insert. The data_to_insert list is empty.")

# Check the result


# Close the MongoDB connection
client.close()
