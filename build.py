print('combining html files')

top = open('templates/top.html').read()

contents = open('contents/aboutme.html').read()

contents2 = open('contents/education.html').read()

contents3 = open('contents/inclass.html').read()

contents4 = open('contents/funfacts.html').read()

bottom = open('templates/bottom.html').read()


combined_html = top + contents + bottom 
open('docs/built_file.html', 'w+').write(combined_html)


combined_html_education = top + contents2 + bottom
open('docs/built_file_education.html', 'w+').write(combined_html_education)


combined_html_inclass = top + contents3 + bottom
open('docs/built_file_inclass.html', 'w+').write(combined_html_inclass)


combined_html_funfacts = top + contents4 + bottom
open('docs/built_file_funfacts.html', 'w+').write(combined_html_funfacts)

