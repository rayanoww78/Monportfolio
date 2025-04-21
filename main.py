# app.py

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Données du portfolio
DATA = {
    "info": {
        "nom": "Rayan EL AMJAD",
        "titre": "Développeur Informatique Indépendant",
        "email": "elamjadrayan@gmail.com",
        "description": "Passionné par l'analyse de données, le développement web et l'automatisation, je conçois des solutions concrètes qui transforment des idées complexes en outils intelligents et accessibles.",
        "age": 20,
        "formation": [
            {
                "école": "BUT Informatique de Valencienne",
                "formation" : "BUT Informatique",
                "lieu": "Maubeuge",
                "periode": "1ère année - En cours"
            },
            {
                "école": "EFREI Paris",
                "formation" : "école d'ingénieur",
                "lieu": "Villejuif",
                "periode": "2 ans"
            }
        ],
        "competences": [
            "Analyse de données",
            "Power BI, Tableaux de bord",
            "Gestion de projets",
            "PostGreSQL",
            "Python",
            "Java",
            "C"
        ],
        "reseaux": {
            "linkedin": "https://www.linkedin.com/in/rayan-el-amjad/",
            "github": "https://github.com/rayanoww78"
        }
    },
    "projets": [
        {
            "titre": "DiviTrack",
            "description": "Application web d'analyse d'investissements en temps réel intégrant les API Powens et Yahoo Finance, avec calculs d'EPS et de dividendes.",
            "technologies": ["API", "Finance", "Data Analysis"],
            "lien": "https://github.com/rayanoww78/DiviTrack/tree/master"
        },
        {
            "titre": "To-do List Intelligente",
            "description": "Application graphique multi-utilisateur avec authentification, recherche, marquage des tâches, intégration de l'API ChatGPT et fine-tuning d'un modèle pour une assistance personnalisée.",
            "technologies": ["IA", "API", "UI/UX"],
            "lien": "https://github.com/rayanoww78/To-do-list"
        },
        {
            "titre": "Analyse des Notes",
            "description": "Algorithme d'extraction et d'analyses de données envoyé par mail, permettant d'automatiser le traitement et l'analyse des résultats académiques.",
            "technologies": ["Data Mining", "Automation", "Email"],
            "lien": "https://github.com/rayanoww78/NoteDataAnalyzer"
        },
        {
            "titre": "Convertisseur de Monnaies",
            "description": "Application permettant de convertir différentes devises en temps réel grâce à l'intégration d'une API de taux de change.",
            "technologies": ["API", "Currency", "Real-time"],
            "lien": "https://github.com/rayanoww78/MoneyConvertisseur"
        },
        {
            "titre" : "Algorithme Développement personnel - Mood & Goal Tracker",
            "description" : "Algorithme demandant à la personne son humeur et la raison de son humeur puis qui lui demande chaque jour d'ajouter un objectif avec un niveau d'importance, une deadline, une approximation du nombre d'heure pour réussir l'objectif avec une interface graphique assez simple qui est par la suite stocké dans une base de données SQL.",
            "technologies": ["SQL", "Python", "Tkinter"],
            "lien" :"https://github.com/rayanoww78/Dev_perso"
        }    ]
}


@app.route('/')
def index():
    return render_template('index.html', data=DATA)


@app.route('/download-cv')
def download_cv():
    # Dans un cas réel, vous auriez un fichier CV dans un dossier static
    return send_from_directory('static', 'CV_RAYAN_EAD_MAJ.pdf')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        nom = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Ici, vous pourriez enregistrer ces informations dans une base de données
        # ou envoyer un email avec les informations du formulaire
        print(f"Message reçu de {nom} ({email}): {message}")

        # Rediriger vers la page d'accueil avec un paramètre de succès
        return redirect(url_for('index', message="success"))

    return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
