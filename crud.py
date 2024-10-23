import sys
from shutil import copytree


def main():
    if len(sys.argv) != 1:
        print("Informe apenas o nome do novo crud a ser criado")
        sys.exit()

    crud = sys.argv[1]

    copytree("//apps//estados", "//apps//" + crud)
