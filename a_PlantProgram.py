import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())
#Subclass can call the super, one way

#print(primrose.get_petals())
#This won't work becasue plant is super and can't call the subclas
