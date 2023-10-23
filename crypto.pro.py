import string
alpha = string.ascii_lowercase
alphabet=str(alpha)
#print(alphabet)
Hint = "qmjztgfkpwlsboxncryevhiadu"

def dec(code):
    massage = ''
    for i in code:
        if i == ' ':
            massage += ' '
        else:
            massage += alphabet[(Hint.find(str(i)))]

    return massage


code=input()
print(dec(code))
