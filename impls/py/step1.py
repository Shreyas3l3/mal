import sexpdata
import traceback

def eval_expr(ast):
    return ast

def rep(source):
    return sexpdata.dumps(eval_expr(sexpdata.loads(source)))

def main():
    while True:
        try:
            print(rep(input('user> ')))
        except EOFError:
            break
        except Exception as e:
            traceback.print_exception(e, limit=10)

if __name__ == "__main__":
    main()                
