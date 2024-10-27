from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def parse_site(url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    
    }
    # Отправляем запрос на указанный URL
    response = requests.get(url = url, headers = headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch the page"}, 500
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tables = soup.find_all(class_="t431__mobilescroll")
    result = []

    # Проходимся по каждому блоку с классом t431__mobilescroll
    for index, table in enumerate(tables):
        # Ищем два div с классами t431__data-part1 (thead) и t431__data-part2 (tbody)
        thead = table.find(class_="t431__data-part1")
        tbody = table.find(class_="t431__data-part2")

        # Извлекаем текст из найденных div и формируем JSON
        table_name = f"table{index+1}"
        
        result.append({
            "table_name": table_name,
            "thead": thead.get_text(strip=True) if thead else "",
            "tbody": tbody.get_text(strip=True) if tbody else ""
        })

    return result
    


@app.route('/parse', methods=['GET'])
def parse():
    parsed_data_obj = []
    parsed_data_obj.append(parse_site("http://abaiairport.kz/flights#!/tab/450380678-1"))
    parsed_data_obj.append(parse_site("http://abaiairport.kz/flights/kz#!/tab/468050120-1"))
    parsed_data_obj.append(parse_site("http://abaiairport.kz/flights/en#!/tab/456376627-1"))
    return jsonify(parsed_data_obj)



@app.route('/parse_main', methods=['GET'])
def parse_main():
    parsed_data_obj = []
    parsed_data_obj.append(parse_site("http://abaiairport.kz/main/#!/tab/449025926-1"))
    parsed_data_obj.append(parse_site("http://abaiairport.kz/main/kz#!/tab/456385630-1"))
    parsed_data_obj.append(parse_site("http://abaiairport.kz/main/en#!/tab/456290301-1"))
    return jsonify(parsed_data_obj)


if __name__ == '__main__':
    app.run(debug=True,host = "0.0.0.0", port = 8003)

