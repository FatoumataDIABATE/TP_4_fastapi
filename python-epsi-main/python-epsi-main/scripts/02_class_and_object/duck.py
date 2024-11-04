def fct():
    try:
        1/10
    except ZeroDivisionError as e:
        print("error", e)
    finally:
        print("Everything is done")
    print("Done")


# fct()

class CriticalException(Exception):
    # def __init__(self, *args):
    #     super().__init__(args)
    pass

class FSError(CriticalException):
    pass

class FormValidationError(Exception):
    pass

try:
    # pass # doing something here that raise exception
    raise FormValidationError("")
except CriticalException as e:
    print(e)
except FormValidationError | RuntimeError as e:
    print(e)



