from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Liste des 300 citations d'amour
quotes = [
    "L'amour est la plus grande aventure de la vie.",
    "Tu es mon aujourd'hui et tous mes demains, Soraya.",
    "Aimer, c'est savoir dire je t'aime sans parler.",
    "Je t'aime non seulement pour ce que tu es, mais pour ce que je suis quand nous sommes ensemble, Soraya.",
    "Chaque fois que je te regarde, Soraya, je me rappelle pourquoi je suis tombé amoureux de toi.",
    "Toi et moi, c'est pour la vie, tout simplement.",
    "Dans tes bras, j'ai trouvé ma maison, Soraya.",
    "Ton sourire, Soraya, est la raison pour laquelle mes journées sont meilleures.",
    "L'amour n'a pas de raison, il ne vit que de sentiments.",
    "Avec toi, chaque moment est une éternité de bonheur.",
    "Tu es la lumière de ma vie, Soraya, et chaque jour avec toi est un cadeau.",
    "Soraya, mon amour pour toi est infini, comme le ciel étoilé.",
    "Quand je te vois sourire, tout semble possible, Soraya.",
    "Aimer, c'est voir la magie dans les petites choses, chaque jour avec toi est un enchantement.",
    "Soraya, tu es ma muse, mon inspiration, mon tout.",
    "Je chéris chaque moment passé avec toi, car tu es ma plus grande bénédiction.",
    "Avec toi, je veux construire un avenir rempli de rires et de doux souvenirs.",
    "Ton amour est une mélodie qui adoucit mon cœur, Soraya.",
    "Je te choisirais, encore et encore, sans hésiter, pour l'éternité.",
    "Soraya, chaque instant à tes côtés est un trésor précieux.",
    "Ta tendresse est le plus beau des cadeaux, et ton amour la plus belle aventure.",
    "Je suis le plus chanceux des hommes car je t'ai toi, Soraya, à mes côtés.",
    "Ton amour est un feu qui réchauffe mon âme, même dans les moments les plus froids.",
    "Soraya, avec toi, chaque rêve devient réalité.",
    "Tu es la plus belle partie de mon existence, et je veux te le rappeler chaque jour.",
    "Quand je suis à tes côtés, je me sens complet, Soraya.",
    "Ton sourire est le soleil qui éclaire ma journée, et ton rire la musique qui enchante mes nuits.",
    "Je t'aime plus que tout, aujourd'hui, demain, et pour l'éternité, Soraya.",
    "Mon cœur t'appartient, et rien ne pourrait changer cela.",
    "Soraya, tu es ma force, ma faiblesse, mon tout.",
    "Avec toi, même les jours les plus simples deviennent extraordinaires.",
    "Ton amour est la plus belle lumière qui guide mes pas, Soraya.",
    "Rien n'est plus doux que de t'avoir près de moi.",
    "Être à tes côtés est la plus belle chose qui puisse m'arriver.",
    "Ton amour est une étoile qui brille éternellement dans mon ciel.",
    "Je t'aime comme je n'ai jamais aimé, Soraya.",
    "Avec toi, tout est possible, tout est amour.",
    "Soraya, je veux être l'homme qui te fait sourire chaque jour.",
    "Ton regard est un refuge, ton amour une paix.",
    "Je t'aime infiniment, passionnément, pour l'éternité, Soraya.",
    "Ton amour est une poésie qui enchante chaque instant de ma vie.",
    "Quand je suis dans tes bras, le monde entier disparaît et il ne reste que toi et moi.",
    "Chaque nuit passée avec toi est une étoile de plus dans mon ciel, Soraya.",
    "Tu es la mélodie douce qui apaise mes peurs et fait battre mon cœur.",
    "Soraya, ta voix est une chanson qui résonne tendrement dans mon âme.",
    "Mon amour pour toi est comme l'océan : profond, puissant, et éternel.",
    "Chaque matin, je remercie le destin de t'avoir placée sur mon chemin.",
    "Ta douceur est un baume pour mon cœur, et ta présence un trésor inestimable.",
    "Avec toi, même les tempêtes deviennent des brises légères.",
    "Ton amour illumine les coins les plus sombres de ma vie, Soraya.",
    "Je suis captivé par chaque regard que tu poses sur moi, chaque sourire que tu partages.",
    "Tu es la lumière qui éclaire mes jours et la chaleur qui réchauffe mes nuits.",
    "Mon bonheur est simple : c'est toi, ici, à mes côtés, pour toujours.",
    "Ta beauté ne se résume pas à ton visage, elle réside dans ton cœur qui est pur et aimant.",
    "Ton rire est la mélodie qui embellit ma vie chaque jour.",
    "J'ai trouvé mon paradis à travers tes yeux, et je ne veux jamais en sortir.",
    "Ta tendresse m'enveloppe comme une couverture chaude lors des nuits froides.",
    "Ton amour est la raison pour laquelle mon cœur continue de battre avec tant de passion.",
    "Chaque moment passé avec toi est un cadeau précieux que je chéris plus que tout.",
    "Je veux être la raison pour laquelle tu crois en l'amour, la raison pour laquelle tu souris chaque matin.",
    "Tu es mon miracle de chaque jour, ma plus belle histoire, mon éternité.",
    "Ton amour est la source de ma joie et de mon espoir, Soraya.",
    "Quand je suis avec toi, le reste du monde semble s'effacer, et seul notre amour subsiste.",
    "Soraya, tu es la fleur qui éclot dans mon jardin, pleine de grâce et de beauté.",
    "Je t'aime non seulement pour ce que tu es, mais pour ce que je deviens quand je suis avec toi.",
    "À chaque instant, je découvre de nouvelles raisons de t'aimer encore davantage, Soraya.",
    "Tu es l'étoile qui guide ma vie, et je suis prêt à tout pour te rendre heureuse.",
    "Chaque baiser que je te donne est un serment de mon amour éternel.",
    "Ton amour est la plus belle histoire qui puisse jamais m'arriver, Soraya.",
    "Tu es le souffle qui donne vie à mes rêves, la raison de chaque battement de mon cœur.",
    "Soraya, chaque instant passé loin de toi me rappelle combien tu es essentielle à ma vie.",
    "Je suis comblé car j'ai trouvé en toi non seulement l'amour mais aussi une amie, une âme sœur.",
    "Quand je suis à tes côtés, le monde semble plus beau, et mes problèmes s'effacent comme par magie.",
    "Chaque jour qui passe est une nouvelle chance de t'aimer, encore plus que la veille.",
    "Ton amour est un phare qui guide mon âme à travers les nuits les plus sombres.",
    "Ta présence est le cadeau le plus précieux que la vie m'ait donné, Soraya.",
    "Tu es mon univers, et sans toi, chaque étoile perdrait sa lumière.",
    "Ton amour est la boussole qui guide mes pas, chaque jour vers le bonheur.",
    "Quand je plonge dans ton regard, je vois mon avenir, et je sais que tout ira bien.",
    "Avec toi, je suis prêt à affronter n'importe quelle tempête, car tu es mon port d'attache.",
    "Ton sourire est la plus belle courbe que j'ai jamais vue, Soraya.",
    "Je veux passer le reste de ma vie à t'aimer, te protéger et te faire sourire.",
    "Chaque baiser que nous partageons est une promesse silencieuse d'un amour éternel.",
    "Tu es le rayon de soleil qui éclaire mes journées, et la lune qui veille sur mes nuits.",
    "Je ne sais pas ce que j'ai fait pour mériter quelqu'un d'aussi merveilleux que toi, mais je remercie le ciel chaque jour.",
    "Ton amour me fait pousser des ailes, et avec toi, je veux voler jusqu'aux confins du bonheur.",
    "Tu es la pièce manquante de mon puzzle, celle qui fait que tout prend sens.",
    "Avec toi, le mot 'toujours' prend enfin tout son sens.",
    "Soraya, tu es la plus douce des mélodies, celle que je veux écouter chaque jour pour le reste de ma vie.",
    "Je te promets de t'aimer, aujourd'hui, demain, et pour toutes les éternités à venir.",
    "Chaque seconde sans toi est une éternité, chaque minute à tes côtés est un instant magique.",
    "Ton amour est un élixir qui me rend plus fort, plus heureux, plus moi.",
    "Soraya, je veux que chaque sourire que tu as soit causé par moi.",
    "Quand je pense à toi, je vois tout ce que j'ai toujours rêvé d'avoir, et bien plus encore.",
    "Ton amour est un refuge où je trouve la paix, loin des tumultes du monde.",
    "Soraya, tu es celle qui donne un sens à mes jours et des rêves à mes nuits.",
    "Ta main dans la mienne, et je suis prêt à affronter l'univers entier.",
    "Avec toi, chaque matin est une promesse d'un bonheur infini.",
    "Tu es le plus beau chapitre de ma vie, et je n'ai pas envie de tourner la page.",
    "Ton amour est une caresse sur mon âme, un souffle doux qui apaise mes angoisses.",
    "Je veux être l'épaules sur laquelle tu te reposes, la main qui sèche tes larmes, et le sourire qui illumine ta journée.",
    "Tu es mon tout, Soraya, et sans toi, il n'y aurait plus de couleur dans ma vie.",
    "Chaque instant passé à tes côtés est une éternité que je souhaite prolonger pour toujours.",
    "Quand je te regarde, je me rappelle pourquoi je suis tombé amoureux de toi, encore et encore.",
    "Ton amour est une flamme qui ne s'éteint jamais, même dans les vents les plus violents.",
    "Ta présence est ma force, ton sourire ma faiblesse, et ton amour mon univers.",
    "Avec toi, chaque soir est une promesse d'un lendemain encore plus beau.",
    "Soraya, tu es l'étoile la plus brillante de mon ciel, et mon cœur bat à ton éclat.",
    "Chaque jour qui passe est une nouvelle occasion de t'aimer davantage, et je saisis chaque instant.",
    "Ton rire est la musique qui apaise toutes mes peines, et ton amour la raison de mon bonheur.",
    "Je t'aime, Soraya, comme un poète aime ses mots, comme un peintre aime ses couleurs.",
    "Quand tu es près de moi, le temps s'arrête, et je veux que cet instant dure pour toujours.",
    "Soraya, avec toi, je veux écrire l'histoire d'un amour sans fin, rempli de rêves et de rires.",
    "Ton amour est la plus douce des musiques, celle qui fait battre mon cœur.",
    "Avec toi, même les jours de pluie ont un goût de soleil.",
    "Je veux passer le reste de ma vie à t'aimer, Soraya, car avec toi, chaque instant est une éternité de bonheur.",
    "Ton sourire est la magie qui éclaire mes ténèbres, et je veux le voir chaque jour.",
    "Soraya, tu es mon évasion, mon horizon, et chaque instant passé avec toi est un voyage vers le bonheur.",
    "Avec toi, l'amour est la plus douce des réalités, une évidence que rien ne pourra jamais effacer.",
    "Ton amour est une étoile qui brille même dans la nuit la plus sombre, et je me perds volontiers dans sa lumière.",
    "Je veux que chaque instant de ta vie soit empli de bonheur, et je ferai tout pour le rendre possible.",
    "Soraya, chaque souffle que je prends est un témoignage de l'amour profond que j'ai pour toi.",
    "Ton amour est mon équilibre, ma paix, et chaque jour avec toi est une bénédiction.",
    "Avec toi, chaque matin est une promesse de rêves à réaliser ensemble, et chaque soir une étreinte de tendresse." 
    # Liste complète des 300 citations d'amour...
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
                background-color: #ff69b4;
                color: white;
                border: 3px solid #ff1493;
                padding: 15px 30px;
                font-size: 1.2em;
                border-radius: 50px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
                font-family: 'Open Sans', sans-serif;
                margin-top: 20px;
                position: absolute;
                bottom: 10%;
                left: 50%;
                transform: translateX(-50%);
            }
            button:hover {
                background-color: #ff1493;
                transform: scale(1.1) translateX(-50%);
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
        <button onclick="nextSlide()">Un peu d'amour par ici</button>
        <script>
            let currentIndex = 0;
            function nextSlide() {
                const carousel = document.querySelector('.carousel');
                currentIndex = (currentIndex + 1) % {{ quotes|length }};
                carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
            }

            function createHeart() {
                const heart = document.createElement('div');
                heart.className = 'heart';
                heart.style.left = Math.random() * 100 + '%';
                heart.style.bottom = '0';
                heart.style.animationDuration = 3 + Math.random() * 2 + 's'; // Randomize animation duration
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

