import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://root:example@localhost:27017/?authMechanism=DEFAULT")
db = client["reprograma"]
mycol = db["Pet"]

cats = mycol.find({
  "type": "cat"
})

cat_list = []
for cat in cats:
    newCat = {
        "name": cat["name"],
        "bride": cat["bride"],
        "weight": str(cat["weight"]) + " kg"
    }
    cat_list.append(newCat)

for cat in cat_list:
    print(cat)
