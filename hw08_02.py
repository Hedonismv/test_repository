#Создать универсальны декоратор, которы меняет
#порядок аргументов в функции на противоположны .

def u_decorator(func):
    def reverse_f(*args):
        list = []
        for w in args:
            list.append(w)
        list.reverse()
        print(list)
    return reverse_f

@u_decorator
def unif(*args):
    print(args)

unif('adadad','2324234',1,12,24,787)
