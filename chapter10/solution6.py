'''
can you change the self parameter 
inside a class to something else (say 'Akriti').
Try changing self to 'slf' or 'Akriti' and see the effects.

'''


class Sample:
    a = "Akriti"
    def __init__(slf, name) -> None:
        slf.name = name

obj = Sample("Akriti")
# obj.a = "Kriti"


print(obj.name)