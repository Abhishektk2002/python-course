import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")

print("Connected")

db=client["class"]
col=db["details"]
user=[{
    "name":"abhishek",
    "age":20,
    "adm":23,
},
{
    "name":"Rahul",
    "age":22,
    "adm":24,
}]
col.insert_many(user)
for doc in col.find({"name":{"$regex":"^R"},"age":{"$gt":22}}):
    print(doc)