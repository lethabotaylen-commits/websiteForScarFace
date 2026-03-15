from flask import Flask, send_from_directory

app = Flask(__name__)

# Allow access to love.mp3
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>To My Girlfriend Zoë ❤️</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                font-family: 'Courier New', monospace;
                background: linear-gradient(to right, #ff9a9e, #fad0c4);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                position: relative;
            }

            .tulip {
                position: fixed;
                font-size: 60px;
                top: 50%;
                transform: translateY(-50%);
            }

            .left { left: 15px; }
            .right { right: 15px; }

            .paper {
                background: repeating-linear-gradient(
                    white,
                    white 24px,
                    #e6e6e6 25px
                );
                width: 90%;
                max-width: 850px;
                padding: 40px;
                border-radius: 15px;
                border: 4px solid #ffb6c1;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                line-height: 25px;
                font-size: 18px;
                color: black;
                text-align: center;
                display: none;
            }

            h1 {
                color: #ff4d6d;
            }

            .heart {
                color: red;
                animation: glow 1.5s infinite alternate;
            }

            @keyframes glow {
                from { text-shadow: 0 0 5px red; }
                to { text-shadow: 0 0 20px red, 0 0 30px red; }
            }

            #startBtn {
                padding: 15px 30px;
                font-size: 20px;
                border: none;
                border-radius: 10px;
                background-color: #ff4d6d;
                color: white;
                cursor: pointer;
            }

            #typing {
                white-space: pre-wrap;
                border-right: 2px solid black;
            }
        </style>
    </head>

    <body>

        <button id="startBtn">Click to Start ❤️</button>

        <audio id="music" loop>
            <source src="/love.mp3" type="audio/mpeg">
        </audio>

        <div class="tulip left">🌷</div>
        <div class="tulip right">🌷</div>

        <div class="paper" id="letter">

        <h1>To My Girlfriend Zoë <span class="heart">❤️</span></h1>

        <div id="typing"></div>

        </div>

        <script>
            const text = `Love is a strong word ii never used to use
But now I’m with you it’s a strong word with meaning
That ii just cannot explain right now

My love for you grows stronger and stronger every time we text or hang out
Ii enjoy our time together
It feels like I’m always on a first date
My heart always skips a beat
Ii still have butterflies in my stomach
Even tho you’re already my girlfriend
Ii still have the biggest crush on you
You’re the most pretty most gorgeoustest girl ever

You never go dull like a Lantana flower
You’re always glowing

Ii don’t know if you created a better version of me
Or just helped me see the one that was already there
But above all you have shown me how true love feels

Ii’m grateful you didn’t make it easy to become your boyfriend
Our love is solid and will last a lifetime

I Love you So much Zoë
Ii hope you never forget that.

XoXo 💋 Taylen`;

            let i = 0;

            function typeWriter() {
                if (i < text.length) {
                    document.getElementById("typing").innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 80); // reading pace
                }
            }

            document.getElementById("startBtn").onclick = function() {
                document.getElementById("music").play();
                document.getElementById("startBtn").style.display = "none";
                document.getElementById("letter").style.display = "block";
                typeWriter();
            };
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(port=5001)

