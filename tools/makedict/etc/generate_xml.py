import sys

from jinja2 import Template


xml_template = Template(u"""
<wordlist>
{% for word in words %}<w f="254">{{ word.word }}</w> 
{% endfor %}
</wordlist>
""")

if __name__ == '__main__':
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    input_file = open(input_file_name)
    
    words = []

    for line in input_file:
        word = line.decode('utf-8').strip()
        words.append({'word': word})

    open(output_file_name, 'w').write(xml_template.render(words=words).encode('utf-8'))
