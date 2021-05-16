import numpy
from . import dialog as d
from ..helper.img import import_image

__success_dialog = d.Dialog(
  'A operação foi concluída com sucesso!',
  header='Sucesso'
)

__failure_dialog = d.Dialog(
  'Não foi possível concluir a operação.',
  header='Fracasso'
)

def home() -> int:
  menu = d.Menu(
    'Sair',
    'Recomeçar',
    header='Por favor, selecione uma opção abaixo:')

  return menu.show()

def load() -> numpy.ndarray:
  path = d.Input(
    'Insira abaixo o endereço da imagem.',
    header='Importação',
    input_title='Endereço'
  ).show()

  result = import_image(path)
  if result is None:
    __failure_dialog.show()
    return load()
  else:
    __success_dialog.show()
    return result
