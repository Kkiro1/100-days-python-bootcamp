def format_name(f_name, l_name):
    """Takes first and last name to format them into one full name

    Args:
        f_name (str): A string representing first name
        l_name (str): A string representing last name

    Returns:
        str: full name formatted
    """
    if f_name == "" or l_name == "":
        return "You did not provide any name."
    full_name = f_name + " " + l_name
    return full_name.title()

print(format_name("john", "doe"))
# print(format_name(input("What's your first name? "), input("What's your last name? ")))


def function1(text):
    return text + text


def function2(text):
    return text.title()

print(function2(function1("hello")))