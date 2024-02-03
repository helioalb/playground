from file_two import function_three

print(f"__name__ no file_one.py está definido como: {__name__}")

def function_one():
  print('Função um é executada')

def function_two():
  print('Função dois é executada')

if __name__ == '__main__':
  print('file_one.py executado quando rodou diretamente')
  function_two()
  function_three()
else:
  print('file_one.py executado ao ser importado')
