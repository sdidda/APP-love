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
    # Ajoutez ici jusqu'à 300 citations.
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
                flex-direction: column;
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
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
                font-size: 1.5em;
                color: #4a2e67;
                font-family: 'Great Vibes', cursive;
                text-align: center;
                box-sizing: border-box;
            }
            button {
                position: absolute;
                bottom: 10%;
                padding: 10px 20px;
                font-size: 1em;
                border-radius: 50px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
                font-family: 'Open Sans', sans-serif;
                background-color: #ff69b4;
                border: 3px solid #ff1493;
                color: white;
            }
            button:hover {
                background-color: #ff1493;
                transform: scale(1.1);
            }
            button.previous {
                left: 15%;
            }
            button.next {
                right: 15%;
            }
            @keyframes float {
                0% {
                    transform: translateY(0) rotate(-45deg);
                    opacity: 1;
                }
                50% {
                    transform: translateY(-200px) rotate(-45deg) scale(1.5);
                    opacity: 0.8;
                }
                100% {
                    transform: translateY(-400px) rotate(-45deg);
                    opacity: 0;
                }
            }
            .heart {
                position: absolute;
                width: 20px;
                height: 20px;
                background-color: rgba(255, 105, 180, 0.7);
                transform: rotate(-45deg);
                animation: float 5s ease-in-out infinite;
                pointer-events: none;
            }
            .heart::before,
            .heart::after {
                content: "";
                position: absolute;
                width: 20px;
                height: 20px;
                background-color: rgba(255, 105, 180, 0.7);
                border-radius: 50%;
            }
            .heart::before {
                top: -10px;
                left: 0;
            }
            .heart::after {
                top: 0;
                left: -10px;
            }
            @media (max-width: 600px) {
                .quote-slide {
                    font-size: 1.2em;
                    padding: 20px;
                }
                button {
                    font-size: 0.9em;
                    padding: 8px 15px;
                }
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
        <button class="previous" onclick="previousSlide()">Retour</button>
        <button class="next" onclick="nextSlide()">Suivant</button>
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

            function createHeart() {
                const heart = document.createElement('div');
                heart.className = 'heart';
                heart.style.left = Math.random() * 100 + '%';
                heart.style.bottom = '0';
                heart.style.animationDuration = 3 + Math.random() * 2 + 's';
                document.body.appendChild(heart);

                setTimeout(() => {
                    heart.remove();
                }, 5000);
            }

            setInterval(createHeart, 300);
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content, quotes=quotes)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
