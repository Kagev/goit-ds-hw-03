from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from colorama import Fore, Style
from pymongo.errors import PyMongoError

# Load environment variables
load_dotenv()
uri = os.environ.get("MONGODB_URI")

client = MongoClient(uri)
db = client['cat_database']
collection = db['cats']

def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f'Cat added with id: {result.inserted_id}')
    except PyMongoError as e:
        print(f'Error adding cat: {e}')

def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f'Error reading cats: {e}')

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print('Cat not found')
    except PyMongoError as e:
        print(f'Error finding cat: {e}')

def update_cat_age(name, new_age):
    try:
        result = collection.update_one(
            {"name": name},
            {"$set": {"age": new_age}}
        )
        if result.modified_count > 0:
            print("Cat's age updated!")
        else:
            print("Cat not found or age is the same")
    except PyMongoError as e:
        print(f'Error updating cat age: {e}')

def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one(
            {"name": name},
            {"$push": {"features": feature}}
        )
        if result.modified_count > 0:
            print("Feature added to cat!")
        else:
            print("Cat not found or feature already exists")
    except PyMongoError as e:
        print(f'Error adding feature to cat: {e}')

def delete_cat(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Cat deleted!")
        else:
            print("Cat not found")
    except PyMongoError as e:
        print(f'Error deleting cat: {e}')

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f'All cats deleted! Count: {result.deleted_count}')
    except PyMongoError as e:
        print(f'Error deleting all cats: {e}')

def menu():
    while True:
        print("\n1. Create Cat")
        print("2. Read All Cats")
        print("3. Read Cat by Name")
        print("4. Update Cat Age")
        print("5. Add Feature to Cat")
        print("6. Delete Cat")
        print("7. Delete All Cats")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter cat name: ")
            age = int(input("Enter cat age: "))
            features = input("Enter cat features (comma separated): ").split(", ")
            create_cat(name, age, features)

        elif choice == '2':
            read_all_cats()

        elif choice == '3':
            name = input("Enter cat name: ")
            read_cat_by_name(name)

        elif choice == '4':
            name = input("Enter cat name: ")
            new_age = int(input("Enter new age: "))
            update_cat_age(name, new_age)

        elif choice == '5':
            name = input("Enter cat name: ")
            feature = input("Enter new feature: ")

        elif choice == '6':
            name = input("Enter cat name: ")
            delete_cat(name)

        elif choice == '7':
            delete_all_cats()

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    menu()