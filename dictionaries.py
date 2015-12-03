#my_stats = {"name": "hilary", "age": "31", "height": "5'3"} 
#print my_stats["name"] + " is " + my_stats["age"] + " years old with a height of " + my_stats["height"]
#del my_stats["age"]
#print my_stats 

#vocabulary_words = {"integer": "a whole number", "float": "a decimal number", 
#"boolen": "a conditional stating whether it is true or false", "string": "a value within quotation marks"}
#print vocabulary_words

#full_name = raw_input("What is your full name? ")
#namedictionary = {}
#for letter in full_name:
#	if letter in namedictionary:
#		namedictionary[letter] += 1 
#	else:
#		namedictionary[letter] = 1
#print namedictionary


fish = raw_input("Give me a string!")

fishdictionary = {}
for word in fish:
	if word in fishdictionary:
		fishdictionary[word] += 1
	else:
		fishdictionary[word] = 1
print fishdictionary