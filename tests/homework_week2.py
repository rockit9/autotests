import argparse
import os
import tempfile
import json
from collections import OrderedDict


def main():
    finish = {}
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type=str)
    parser.add_argument("--val", type=str, nargs='*')
    parsed = parser.parse_args()
    result = OrderedDict(vars(parsed))

    # Check if entered value and key - open a file and write this data as json
    if result['val'] is not None:
        finish.update({result['key']:result['val']})
        with open(storage_path, 'w') as f:
            f.write(json.dumps(finish))
            print("Key and values have been recorded sucessfully")
    # Check if entered only key - read JSON file and try to retrieve values.
    # In case key doesn't exist - print error message
    elif result['val'] is None:
        with open(storage_path, 'r') as f:
            test = (json.loads(f.read()))
            key = result['key']
            if result['key'] in test:
                print("The values in storage are " + str(test[key]))
            elif result['key'] not in test:
                print("No such key in storage yet")


if __name__ == "__main__":
    main()
