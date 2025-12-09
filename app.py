from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IronPulse Fitness</title>

  <style>
    /* Basic Reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: "Poppins", sans-serif;
      background-color: #f4f4f4;
      color: #333;
    }

    /* Navbar */
    nav {
      background-color: #1e1e1e;
      padding: 15px 0;
    }

    nav ul {
      list-style: none;
      display: flex;
      justify-content: center;
      gap: 40px;
    }

    nav ul li a {
      color: white;
      text-decoration: none;
      font-size: 18px;
      font-weight: 600;
      transition: 0.3s;
    }

    nav ul li a:hover {
      color: #ff3c00;
    }

    /* Hero Section */
    header {
      background-image: url("https://images.unsplash.com/photo-1558611848-73f7eb4001a1?auto=format&fit=crop&w=1600&q=80");
      background-size: cover;
      background-position: center;
      height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: white;
      text-shadow: 2px 2px 10px rgba(0,0,0,0.7);
    }

    header h1 {
      font-size: 60px;
      letter-spacing: 2px;
    }

    header p {
      font-size: 20px;
      margin-top: 10px;
    }

    /* About Section */
    section {
      padding: 60px 20px;
      text-align: center;
    }

    section h2 {
      font-size: 36px;
      color: #222;
      margin-bottom: 20px;
    }

    section p {
      font-size: 18px;
      max-width: 700px;
      margin: 0 auto 40px;
      color: #555;
    }

    /* Gallery */
    .gallery {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
    }

    .gallery img {
      width: 300px;
      height: 200px;
      object-fit: cover;
      border-radius: 10px;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .gallery img:hover {
      transform: scale(1.05);
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* Membership Section */
    .plans {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 25px;
    }

    .plan {
      background-color: white;
      border-radius: 10px;
      padding: 25px;
      width: 250px;
      box-shadow: 0 3px 8px rgba(0,0,0,0.2);
      transition: 0.3s;
    }

    .plan:hover {
      transform: translateY(-5px);
    }

    .plan h3 {
      color: #ff3c00;
      margin-bottom: 15px;
    }

    .plan p {
      font-size: 18px;
    }

    /* Footer */
    footer {
      background-color: #1e1e1e;
      color: white;
      text-align: center;
      padding: 15px 0;
      margin-top: 40px;
    }

  </style>
</head>
<body>

  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/membership">Membership</a></li>
    </ul>
  </nav>
"""

ABOUT = """
<section>
  <h2>About Us</h2>
  <p>
    At IronPulse Fitness, we believe in transforming lives through fitness. 
    Our state-of-the-art equipment, certified trainers, and friendly environment 
    make your fitness journey exciting and effective.
  </p>

  <div class="gallery">
    <img src="https://images.unsplash.com/photo-1554284126-aa88f22d8b74?auto=format&fit=crop&w=800&q=60">
    <img src="https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&w=800&q=60">
  </div>
</section>
"""

MEMBERSHIP = """
<section>
  <h2>Membership Plans</h2>
  <div class="plans">
    <div class="plan"><h3>Monthly</h3><p>$50 / month</p></div>
    <div class="plan"><h3>Quarterly</h3><p>$135 / 3 months</p></div>
    <div class="plan"><h3>Yearly</h3><p>$500 / year</p></div>
  </div>
</section>
"""

FOOTER = """
  <footer>
    <p>© 2025 IronPulse Fitness | Designed by Umer</p>
  </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML + """
    <header>
      <h1>Welcome to IronPulse Fitness</h1>
      <p>Train Hard • Stay Strong • Live Fit</p>
    </header>
    """ + ABOUT + MEMBERSHIP + FOOTER


@app.route("/about")
def about():
    return HTML + ABOUT + FOOTER


@app.route("/membership")
def membership():
    return HTML + MEMBERSHIP + FOOTER


if __name__ == "__main__":
    app.run(debug=True)
