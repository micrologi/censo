#!/usr/bin/env python
import os
import sys
from shutil import copytree
from shutil import rmtree
from shutil import copyfile


def main():

    if len(sys.argv) != 4:
        print("CRUD Generator 1.0.1.")
        print()
        print("Informe os seguintes parâmetros, na ordem que segue:")
        print()
        print(" 1) Nome do CRUD (Plural, minusculo). Ex.: estados")
        print(" 2) Nome do módulo (Plural, primeira letra). Ex.: Estados")
        print(" 3) Nome do modelo (Singular, primeira letra). Ex.: Estado")
        sys.exit()

    dic = {
        "<<crud>>": sys.argv[1],
        "<<module>>": sys.argv[2],
        "<<model>>": sys.argv[3],
    }

    print("Gerando arquivos do crud")
    copytree("./apps/crud", "./apps/" + dic.get("<<crud>>"))

    print("Reestruturando diretório migrations")
    rmtree("./apps/" + dic.get("<<crud>>") + "/migrations")
    os.mkdir("./apps/" + dic.get("<<crud>>") + "/migrations")
    copyfile(
        "./apps/crud/migrations/__init__.py",
        "./apps/" + dic.get("<<crud>>") + "/migrations/__init__.py",
    )

    print("Renomeando arquivos necessários")
    os.rename(
        "./apps/" + dic.get("<<crud>>") + "/templates/estados_add.html",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_add.html",
    )
    os.rename(
        "./apps/" + dic.get("<<crud>>") + "/templates/estados_list.html",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_list.html",
    )
    os.rename(
        "./apps/" + dic.get("<<crud>>") + "/templates/estados_update.html",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_update.html",
    )

    listfiles = {
        "./apps/" + dic.get("<<crud>>") + "/urls.py": "Definindo rotas",
        "./apps/" + dic.get("<<crud>>") + "/models.py": "Criando o modelo",
        "./apps/" + dic.get("<<crud>>") + "/forms.py": "Gerando formulário",
        "./apps/" + dic.get("<<crud>>") + "/admin.py": "Gerando painel administrativo",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_update/views.py": "Visão de atualização",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_list/views.py": "Visão de listagem",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_delete/views.py": "Visão de deleção",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_add/views.py": "Visão de adição",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_add.html": "Visão de adição",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_list.html": "Visão de adição",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_update.html": "Visão de adição",
    }

    for listfileskey in listfiles:
        print(listfiles[listfileskey])

        namer = listfileskey
        namew = listfileskey + ".bac"

        filewrite = open(namew, "w")
        with open(namer, "r") as fileread:
            for line in fileread:
                for key in dic:
                    line = line.replace(key, dic[key])
                filewrite.write(line)
        filewrite.close()

        os.remove(listfileskey)
        os.rename(namew, namer)

    print(
        "Crud gerado com sucesso. Adicione ele como APP da aplicação, preencha o MODEL e faça o MAKEMIGRATIONS!"
    )


if __name__ == "__main__":
    main()
