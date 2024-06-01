class Owner:
   
    all = []

    def __init__(self, name):
        self.name = name
        self.owner_pets = []
          
    def pets(self):
        return self.owner_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Not a valid pet type")
        else:
            self.owner_pets.append(pet)
            pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.owner_pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner="None"):
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self._pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)
        else:
            raise Exception
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value in Pet.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception(f"{value} is not a valid pet type")


owner1 = Owner("betty")
owner2 = Owner("alice")

pet1 = Pet("choruzo", "dog", owner1)
pet2 = Pet("chinchila", "rodent", owner2)

owner1.add_pet(pet1)
owner2.add_pet(pet2)

print(pet2.owner.name)  # Output: alice
print(owner1.get_sorted_pets())  # Output: [Pet(name=choruzo, pet_type=dog, owner=betty)]
print(owner2.get_sorted_pets())