class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type):
        self.type = type


class EventSet:
    def __init__(self, value):
        self.value = value
        self.type = type(value)


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        #print("Null Handler")
        if self.__successor is not None:
            #print("Move next")
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        #print("Int Handler")
        if event.type.__name__ == "int":
            #print("It is int")
            if isinstance(event, EventGet):
                #print("Event Get")
                return obj.integer_field
            elif isinstance(event, EventSet):
                #print("Event Set")
                obj.integer_field = event.value
            else:
                print("Wrong Event")
        else:
            #print("Next handler")
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        #print("Float Handler")
        if event.type.__name__ == "float":
            #print("It is float")
            if isinstance(event, EventGet):
                #print("Event Get")
                return obj.float_field
            elif isinstance(event, EventSet):
                #print("Event Set")
                obj.float_field = event.value
            else:
                print("Wrong Event")
        else:
            #print("Next handler")
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        #print("Str Handler")
        if event.type.__name__ == "str":
            #print("It is str")
            if isinstance(event, EventGet):
                #print("Event Get")
                return obj.string_field
            elif isinstance(event, EventSet):
                #print("Event Set")
                obj.string_field = event.value
            else:
                print("Wrong Event")
        else:
            #print("Next handler")
            return super().handle(obj, event)


class Chain:
    def __init__(self):
        self.chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

    def handle(self, obj, event):
        return self.chain.handle(obj, event)


if __name__ == '__main__':
    obj = SomeObject()

    Chain.handle(obj, EventGet(int))

    #chain = Chain()

    #print(chain.handle(obj, EventGet(int)))
    #print(chain.handle(obj, EventGet(float)))
    #print(chain.handle(obj, EventGet(str)))
    #print(chain.handle(obj, EventSet(1)))
    #print(chain.handle(obj, EventSet(1.1)))
    #print(chain.handle(obj, EventSet("str")))
    #print(chain.handle(obj, EventGet(int)))
    #print(chain.handle(obj, EventGet(float)))
    #print(chain.handle(obj, EventGet(str)))