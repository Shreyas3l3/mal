
def read(input):
    return input

def eval_expr(expr):
    return expr

def print_expr(line):
    return line

def rep(input):
    return print_expr(eval_expr(read(input)))

def main():
    while True:
        try:
            user_input = input('user> ')
            print(rep(user_input))
        except EOFError:
            break

if __name__ == "__main__":
    main()            