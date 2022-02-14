def make_bold(fun):
    def wrapper(*args):
        return f'<b>{fun(*args)}</b>'
    return wrapper


def make_italic(fun):
    def wrapper(*args):
        return f'<i>{fun(*args)}</i>'
    return wrapper


def make_underline(fun):
    def wrapper(*args):
        return f'<u>{fun(*args)}</u>'
    return wrapper


'''
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
-----------------------------------------
<b><i><u>Hello, Peter, George</u></i></b>
'''