from . import dialog as d

def home() -> int:
  menu = d.Menu(
    'Sair',
    header='Por favor, selecione uma opção abaixo:')

  return menu.show()

