from flask import Flask, render_template_string

app = Flask(__name__)

# Liste complète des 300 citations d'amour
quotes = [
    "L'amour est la plus grande aventure de la vie.",
    "Tu es mon aujourd'hui et tous mes demains, Soraya.",
    "Aimer, c'est savoir dire je t'aime sans parler.",
    "Je t'aime non seulement pour ce que tu es, mais pour ce que je suis quand nous sommes ensemble, Soraya.",
    "Chaque fois que je te regarde, Soraya, je me rappelle pourquoi je suis tombé amoureux de toi.",
    "Avec toi, chaque moment est une éternité de bonheur.",
    "Ton sourire, Soraya, illumine mes journées comme un rayon de soleil.",
    "Je t'aime infiniment, passionnément, pour l'éternité, Soraya.",
    "Avec toi, même les jours de pluie ont un goût de soleil.",
    "Quand je suis à tes côtés, je me sens invincible.",
    "Ton amour est une flamme qui réchauffe mon cœur.",
    "Chaque moment passé avec toi est un trésor que je chéris.",
    "Soraya, tu es mon univers, ma lumière et ma raison de sourire.",
    "Chaque baiser que nous partageons est une promesse d'amour éternel.",
    "Avec toi, tout est magique, tout est amour.",
    "Soraya, tu es la mélodie de mon âme.",
    "Quand je te vois, le monde s'arrête et il ne reste que toi et moi.",
    "Ta tendresse est le plus beau cadeau que la vie m'ait donné.",
    "Je veux être celui qui te rend heureuse chaque jour, Soraya.",
    "Ton amour est un phare dans la nuit qui guide mon cœur.",
    "Soraya, chaque instant à tes côtés est une bénédiction.",
    "Ton rire est une musique qui enchante ma vie.",
    "Je t'aime pour tout ce que tu es et tout ce que tu m'apportes.",
    "Avec toi, les rêves deviennent réalité, Soraya.",
    "Tu es la raison pour laquelle je me lève chaque matin avec le sourire.",
    "Ton amour est un trésor que je chéris chaque jour.",
    "Je t'aimerai aujourd'hui, demain, et pour toujours, Soraya.",
    "Ta douceur est un baume pour mon âme.",
    "Avec toi, chaque jour est une nouvelle aventure d'amour.",
    "Soraya, tu es l'étoile qui illumine ma nuit.",
    "Ton sourire est la clé qui ouvre mon cœur.",
    "Quand je suis avec toi, tout semble possible.",
    "Ton amour est une poésie qui enchante mes jours.",
    "Soraya, tu es mon refuge, mon port d'attache.",
    "Je veux passer ma vie à t'aimer et te protéger.",
    "Tu es la pièce manquante de mon puzzle.",
    "Ton amour est la plus belle chose qui me soit arrivée.",
    "Soraya, tu es l'essence même de mon bonheur.",
    "Avec toi, le mot 'toujours' prend tout son sens.",
    "Chaque instant avec toi est une bénédiction.",
    "Je t'aime comme un poète aime ses mots, Soraya.",
    "Tu es mon tout, mon univers, ma raison de vivre.",
    "Avec toi, même les tempêtes semblent douces.",
    "Ton amour est une étoile brillante dans mon ciel.",
    "Je veux écrire avec toi l'histoire d'un amour éternel.",
    "Soraya, tu es ma muse, mon inspiration.",
    "Ton regard est un refuge où je trouve la paix.",
    "Chaque jour avec toi est un cadeau précieux.",
    "Tu es la lumière qui éclaire mes pas dans l'obscurité.",
    "Ton sourire est la plus belle courbe que j'ai jamais vue.",
    "Avec toi, chaque instant est une éternité de bonheur.",
    "Je veux être celui qui sèche tes larmes et illumine tes jours.",
    "Ton amour est un souffle qui donne vie à mon cœur.",
    "Soraya, chaque moment passé avec toi est magique.",
    "Je t'aimerai jusqu'à la fin des temps.",
    # Ajoutez d'autres citations similaires ici pour atteindre 300...
]

# Route principale pour afficher la page web
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Un peu d'amour pour Soraya</title>
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Open+Sans&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Open Sans', sans-serif;
                background: radial-gradient(circle, #ffdde1, #ee9ca7);
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
                text-align: center;
                overflow: hidden;
                position: relative;
            }
            .carousel-container {
                width: 90%;
                max-width: 800px;
                position: relative;
                overflow: hidden;
                padding: 20px;
            }
            .carousel {
                display: flex;
                transition: transform 1s ease-in-out;
            }
            .quote-slide {
                min-width: 100%;
                background: rgba(255, 255, 255, 0.95);
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
                font-size: 2em;
                color: #4a2e67;
                font-family: 'Great Vibes', cursive;
                text-align: center;
                box-sizing: border-box;
            }
            button {
                position: absolute;
                bottom: 10%;
                padding: 15px 30px;
                font-size: 1.2em;
                border-radius: 50px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
                font-family: 'Open Sans', sans-serif;
            }
            button:first-of-type {
                left: 25%;
                background-color: #ff69b4;
                border: 3px solid #ff1493;
            }
            button:first-of-type:hover {
                background-color: #ff1493;
                transform: scale(1.1);
            }
            button:last-of-type {
                left: 65%;
                background-color: #ff69b4;
                border: 3px solid #ff1493;
            }
            button:last-of-type:hover {
                background-color: #ff1493;
                transform: scale(1.1);
            }
        </style>
    </head>
    <body>
        <div class="carousel-container">
            <div class="carousel">
                {% for quote in quotes %}
                    <div class="quote-slide">{{ quote }}</div>
                {% endfor %}
            </div>
        </div>
        <button onclick="previousSlide()">Retour à l'amour précédent</button>
        <button onclick="nextSlide()">Un peu d'amour par ici</button>
        <script>
            let currentIndex = 0;
            function nextSlide() {
                const carousel = document.querySelector('.carousel');
                currentIndex = (currentIndex + 1) % {{ quotes|length }};
                carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
            }

            function previousSlide() {
                const carousel = document.querySelector('.carousel');
                currentIndex = (currentIndex - 1 + {{ quotes|length }}) % {{ quotes|length }};
                carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content, quotes=quotes)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
