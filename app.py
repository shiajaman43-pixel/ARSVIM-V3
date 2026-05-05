from flask import Flask, render_template_string
import os

app = Flask(__name__)

# ১. প্রজেক্ট ডাটা (AI descriptions, benefits, effects সহ)
projects = {
    "humanoid": {
        "title": "ARSVIM-V1 Humanoid",
        "tag": "Advanced Robotics",
        "image": "https://images.unsplash.com/photo-1546776310-eef45dd6d63c?q=80&w=1000",
        "speciality": "Mechanical lip-syncing and sound frequency analysis.",
        "benefits": "এটি মানুষের সাথে রোবটের ইন্টারঅ্যাকশন সহজ করে এবং কাস্টমার সার্ভিসে বিপ্লব ঘটাতে পারে।",
        "bad_effects": "অত্যধিক বিদ্যুৎ খরচ এবং এটি মেইনটেইন করার খরচ অনেক বেশি।",
        "description": "ARSVIM-V1 একটি অত্যাধুনিক রোবটিক হেড প্রোটোটাইপ। এটি মানুষের কণ্ঠস্বরের ছন্দ বুঝে ঠোঁট নাড়াতে পারে।"
    },
    "uturn": {
        "title": "Smart U-Turn System",
        "tag": "Safety Innovation",
        "image": "https://images.unsplash.com/photo-1596733204953-6a987d69286d?q=80&w=1000",
        "speciality": "Ultrasonic Sensor Fusion এর মাধ্যমে অন্ধ মোড়ে গাড়ি শনাক্তকরণ।",
        "benefits": "পাহাড়ি রাস্তায় প্রায় ৯০% দুর্ঘটনা কমিয়ে আনতে সক্ষম এবং চালককে আগেভাগে সতর্ক করে।",
        "bad_effects": "ভারী বৃষ্টির সময় সেন্সরের একুরেসি কিছুটা কমে যেতে পারে।",
        "description": "এটি রাস্তার ব্লাইন্ড স্পটে বিপরীত দিক থেকে আসা গাড়ির অবস্থান শনাক্ত করে সিগন্যাল দেয়। সায়েন্স ফেয়ার ২০২৬-এ এটি ২য় স্থান অর্জন করেছে।"
    },
    "bridge": {
        "title": "Automated Smart Bridge",
        "tag": "Smart City Tech",
        "image": "https://images.unsplash.com/photo-1545138697-45eb2968b249?q=80&w=1000",
        "speciality": "Real-time traffic counting এবং স্বয়ংক্রিয় সার্ভো-গেট কন্ট্রোল।",
        "benefits": "ট্রাফিক জ্যাম মুক্ত রাস্তা এবং জাহাজ চলাচলের সময় অটোমেটিক গেট বন্ধ করে নিরাপত্তা নিশ্চিত করে।",
        "bad_effects": "সিস্টেম ক্রাশ করলে ম্যানুয়াল কন্ট্রোল ছাড়া গেট খোলা কঠিন হতে পারে।",
        "description": "এটি একটি ফিউচারিস্টিক স্মার্ট ব্রিজ মডেল যা আইআর সেন্সর ব্যবহার করে স্বয়ংক্রিয়ভাবে ট্রাফিক কন্ট্রোল করে।"
    }
}

# ২. তোমার ব্যক্তিগত তথ্য
bio_data = {
    "name": "Rasvi Zaman Siyam",
    "school": "Ulipur Maharani Sornomoyi School & College",
    "class": "Class 9",
    "location": "Ulipur, Kurigram",
    "achievements": "2nd Place Winner, Science Fair 2026",
    "interest": "Robotics, AI, and Electronics Engineering"
}

# ৩. মেইন পেজ (HTML & CSS)
@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ARSVIM | Engineering Hub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            :root { --accent: #c5a059; --bg: #ffffff; --dark: #121212; }
            body { background: var(--bg); font-family: 'Helvetica Neue', Arial; }
            .navbar { border-bottom: 1px solid #eee; padding: 25px 0; background: white; }
            .navbar-brand { font-size: 2rem; font-weight: 900; letter-spacing: 6px; color: var(--dark) !important; text-decoration: none;}
            .main-container { max-width: 1200px; margin: auto; padding: 60px 20px; }
            .project-card { background: white; border-radius: 15px; border: 1px solid #f0f0f0; transition: 0.5s; text-decoration: none; color: inherit; display: block; height: 100%; box-shadow: 0 10px 40px rgba(0,0,0,0.04); overflow: hidden; }
            .project-card:hover { transform: translateY(-15px); box-shadow: 0 25px 50px rgba(197, 160, 89, 0.15); border-color: var(--accent); }
            .img-wrap { height: 260px; overflow: hidden; }
            .img-wrap img { width: 100%; height: 100%; object-fit: cover; }
            .card-body { padding: 40px; text-align: center; }
            .bio-wrap { background: #fcfaf5; padding: 100px 0; border-top: 1px solid #eee; }
            .bio-card { max-width: 850px; margin: auto; background: white; padding: 60px; border: 1px solid #e0e0e0; }
            footer { padding: 40px; text-align: center; letter-spacing: 5px; color: #aaa; font-size: 0.8rem; }
        </style>
    </head>
    <body>
    <nav class="navbar text-center"><div class="container"><a href="#" class="navbar-brand">ARSVIM</a></div></nav>
    <div class="main-container">
        <div class="row g-5">
            {% for id, p in projects.items() %}
            <div class="col-md-4">
                <a href="/project/{{id}}" class="project-card">
                    <div class="img-wrap"><img src="{{p.image}}"></div>
                    <div class="card-body">
                        <h3 style="font-weight: 300;">{{p.title}}</h3>
                        <p class="text-muted">Details</p>
                    </div>
                </a>
            </div>
            {% endfor %}
        </div>
    </div>
    <div class="bio-wrap">
        <div class="bio-card text-center shadow-sm">
            <h2 style="font-size: 3rem; font-weight: 200;">{{bio.name}}</h2>
            <p style="font-size: 1.2rem; line-height: 2; color: #444;">
                Student of <strong>{{bio.school}}</strong>, <strong>{{bio.class}}</strong>. <br>
                Location: <strong>{{bio.location}}</strong>. <br>
                Achievement: <strong>{{bio.achievements}}</strong>
            </p>
        </div>
    </div>
    <footer>© 2026 ARSVIM TECHNOLOGY</footer>
    </body>
    </html>
    """
    return render_template_string(html, projects=projects, bio=bio_data)

# ৪. ডিটেইল পেজ
@app.route('/project/<project_id>')
def project_detail(project_id):
    p = projects.get(project_id)
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { padding: 50px 20px; font-family: sans-serif; }
            .container-detail { max-width: 800px; margin: auto; }
            img { width: 100%; height: 450px; object-fit: cover; border-radius: 20px; }
            .spec-box { background: #f9f9f9; padding: 30px; margin-top: 30px; border-left: 5px solid #c5a059; }
        </style>
    </head>
    <body>
        <div class="container-detail">
            <a href="/" style="color: #c5a059; text-decoration: none;">← BACK</a>
            <img src="{{p.image}}" class="mt-4">
            <h1 class="mt-4">{{p.title}}</h1>
            <p>{{p.description}}</p>
            <div class="spec-box">
                <h5>Speciality:</h5> <p>{{p.speciality}}</p>
                <h5>Benefits:</h5> <p>{{p.benefits}}</p>
                <h5>Bad Effects:</h5> <p>{{p.bad_effects}}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, p=p)

# ৫. সার্ভার সেটিংস (Render এর জন্য পরিবর্তন করা হয়েছে)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
