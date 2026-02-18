TRUE  = lambda x: (lambda y: x)   # λx.λy.x
FALSE = lambda x: (lambda y: y)   # λx.λy.y
IF    = lambda c: (lambda a: (lambda b: c(a)(b)))

# Church numerals
ZERO = lambda f: (lambda x: x)                       # λf.λx.x
SUCC = lambda n: (lambda f: (lambda x: f(n(f)(x))))  # λn.λf.λx.f (n f x)
ADD  = lambda a: (lambda b: (lambda f: (lambda x: a(f)(b(f)(x))))) # λx. λy. x + y
MULT = lambda a: (lambda b: (lambda f: a(b(f))))

to_int = lambda n: n(lambda x: x + 1)(0)
