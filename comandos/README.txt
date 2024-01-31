-------------------------------------------------------------------------------------------------------------------------------------------------------
Iniciar um projeto em django

    1° -> crio o ambiente virtual
    2° -> atiovel 
    3° -> depois instale o Django
    4° -> se necessario atualizar o pip
    5° -> crie os arquivos necessarios de configurações do django com o startproject


-------------------------------------------------------------------------------------------------------------------------------------------------------
Ambiente virtual

    python -m venv venv (instalação e criação dos arquivos do ampiente virtual)

    . venv/Scripts/activate (ativação do ambiente virtual)

-------------------------------------------------------------------------------------------------------------------------------------------------------

PIP

    pip freeze (mostra as coisas instaladas no ambiente)

    python.exe -m pip install --upgrade pip (atualizar o pip)

    pip install django (instalar o django)

    pip install pillow (mexer com imagens)

-------------------------------------------------------------------------------------------------------------------------------------------------------

Django

    django-admin help (mostrar os comandos)

    pip install django (instalar o django)

    django-admin startproject project . (criação dos arquivos necessarios para o django funcionar, o nome da pasta do arquivo neste caso é profect)

    python manage.py runserver (rodar o servidor local), (Ctr| + c, para de rodar o servidor local)

    python manage.py startapp nomeEscolhiApp (cria os arqiovps necessarios do app)

    python manage.py makemigrations (usar quando fazer qualquer modificação nos models [data base] e usar o comando migrate depois)

    python manage.py migrate (base de dados)

    python manage.py createsuperuser (criação de super usuaria)

    python manage.py changepassword USERNAME

    python manage.py collectstatic (coletar todos os arquivos estaticos no final do desenvolvimento e transferir para esta pasta sinalizada)