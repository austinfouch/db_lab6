from pymongo import MongoClient
import json

client = MongoClient('mongodb://user:password@ds243049.mlab.com:43049/cmps364')

things = client.cmps364.things

num = things.count({})
if num == 0:
	with open('data.json', 'r') as seed:
  		data = seed.read()

	documents = json.loads(data)
	things.insert_many(documents)

num = things.count({})
print("Working with ", num, "things")


# Example - Print the names of all things over $40
pipeline = [
    {'$match': {'price': {'$gte': 40}}},
    {'$project': {'_id': 0, 'name': 1} }
    ]
    
results = things.aggregate(pipeline)

for i, thing in enumerate(results):
	print(str(i).rjust(4), thing['name'])
print("-"*80)

##############################################################################################
#  For each of the 5 problems below, please make sure you structure your output documents
#  so the code I've provided will print.  It's critical that your output is done with the
#  output commands I've provided - although you can add / alter printouts while debugging.
##############################################################################################

# Problem 1:  List the names of every digital item that is less than or equal to $10 and 
#			  has an average rating of 4 or greater.
#			  Output documents should have 'name' and 'average_rating' properties
# Hint:  	  You can't use $avg in the match stage, only group and project stages.
pipeline = [{'$match':{'price':{'$lte':10}}},{'$project':{'_id':0, 'name':1, 'average_rating':{'$avg':'$ratings'}}},{'$match':{'average_rating':{'$gte':4}}}]
    
results = things.aggregate(pipeline)

print("-"*80)
print('Problem 1 Results')
print("-"*80)
for i, thing in enumerate(results):
	print(str(i).rjust(4), thing['name'], " - Average rating = ", thing['average_rating'])
print("-"*80)



# Problem 2:  List the highest rating for each item
# Hint: 	  https://docs.mongodb.com/manual/reference/operator/aggregation/max/
pipeline = [{'$project':{'_id':1, 'name':1, 'max_rating':{'$max':'$ratings'}}}]
    
results = things.aggregate(pipeline)

print("-"*80)
print('Problem 2 Results')
print("-"*80)
for i, thing in enumerate(results):
	print(str(i).rjust(4), thing['name'].ljust(20), " - Max Rating = ", thing['max_rating'])
print("-"*80)



# Problem 3:  List average maximum rating for each category
# 			  For example, if there are 5 toys, you are averaging 5 maximum ratings, one from each toy

pipeline = [{'$unwind':'$category'},{'$group':{'_id':'$category','avg_max_rating':{'$avg':{'max':'$ratings'}}}}]
    
results = things.aggregate(pipeline)

print("-"*80)
print('Problem 3 Results')
print("-"*80)
for i, thing in enumerate(results):
	print(str(i).rjust(4), thing['_id'].ljust(20), " - Avg Max Rating = ", thing['avg_max_rating'])
print("-"*80)



# Problem 4:  For each item, output the number of 5 star ratings it has received.
# Hint:  	  You can group by the concatenation of two fields by constructing an object for the value
#             of _id...  {_id: {a: $field1, b: $field2}}

#pipeline = [{'$group':{'_id':{'name':'$name', {'$match':{'$ratings':{'$gte':5}}}, '$count':{'$ratings':5}}}}]
    
#results = things.aggregate(pipeline)

print("-"*80)
print('Problem 4 Results')
print("-"*80)
#for i, thing in enumerate(results):
#	print(str(i).rjust(4), thing['_id']['name'].ljust(20), thing['count'])
print("-"*80)



# Problem 5:  Find the worst rated item in each category, by average rating
# Hint:       This one is tough... Try first calculating the average rating for each
#             item, and then sort the result by average rating.
#             https://docs.mongodb.com/manual/reference/operator/aggregation/sort/#pipe._S_sort
#		
#		      Once sorted, you can group by category, using $first
#		      https://docs.mongodb.com/manual/reference/operator/aggregation/first/

pipeline = []
    
results = things.aggregate(pipeline)

print("-"*80)
print('Problem 5 Results')
print("-"*80)
#for i, thing in enumerate(results):
#	print(str(i).rjust(4), thing['_id'].ljust(20), "-", thing['name'].ljust(20), thing['average_rating'])
print("-"*80)