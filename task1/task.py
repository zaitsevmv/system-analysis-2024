import json

input = '''
{
    "nodes":{
        "1": ["2"],
        "2": ["3", "4"],
        "3": ["5"],
        "4": [],
        "5": []

    }
}
'''

class Tree:
    map_representation = {}
 
    def __init__(self, input) -> None:
        data = json.loads(input)
        data = data["nodes"]
        elem_count = 0
        for key, val in data.items():
            self.map_representation[int(key)] = list(map(int, val.copy()))
            elem_count += 1
        for key, val in data.items():
            for n in val:
                self.map_representation[int(n)].append(int(key))
        for key, val in self.map_representation.items():
            s = set(val)
            val = list(s)
            self.map_representation[key] = val


def main():
    tree = Tree(input)
    print(tree.map_representation)

if __name__ == "__main__":
    main()