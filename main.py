#==========[Local Libraries]==========
#-----[Terminal Interface]-----
import src.cli.menu as menu

#==========[Main Function]==========
def main():
  img_original = menu.load()

  while True:
    selection = menu.home()

    if selection == 0:
      break

#==========[Script Initializer]==========
if __name__ == "__main__":
  main()
