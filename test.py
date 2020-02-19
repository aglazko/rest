def validAnimalObject(animalObject):
    if ("name" in animalObject and "price" in animalObject and "id" in animalObject
            and "center_id" in animalObject and "age" in animalObject and "species" in animalObject):
        return True
    else:
        return False


valid_object = {
    'id': 236,
    'center_id': 96,
    'name': 'zu',
    'age': 3,
    'species': 'cat',
    'price': 590
}
missing_name = {
    'id': 236,
    'center_id': 96,
    'age': 3,
    'species': 'cat',
    'price': 590
}
missing_id = {
    'center_id': 96,
    'name': 'zu',
    'age': 3,
    'species': 'cat',
    'price': 590
}