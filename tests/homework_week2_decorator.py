import json

def to_json(func):
    print("Hello above the func")

    def wrapped():
        result = json.dumps(func())
        print(type(result))
        return result
    return wrapped

@to_json
def get_data():
    x = {"my_first":"decorator"}
    return print(x)


if __name__ == "__main__":
    get_data()