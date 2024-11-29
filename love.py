from flask import Flask, render_template_string
import random
import openai
import os

# Initialiser l'application Flask
app = Flask(__name__)

# Initialiser l'API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fonction pour générer une citation d'amour unique
def generate_love_quote():
    prompt = "Génère une citation d'amour inspirante."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        temperature=0.9  # Augmente la créativité
    )
    return response.choices[0].message['content'].strip()

# Route principale pour afficher la page web
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Un peu d'amour infini</title>
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
            .quote-container {
                width: 90%;
                max-width: 800px;
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
                margin-top: 20px;
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
        </style>
    </head>
    <body>
        <div class="quote-container">
            {{ quote }}
        </div>
        <form method="get" action="/">
            <button type="submit">Nouvelle citation</button>
        </form>
    </body>
    </html>
    """
    # Générer une nouvelle citation d'amour
    quote = generate_love_quote()
    return render_template_string(html_content, quote=quote)

# Lancer l'application Flask
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
