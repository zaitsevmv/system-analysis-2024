import json

input = '''
{
    "data":{
        "18-24": {
            "Электроника": 20,
            "Одежда": 15,
            "Книги": 10,
            "Обувь": 5
            },
        "25-34": {
            "Электроника": 30,
            "Одежда": 20,
            "Книги": 15,
            "Обувь": 10
            },
        "35-44": {
            "Электроника": 25,
            "Одежда": 25,
            "Книги": 20,
            "Обувь": 15
            },
        "45-54": {
            "Электроника": 20,
            "Одежда": 20,
            "Книги": 25,
            "Обувь": 20
            },
        "54+": {
            "Электроника": 15,
            "Одежда": 15,
            "Книги": 30,
            "Обувь": 25
            },
    }
}
'''

def H(data: dict):
    s = sum(data.values())
    return sum([p/s for p in data.values()])

def main():
    H()
    
if __name__ == "__main__":
    main()