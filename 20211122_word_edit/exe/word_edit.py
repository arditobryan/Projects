import json

with open('names.json') as f:
    names = json.load(f)
names

replacements_list = list()
for a, b in enumerate(names):
    replacements_list.append(names[b])
replacements_list

from docx import Document

doc_list = ['DICHIARAZIONE di non rinuncia.docx', 'informativa di mediazione.docx', 'POA.docx']
for doc_name in doc_list:
    for replacements in replacements_list:
        doc = Document(doc_name)
        for paragraph in doc.paragraphs:
            for key in replacements:
                paragraph.text = paragraph.text.replace(key, replacements[key])
        doc.save('generated/'+doc_name.split('.')[0] + ' ' + replacements['%nome%'] + '.docx')