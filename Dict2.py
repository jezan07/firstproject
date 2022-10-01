sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample =["name", "salary"]

for key in sample:
    sample_dict.pop(key)

print(sample_dict)
