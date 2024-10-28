import json
import numpy as np


json_string = '''
{
    "objects":{
        "A": [1,[2,3],4,[5,6,7],8,9,10],
        "B": [[1,2],[3,4,5],6,7,9,[8,10]],
        "C": [3,[1,4],2,6,[5,7,8],[9,10]]
    }
}
'''

json_string_A = '[1,[2,3],4,[5,6,7],8,9,10]'
json_string_B = '[[1,2],[3,4,5],6,7,9,[8,10]]'
json_string_C = '[3,[1,4],2,6,[5,7,8],[9,10]]'


class Task:
    data = {}
    np_data = {}
    T_np_data = {}

    def __init__(self):
        pass
    
    def add_object(self, order: list, name: str):
        new_data = {}
        all_objects = []
        for i in order:
            if type(i) is list:
                for a in i:
                    all_objects.append(a)
            else:
                all_objects.append(i) 

        all_objects = set(all_objects)

        for obj in all_objects:
            new_data[obj] = {}

        for obj in all_objects:
            found = False
            for i in order:
                if type(i) is list:
                    if obj in i:
                        found = True
                        for a in i:
                            new_data[obj][a] = int(True)
                    else:
                        for a in i:
                            new_data[obj][a] = int(not found)
                else:
                    new_data[obj][i] = int(not found)
                    if obj == i:
                        found = True

        for key, d in new_data.items():
            new_data[key] = {key: d[key] for key in new_data.keys()}
        array_data = np.array([[new_data[i][j] for j in new_data[i].keys()] for i in new_data.keys()])
        self.data[name] = new_data
        self.np_data[name] = array_data
        self.T_np_data[name] = array_data.T
        
    def recreate_from_matrix(self, data_matrix: dict):
        sums = {key: sum(val.values()) for key, val in data_matrix.items()}
        sums = dict(sorted(sums.items(), key=lambda item: item[1]))
        
        result = []
        first_key = next(iter(sums))
        temp = [first_key]
        t = sums[first_key]
        for key, val in sums.items():
            if key == first_key:
                continue
            if val != t:
                if len(temp) > 1:
                    result.append(temp)
                else:
                    result.append(temp[0])
                temp = []
            temp.append(key)
            t = val
        if len(temp) > 1:
            result.append(temp)
        else:
            result.append(temp[0])
        return result
        
    def arrange(self, obj1: str, obj2: str):
        if self.data[obj1].keys() != self.data[obj2].keys():
            return None
        
        Y_12 = self.np_data[obj1]*self.np_data[obj2]
        Y_T_12 = self.T_np_data[obj1]*self.T_np_data[obj2]
        result = np.logical_or(Y_12.astype(bool), Y_T_12.astype(bool)).astype(int)
        result = {}

        i = 0
        for key1 in self.data[obj1].keys():
            result[key1] = {}
            j = 0
            for key2 in self.data[obj1].keys():
                result[key1][key2] = int(Y_12[i][j])
                j += 1
            i += 1
        return result

def main(input1: str, input2: str):
    data_A = json.loads(input1)
    data_B = json.loads(input2)
    task = Task()
    task.add_object(data_B, 'B')
    task.add_object(data_A, 'A')
    
    ans = task.arrange('A', 'B')
    print(task.recreate_from_matrix(ans))


if __name__ == "__main__":
    main(json_string_A, json_string_C)
