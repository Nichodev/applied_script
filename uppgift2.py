# name = " aNnA kARlsSon "
# username = name.replace("aNnA kARlsSon", "Anna-Karlsson")

# print(username)

list = ("apples" , "oranges" , "bananas" , "milk" , "wheat")
print(list[0:3])
print(list[3:5])
print(list[::2])

movies = ["Inception" , "The matrix" , "Interstellar", "The prestige"]
movies.append("Momento")
movies[1] = "LOTR"
movies.remove("The prestige")
movies.insert(1, "The dark knight")

print(movies)