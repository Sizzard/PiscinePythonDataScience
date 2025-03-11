def all_thing_is_obj(object: any) -> int:
    if not object:
        return
    ft_dict = {
        list: "List : ",
        tuple: "Tuple : ",
        set: "Set : ",
        dict: "Dict : ",
        str: f"{object} is in the kitchen : ",
    }
    if type(object) not in ft_dict:
        print("Type not found")
    else:
        print(f"{ft_dict[type(object)]}{type(object)}")
    return 42