""" sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)


translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }

print(translations)

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

students_in_classes = ["philosphy"].append("marco")

print(students_in_classes)

students_in_classes["philosphy"].append("5")

print(students_in_classes)



powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
 """
my_empty_dictionary={}
print(my_empty_dictionary)
my_empty_dictionary["celulares"]=0
print(my_empty_dictionary)
my_empty_dictionary[3]=17
print(my_empty_dictionary)
////
celulares={}
celulares["samsung"]=0
print(celulares)

celulares{"iphone":1}
print(celulares)

celulares= {"nokia": 9018293, "huawei": 119238}
print(celulares)
celulares.update({"LG": 138475, "Honor": 85739})
print(celulares)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)


drinks=["expresso","chai","decaf","drip"]
caffeine=[64,48,0,120]
zipped_drinks= zip(drinks, caffeine)
drinks_to_caffeine= {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
