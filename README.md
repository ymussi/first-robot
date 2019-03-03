# Para instalar:

OBS: Utilize python >= 3.7

pip install -r requirements.txt

python setup.py develop


# Informar seus dados de acesso no config.ini

OBS: nao esqueça de alterar os dados no config.ini para poder rodar a API

# Iniciar o serviço

cd robot/

python app.py

# Testar o robot fora da API

cd robot/codigo/

alterar o config.read no robot_mail.py

    DE: config.read('../config.ini')
    PARA: config.read('../../config.ini')

python robot_mail.py

