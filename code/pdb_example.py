def get_farm_animals():
    farm = ["cow", "pig", "goat"]
    return farm

import pdb; pdb.set_trace()  # add breakpoint
animals = ["otter", "seal"]
farm_animals = get_farm_animals()
animals = animals + farm_animals
print(animals)
