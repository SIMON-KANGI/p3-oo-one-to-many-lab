class Pet:
    all=[]
    PET_TYPES=["dog", "cat", "rodent", "bird", "reptile",'exotic']
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self._owner=owner
        Pet.all.append(self)
        self.type = pet_type
     
    @property
    def owner(self):
             return self._owner
    @owner.setter
    def owner(self,owner):
        self._owner = owner
    @property
    def type(self):
        return self.pet_type
    @type.setter
    def type(self,pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("pet_type not valid")
        self._pet_type = pet_type
    def __lt__(self, other):
        return self.name < other.name   

class Owner:
    def __init__(self,name):
        self.name = name
        #self.add_pet =None
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner ==self]
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("pet must be of type Pet")
        pet.owner=self
           
            
    def get_sorted_pets(self):
        return sorted(Pet.all)
    
    
    Simon=Pet("Simon","bird")
    
