


r=['erfer', "34", 'deswd']
text = ['34', 'd34', '345']

def fire(text):
    for item in text:
        if item[0] == '3':
            print('мы нашли элемент 3')
        elif item[0] == 'd':
            print('мы нашли элемент d')
        else:
            print('мы нашли элемент который не подходит под условия')


data = [
    {"name": "Alex", "age": 25, "job": "dev"},
    {"name": "Max", "age": 36, "job": "front"},
    {"name": "Maximka", "age": 19, "job": "front"}
]

def getData(dataList):
    for element in dataList:
        if element['name'] == "Alex":
            print("привет Алекс")
        elif element['age'] > 27:
            print(f'уважаемый {element["name"]} вам уже {element["age"]} лет вы нам не подходите')
        if element['job'] == "dev":
            print("Пока")
if __name__=="__main__":
    
    fire(text)
  