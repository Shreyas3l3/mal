import sexpdata
import traceback

repl_env = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b),
}    

def eval_expr(ast, env):

    if isinstance(ast, sexpdata.Symbol):
        symbol = str(ast)
        if symbol in env:
            return env[symbol]
        raise Exception(f"Symbol not found: {symbol}")
        
    
    elif isinstance(ast, list):
        if len(ast) == 0:
            return ast  
        # this becomes the lambda function
        fn = eval_expr(ast[0], env)
        # list of values
        args = [eval_expr(arg, env) for arg in ast[1:]]
        # * unpacks list of arguments
        return fn(*args)
    
    else:
        return ast 

def rep(source):
    ast = sexpdata.loads(source)          
    result = eval_expr(ast, repl_env)     
    return sexpdata.dumps(result)        

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
