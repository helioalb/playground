# fire_test.py
import fire

def assert_equals(expected : str, current : str) -> str:
  if expected == current:
    print('Ok')
  else:
    print('Fail')

def main():
  assert_equals(fire.ready(), 'Preparar')
  assert_equals(fire.aim(), 'Apontar')
  assert_equals(fire.fire(), 'Fogo')

if __name__ == '__main__':
  main()
