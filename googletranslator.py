from googletrans import Translator
translator = Translator()

value=translator.translate("come stai ?")
value=translator.translate("come stai ?",src='it',dest='fr')

print(value)
print(value.src)
print(value.dest)
print(value.text)
print(value.pronunciation)


