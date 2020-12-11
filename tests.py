
from utils import get, get_json_list_sync


def test_smoke():
    "tests if api returns something"
    text = 'продавец'
    response = get(text)
    assert response.status_code == 200, 'smoke test, bad response'


def test_response_format():
    "tests if response is in json format and contains necessary first-level fields"
    text = 'продавец'
    response = get(text)
    try:
        r_json = response.json()
    except ValueError:
        raise AssertionError('format test, response cannot be parsed as json')

    fields = set(r_json.keys())
    assert 'items' in fields, 'not items field in response'
    assert 'found' in fields, 'no found field in response'
    assert 'page' in fields, 'no page field in response'
    assert 'pages' in fields, 'no pages field in response'
    assert 'per_page' in fields, 'no per_page field in response'
    assert 'clusters' in fields, 'no clusters field in response'
    assert 'arguments' in fields, 'no arguments field in response'
    assert 'alternate_url' in fields, 'no alternate_url field in response'
    assert r_json['per_page'] == 20, 'per_page != 20'


def test_positive_ru():
    "tests response to some regular input, cyrillic"
    text = 'курьер'
    r_json = get(text).json()
    assert len(r_json['items']) > 0, f'empty items list for {text}'

def test_positive_en():
    "tests response to some regular input, latin"
    text = 'developer'
    r_json = get(text).json()
    assert len(r_json['items']) > 0, f'empty items list cor {text}'

def test_negative_abracadabra():
    "tests response to some strange input, abracadabra"
    text = 'fdkjflakjfka'
    r_json = get(text).json()
    assert len(r_json['items']) == 0, f'non-empty items list for {text}'


def test_negative_special():
    "tests response to some strange input, special"
    text = '!$8790'
    r_json = get(text).json()
    assert len(r_json['items']) == 0, f'non-empty items list for {text}'


def test_consistency():
    "tests response to some strange input, special"
    text = 'директор завода'
    r_json1 = get(text).json()
    r_json2 = get(text).json()
    assert r_json1 == r_json2, 'two consecutive requests return different results'

def test_load():
    "tests multiple consecutive requests"
    lst = [' разработчк', 'тестировщик', 'музыкант', 'клоун', 'акробат', 'скалолаз']
    try:
        results = get_json_list_sync(lst)
    except Exception as e:
        raise AssertionError(f'Load (n={len(lst)}) failed with error {e}')