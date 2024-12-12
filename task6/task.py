import json
import numpy as np


data_temp = '''{
  "температура": [
      {
      "id": "холодно",
      "points": [
          [0,1],
          [18,1],
          [22,0],
          [50,0]
      ]
      },
      {
      "id": "комфортно",
      "points": [
          [18,0],
          [22,1],
          [24,1],
          [26,0]
      ]
      },
      {
      "id": "жарко",
      "points": [
          [0,0],
          [24,0],
          [26,1],
          [50,1]
      ]
      }
  ]
}'''

data_heat = '''{
  "температура": [
      {
        "id": "слабый",
        "points": [
            [0,0],
            [0,1],
            [5,1],
            [8,0]
        ]
      },
      {
        "id": "умеренный",
        "points": [
            [5,0],
            [8,1],
            [13,1],
            [16,0]
        ]
      },
      {
        "id": "интенсивный",
        "points": [
            [13,0],
            [18,1],
            [23,1],
            [26,0]
        ]
      }
  ]
}'''

temp2heat = '''[
    ["холодно", "интенсивный"],
    ["нормально", "умеренный"],
    ["жарко", "слабый"]
]'''


def fuzzification(value, fuzzy_set):
    points = fuzzy_set["points"]
    position = next((i for i, (x, _) in enumerate(points) if value <= x), len(points))
    if position == 0:
        return 0 if value < points[0][0] else points[0][1]
    if position >= len(points):
        return points[-1][1]
    x0, y0 = points[position - 1]
    x1, y1 = points[position]
    return ((value - x0) / (x1 - x0)) * (y1 - y0) + y0


def defuzzification(control_sets, center_sets):
    max_control = max(control_sets, key=lambda x: x[0])
    center = next((cs for cs in center_sets if cs['id'] == max_control[1]), None)
    if center is None:
        return -1
    points = center["points"]
    y_value = max_control[0]
    position = next((i for i, (_, y) in enumerate(points) if y_value <= y), len(points))
    if position == 0:
        return points[0][0]
    x0, y0 = points[position - 1]
    x1, y1 = points[position]
    return ((y_value - y0) / (y1 - y0)) * (x1 - x0) + x0


def solve(temperature_data: dict, heat_data: dict, rules: dict, temperature: float):
    fuzzified_values = [
        (fuzzification(temperature, C), C["id"]) for C in temperature_data
    ]
    
    transformed_values = [
        (fuzz_value[0], rule[1]) for fuzz_value in fuzzified_values for rule in rules if fuzz_value[1] == rule[0]
    ]
    
    return defuzzification(transformed_values, heat_data)


def main(temperature_json: str, heat_json: str, t2h_json: str, temperature: float):
    temperature_data = json.loads(temperature_json)['температура']
    heat_data = json.loads(heat_json)['температура']
    rules = json.loads(t2h_json)
    
    result = solve(temperature_data, heat_data, rules, temperature)
    print(result)


if __name__ == "__main__":
    main(data_temp, data_heat, temp2heat, 10)
    main(data_temp, data_heat, temp2heat, 20)
    main(data_temp, data_heat, temp2heat, 22)
    main(data_temp, data_heat, temp2heat, 19)
    main(data_temp, data_heat, temp2heat, 30)