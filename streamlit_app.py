<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Teacher's Day, Mam Kiran Nabi!</title>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --accent-green: #10b981;
            --accent-cyan: #06b6d4;
            --accent-pink: #f43f5e;
            --text-light: #f8fafc;
            --text-muted: #94a3b8;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-light);
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 2rem 1rem;
            overflow-x: hidden;
        }

        /* Hero Header */
        .header {
            text-align: center;
            margin-bottom: 2rem;
            animation: fadeIn 1s ease-in-out;
        }

        .header h1 {
            font-size: 2.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .header p {
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        /* Main Container */
        .container {
            max-width: 800px;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        /* Tech Card Styling */
        .card {
            background: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-4px);
        }

        /* Apology / Terminal Box */
        .terminal {
            background-color: #020617;
            border-radius: 12px;
            border: 1px solid #1e293b;
            overflow: hidden;
            font-family: 'Fira Code', monospace;
        }

        .terminal-header {
            background: #0f172a;
            padding: 0.6rem 1rem;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #1e293b;
        }

        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .dot-red { background-color: #ef4444; }
        .dot-yellow { background-color: #f59e0b; }
        .dot-green { background-color: #10b981; }

        .terminal-body {
            padding: 1.5rem;
            color: #38bdf8;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .terminal-body .command {
            color: var(--accent-green);
        }

        .terminal-body .error {
            color: var(--accent-pink);
        }

        .terminal-body .highlight {
            color: #facc15;
        }

        /* Apology Note */
        .apology-section {
            border-left: 4px solid var(--accent-pink);
            background: rgba(244, 63, 94, 0.05);
        }

        .apology-section h3 {
            color: var(--accent-pink);
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Appreciation Wishes */
        .wish-section h2 {
            color: var(--accent-cyan);
            margin-bottom: 1rem;
        }

        .wish-section p {
            line-height: 1.8;
            color: #cbd5e1;
            margin-bottom: 1rem;
        }

        /* Interactive Button Section */
        .interactive-zone {
            text-align: center;
            padding: 1.5rem;
        }

        .btn {
            background: linear-gradient(135deg, var(--accent-cyan), var(--accent-green));
            color: #0f172a;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        }

        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
        }

        #hidden-message {
            margin-top: 1.5rem;
            display: none;
            padding: 1rem;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid var(--accent-green);
            border-radius: 12px;
            color: var(--accent-green);
            font-weight: 500;
            animation: fadeIn 0.5s ease;
        }

        footer {
            margin-top: auto;
            padding-top: 2rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            text-align: center;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 600px) {
            .header h1 { font-size: 2rem; }
            .card { padding: 1.2rem; }
        }
    </style>
</head>
<body>

    <header class="header">
        <h1>Happy Teacher's Day! ✨</h1>
        <p>Dedicated to the best Computer Teacher: <strong>Mam Kiran Nabi</strong></p>
    </header>

    <div class="container">

        <!-- Tech Terminal Block -->
        <div class="terminal">
            <div class="terminal-header">
                <div class="dot dot-red"></div>
                <div class="dot dot-yellow"></div>
                <div class="dot dot-green"></div>
                <span style="font-size: 0.8rem; color: #64748b; margin-left: 10px;">apology_log.sh</span>
            </div>
            <div class="terminal-body">
                <p><span class="command">student@system:~$</span> execute wish_teacher.py</p>
                <p class="error">[WARNING]: Exception detected in Memory Buffer!</p>
                <p class="highlight">> Error 404: Timely Wish Not Found.</p>
                <p>> System automatically compiling heartfelt apology module...</p>
                <p class="command">> Status: RUNNING SUCCESSFUL (100%)</p>
            </div>
        </div>

        <!-- Sincere Apology Card -->
        <div class="card apology-section">
            <h3><span>🙏</span> I Am So, So Sorry, Mam!</h3>
            <p>
                I feel extremely guilty for missing the opportunity to wish you on time and needing your reminder. As your computer science student, forgetting a critical event feels like an unhandled bug in my system! Please forgive my delay—my respect and gratitude for you are always running in the background, 24/7.
            </p>
        </div>

        <!-- Appreciation Note Card -->
        <div class="card wish-section">
            <h2>To My Favorite Tech Mentor 👩‍💻</h2>
            <p>
                Dear <strong>Mam Kiran Nabi</strong>,
            </p>
            <p>
                Thank you for turning complex logic into simple understanding and making computer science so engaging and exciting. You don't just teach code and theory; you inspire us to debug our mistakes, think critically, and upgrade ourselves every day.
            </p>
            <p>
                You are truly the best teacher, and I am so grateful to have you as my mentor!
            </p>
        </div>

        <!-- Interactive Surprise Section -->
        <div class="card interactive-zone">
            <button class="btn" onclick="revealMessage()">Click to Compile Wish 🚀</button>
            <div id="hidden-message">
                🎉 <code>System.out.println("Happy Teacher's Day, Mam Kiran Nabi! You are legendary!");</code> 🎉
            </div>
        </div>

    </div>

    <footer>
        <p>Built with ❤️ and respect by your student | Always learning, always debugging</p>
    </footer>

    <script>
        function revealMessage() {
            const messageBox = document.getElementById('hidden-message');
            messageBox.style.display = 'block';
        }
    </script>

</body>
</html>
