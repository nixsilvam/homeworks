import functools


def list_function(f_t_d):
    @functools.wraps(f_t_d)
    def the_wrapper(x):
        f_t_d(x)
        return x.split()
    return the_wrapper


@list_function
def return_string(x):
    return x


def user_input():
    inp = input("Enter a text string: ")
    return return_string(inp)


if __name__ == '__main__':
    print(user_input())
    print(user_input.__name__)
