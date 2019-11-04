from jinja2 import Environment, FileSystemLoader, select_autoescape
import json


with open('caps.json', encoding='utf-8') as file:
    caps = json.load(file)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(caps=caps)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)
