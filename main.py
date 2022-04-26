from datetime import datetime


def create_dec_logger(path=''):
    def logger(func):
        def new_func(*args, **kwargs):
            call_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            name = func.__name__
            result = func(*args, **kwargs)
            entry = f'{call_time}: name "{name}", args "{args}", kwargs "{kwargs}, result "{result}"'
            if path:
                with open(path, 'a') as f:
                    f.write(entry + '\n')
            else:
                print(entry)
            return result
        return new_func
    return logger


@create_dec_logger('test.txt')
def test(*args, **kwargs):
    print('Hi')
    return False


test(1, 2, c=2, d=3)
