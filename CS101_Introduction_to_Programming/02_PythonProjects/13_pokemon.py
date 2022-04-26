class Pokemon:
  def __init__(self, input_name, input_type, input_level):
    self.name = input_name
    self.type = input_type
    self.level = input_level

  def __repr__(self):
    description = "{} is a level {} {}-type pokemon.".format(self.name, self.level, self.type)
    return description

  def level_up(self):
    self.level += 1
  
  def change_name(self, new_name):
    self.name = new_name
    print("The pokemon's new name is {}.".format(self.name))

  def change_type(self, new_type):
    self.type = new_type
    print("The pokemon's new type is {}.".format(self.type))

class Trainer:
  def __init__(self, input_name, input_pokeball, input_potion):
    self.name = input_name
    self.pokeball = input_pokeball
    self.potion = input_potion
  
  def __repr__(self):
    description = "Trainer {} has {} pokeball(s) and {} potion(s).".format(self.name, self.pokeball, self.potion)
    return description
  
  def buy_pokeball(self):
    self.pokeball += 1
  
  def use_pokeball(self):
    if self.pokeball > 0:
      print("{} used the pokeball!".format(self.name))
      self.pokeball -= 1
    else:
      print("You are out of pokeball!")

  def buy_potion(self):
    self.potion += 1

# Create instances
pokemon_a = Pokemon("Charmander", "Fire", 7)
pokemon_b = Pokemon("Squirtle", "Water", 5)
trainer_a = Trainer("Bob", 8, 2)
trainer_b = Trainer("Jake", 1, 3)

# Print instances
print(pokemon_a)
print(pokemon_b)
print(trainer_a)
print(trainer_b)

# TODO: Methods where both classes can interact with each other
