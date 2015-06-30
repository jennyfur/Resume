from markdown import markdown
import pdfkit

input_filename = 'README.md'
output_filename = 'README.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

options = {
    'page-size': 'Letter',
    'margin-top': '0.25in',
    'margin-right': '0.25in',
    'margin-bottom': '0.25in',
    'margin-left': '0.25in',
    'encoding': "UTF-8",
    'no-outline': None
}

css = 'style.css'

pdfkit.from_string(html_text, output_filename, options=options, css=css)
