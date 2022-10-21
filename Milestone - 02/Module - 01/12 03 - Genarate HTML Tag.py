# Expected Output: <p>This is a paragraph</p>

paragraph1 = 'This is paragraph1'
paragraph2 = 'This is paragraph2'
paragraph3 = 'This is paragraph3'
paragraph4 = 'This is paragraph4'
"""
print('<p>'+'paragraph1'+'</p>')
print('<p>'+'paragraph2'+'</p>')
print('<p>'+'paragraph3'+'</p>')
print('<p>'+'paragraph4'+'</p>')
"""
"""
def html_genarator(paragraph):
    code = f'<p>{paragraph}<p>'
    return code

paragraph_code1 = html_genarator('This is paragraph1')
paragraph_code2 = html_genarator('This is paragraph2')
paragraph_code3 = html_genarator('This is paragraph3')
paragraph_code4 = html_genarator('This is paragraph4')

print(paragraph_code1)
print(paragraph_code2)
print(paragraph_code3)
print(paragraph_code4)
"""

def h2_html(heading):
    code = f'<h2>{heading.title()}<h2/>'
    return code

h2_1 = h2_html('top 10 restaurant in usa')
h2_2 = h2_html('top 10 motel in usa')
h2_3 = h2_html('top 10 place in usa')

print(h2_1)
print(h2_2)
print(h2_3)
