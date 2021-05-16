from ..cli.dialog import Dialog

def print_basic(basic_histogram: list) -> None:
  Dialog(
    'Abaixo temos a quantidade de píxeis',
    'que possuem a mesma intensidade que',
    'o píxel requisitado, separados por cor',
    header='Histograma Básico',
  ).show()

  Dialog(
    f'Vermelho: {basic_histogram[0]} píxeis',
    f'Verde: {basic_histogram[1]} píxeis',
    f'Azul: {basic_histogram[2]} píxeis'
  ).show()
