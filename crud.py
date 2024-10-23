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
        "# <<crudsettings>>": '"apps.' + sys.argv[1] + '",\n    # <<crudsettings>>',
        "# <<crudurls>>": 'path("", include("apps.'
        + sys.argv[1]
        + '.urls")),\n    # <<crudurls>>',
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
        "./config/settings.py": "Adicionando aplicação na configuração",
        "./config/urls.py": "Adicionando rotas",
        "./apps/" + dic.get("<<crud>>") + "/urls.py": "Definindo rotas do módulo",
        "./apps/" + dic.get("<<crud>>") + "/models.py": "Criando o modelo",
        "./apps/" + dic.get("<<crud>>") + "/forms.py": "Gerando formulário",
        "./apps/" + dic.get("<<crud>>") + "/admin.py": "Gerando painel administrativo",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_update/views.py": "Atualizando Visão de atualização",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_list/views.py": "Atualizando Visão de listagem",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_delete/views.py": "Atualizando Visão de deleção",
        "./apps/"
        + dic.get("<<crud>>")
        + "/transaction_add/views.py": "Atualizando Visão de adição",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_add.html": "Atualizando Template de adição",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_list.html": "Atualizando Template de listagem",
        "./apps/"
        + dic.get("<<crud>>")
        + "/templates/"
        + dic.get("<<crud>>")
        + "_update.html": "Atualizando Visão de atualização",
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

    print("Crud gerado com sucesso!")
    print()
    print("Próximas etapas:")
    print("- Preencha o MODEL")
    print("- Faça MAKEMIGRATIONS MIGRATES")
    print("- Adicione o menu")


if __name__ == "__main__":
    main()
