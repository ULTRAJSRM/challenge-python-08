import time


def finish_date(func):
    def wrapper(*args,**kwargs):

        func(*args,**kwargs)

        localtime = time.strftime('%d/%m/%Y - %H:%M:%S', time.localtime(time.time()))
        print(f'Execution finished at : {localtime}')

    return wrapper


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
