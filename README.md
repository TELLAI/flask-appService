# Flask-appService:
Sur ce project nous avons pour but de déployer sur une le service web AppService de azure une application flask qui nous renvoie certaines routes.
Ces routes vont communiquer avec un base de donnée stocké sur une VM azure.
Le but est de communiquer entre la VM et la Web app azure.

## Technologies  :snake: ⚗️:whale:
- Python
- Postgresql 
- Flask
- HTML 
- Docker 

## Deployment :pencil:

### 1) Passage par Gitactions et la CI de Git:
- Créer une Web App et la configurer pour la relier à notre repository Git sur Github.
- Pour cela:

        - Aller dans l'onglet Deployment Center

        - onglet Settings

        - Dans le menu déroulant source choisir github

        - La plateforme va nous créer une pré-configuration à rajouter dans le workflow de notre app.

- Dans le fichier YML de notre workflows ajouter la préconfiguration azure pour deployer sur la Web App.
- Pusher les fichiers sur le repo git et git actions va s'occuper de déployer sur la web App

### 2) Passage par conteneur docker:
- Créer un dockerfile avec la configuration que l'on souhaite deployer
- Créer un regitry container sur Azure .
- Build l'image docker en local
- se logger au contenair registry
- push l'image docker dans le container registry
- Créer la web App avec l'option conteneur
- Choisir l'image docker a utiliser dans la web App

### 3) Passage par le CLI azure:
- Se logger à azure .
- Aller dans le dossier de l'app
- Taper cette commande: az webapp up --sku B1 --name <app-name>
- Azure va se charger de créer la Web App et run le script app.py

## Configuration Postgresql sur la VM:

- Afin que la web App puissent se connecter à postgresql de la VM :
        
        - Décommenter la ligne localhost = "*" dans le fichier postgres.conf
        
        - rajouter host   all   all 0.0.0.0/0     md5 dans le fichier pg_hba.conf
        
        - restart psql
        
        - set un password à l'utilisateur postgres
        
        - rajouter l'adresse IP de la VM dans le script flask

## Next step :pencil2:

 - [ ] Ajouter mon scrapper

