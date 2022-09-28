import a_PlantClass as pc

primrose = pc.Plant("Green",10)

sunflower = pc.Flower("Yellow",20)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals())
    #Cannot go from a subclass to a super class