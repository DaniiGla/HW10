import json


def load_candidates():
    """Загружает данные из файла. Возвращает список из 7 объектов"""
    with open('candidates.json', 'r', encoding='utf-8') as candidates:
        raw_content = candidates.read()
        return json.loads(raw_content)


def get_all():
    """Показывает всех кандидатов"""
    candidates = load_candidates()
    str_ = ''
    for i in range(len(candidates)):
        str_ += f"<pre>Имя кандидата - {candidates[i]['name']}\nПозиция - {candidates[i]['position']}\nНавыки - {candidates[i]['skills']}\n"
    return str_


def get_by_pk(pk):
    """Возвращает кандидата по его pk"""
    internal_list = load_candidates()
    lkj = ''
    for i in internal_list:
        if i['pk'] == pk:
            #lkj += f"<img src='{i['picture']}'>\n<pre>Имя кандидата - {internal_list[i]['name']}\nПозиция - {internal_list[i]['position']}\nНавыки - {internal_list[i]['skills']}<pre>"
            lkj += f"<img src='({i['picture']})'><pre>Имя кандидата - {i['name']}\nПозиция - {i['position']}\nНавыки - {i['skills']}<pre>"
            return lkj


def get_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    internal_list = load_candidates()
    str_ = ''
    skill_n_lowered = skill_name.lower()
    for i in internal_list:
        var = i['skills'].lower().split(', ')
        if skill_n_lowered in var:
            str_ += f"<pre>Имя кандидата - {i['name']}\nПозиция - {i['position']}\nНавыки - {i['skills']}\n<pre>"
            var.clear()
        else:
            var.clear()
    return str_

