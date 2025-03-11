def NULL_not_found(object: any) -> int:

    ft_dict = {
        type(None): "Nothing: None",
        float: f"Cheese: {object}",
        int: f"Zero: {object}",
        str: "Empty:",
        bool: f"Fake: {object}",
    }
    if object != "" and type(object) is str:
        print("Type not Found")
        return 1
    else:
        print(f"{ft_dict[type(object)]} {type(object)}")
    
    return 0