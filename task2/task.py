import json
import math

input = '''
{
    "nodes":{
        "1": ["2", "3"],
        "2": [],
        "3": ["5", "4"],
        "4": [],
        "5": []
    }
}
'''

input1 = '''
{
    "nodes":{
        "1": ["2"],
        "2": ["3", "4"],
        "3": [],
        "4": ["5", "6"],
        "5": [],
        "6": []
    }
}
'''

class Tree:
    map_representation = {}
    parents = {}

    task2_result = {}
 
    def __init__(self, input) -> None:
        data = json.loads(input)
        data = data["nodes"]
        for key, val in data.items():
            self.map_representation[int(key)] = list(map(int, val.copy()))
            self.parents[int(key)] = []
        
        for key, val in self.map_representation.items():
            for obj in val:
                self.parents[obj].append(key)

        def count_kids(key):
            ans = 0
            for child in self.map_representation[key]:
                ans += count_kids(child)
            return ans + len(self.map_representation[key])
        
        def count_parents(key):
            ans = 0
            for parent in self.parents[key]:
                ans += count_parents(parent)
            return ans + len(self.parents[key])

        for key, val in self.map_representation.items():
            self.task2_result[key] = [0]*5
            self.task2_result[key][0] = len(val)
            self.task2_result[key][1] = len(self.parents[key])
            self.task2_result[key][2] = count_kids(key) - len(val)
            self.task2_result[key][3] = count_parents(key) - len(self.parents[key])
            for parent in self.parents[key]:
                self.task2_result[key][4] += (len(self.map_representation[parent]) - 1)

def main(var: str):
    tree = Tree(var)
    print(tree.task2_result)

if __name__ == "__main__":
    main(input1)