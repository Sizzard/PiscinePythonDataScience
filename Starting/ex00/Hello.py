
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

ft_list[1] = "World!"

y = list(ft_tuple)
y[1] = "France!"
ft_tuple = tuple(y)

ft_set.remove("tutu!")
ft_set.add("Paris!")
sorted(ft_set)

ft_dict.update({"Hello" : "42Paris!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)