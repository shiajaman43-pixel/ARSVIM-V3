from flask import Flask, render_template_string
import os

app = Flask(__name__)

# ১. প্রজেক্টের বিস্তারিত তথ্য (AI generated deep analysis)
projects = {
    "humanoid": {
        "title": "ARSVIM-V1 Humanoid Head",
        "tag": "Artificial Intelligence & Robotics",
        "image": "https://images.unsplash.com/photo-1546776310-eef45dd6d63c?q=80&w=1000",
        "overview": "একটি রোবটিক সিস্টেম যা মানুষের কণ্ঠস্বরের ফ্রিকোয়েন্সি বিশ্লেষণ করে প্রতিক্রিয়া জানায়।",
        "speciality": "Real-time voice-to-motion syncing (Lip Sync) এবং সার্ভো মোটরের সূক্ষ্ম কন্ট্রোল।",
        "problem": "প্রথাগত রোবটগুলো মানুষের মতো অভিব্যক্তি দিতে পারে না, যা ইন্টারঅ্যাকশনকে যান্ত্রিক করে তোলে।",
        "solution": "সাউন্ড সেন্সর এবং আরডুইনো মেগা ব্যবহার করে মানুষের কথার তালের সাথে রোবটের ঠোঁট এবং চোখের মুভমেন্ট সিঙ্ক্রোনাইজ করা হয়েছে।",
        "benefits": "এটি শিক্ষা প্রতিষ্ঠান, জাদুঘর এবং কাস্টমার সার্ভিস ডেস্কে ডিজিটাল অ্যাসিস্ট্যান্ট হিসেবে কাজ করতে পারে।",
        "future_scope": "ভবিষ্যতে এতে ফেসিয়াল রিকগনিশন এবং ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং (NLP) যুক্ত করার পরিকল্পনা রয়েছে।",
        "tech": ["Arduino Mega", "MG995 Servos", "Sound Sensor", "3D Printed Parts", "C++ Logic"]
    },
    "uturn": {
        "title": "Smart U-Turn Collision Avoidance",
        "tag": "IoT & Civil Safety",
        "image": "https://images.unsplash.com/photo-1596733204953-6a987d69286d?q=80&w=1000",
        "overview": "পাহাড়ি রাস্তার অন্ধ মোড়ে গাড়ি শনাক্ত করে দুর্ঘটনা রোধ করার একটি স্মার্ট সমাধান।",
        "speciality": "Sensor Fusion প্রযুক্তির মাধ্যমে মোড়ের উভয় প্রান্তের গাড়ির অবস্থান ট্র্যাক করা।",
        "problem": "পাহাড়ি মোড়ে চালকরা বিপরীত দিক থেকে আসা গাড়ি দেখতে পায় না, ফলে মারাত্মক দুর্ঘটনা ঘটে।",
        "solution": "আল্ট্রাসনিক সেন্সর নেটওয়ার্ক ব্যবহার করে মোড়ের অবস্থা পর্যবেক্ষণ করা হয় এবং এলইডি সিগন্যালের মাধ্যমে চালককে সাবধান করা হয়।",
        "benefits": "দুর্ঘটনার ঝুঁকি ৯০% কমায় এবং রাতে বা কুয়াশাতেও এটি চমৎকার কাজ করে।",
        "future_scope": "সোলার পাওয়ার এবং অটোমেটিক স্পিড ব্রেকার কন্ট্রোল সিস্টেম এর সাথে যুক্ত করা হবে।",
        "tech": ["Arduino Nano", "Ultrasonic Sensors", "RGB LED Matrix", "Solar Hybrid Power"]
    },
    "bridge": {
        "title": "Automated Smart Bridge 2.0",
        "tag": "Smart City Infrastructure",
        "image": "https://images.unsplash.com/photo-1545138697-45eb2968b249?q=80&w=1000",
        "overview": "স্বয়ংক্রিয় গেট নিয়ন্ত্রণ এবং রিয়েল-টাইম ট্রাফিক মনিটরিং সমৃদ্ধ আধুনিক ব্রিজ।",
        "speciality": "জাহাজ চলাচলের সময় অটো-গেট কন্ট্রোল এবং আইআইসি এলসিডি ডিসপ্লে ফিডব্যাক।",
        "problem": "ম্যানুয়াল গেট অপারেশনে সময় অপচয় হয় এবং অনেক সময় বড় দুর্ঘটনার ঝুঁকি থাকে।",
        "solution": "ইনফ্রারেড (IR) সেন্সর এবং সার্ভো গেট ব্যবহার করে সম্পূর্ণ সিস্টেমটিকে অটোমেটেড করা হয়েছে।",
        "benefits": "যানজট কমায়, শ্রমশক্তি সাশ্রয় করে এবং নিখুঁত ট্রাফিক ডেটা প্রদান করে।",
        "future_scope": "এটিআই (AI) ট্রাফিক ক্যামেরা এবং এমারজেন্সি অ্যাম্বুলেন্স ডিটেকশন মোড যুক্ত করা।",
        "tech": ["ESP32", "IR Sensors", "Servo Motors", "I2C LCD", "Buzzer Warning System"]
    }
}

bio_data = {
    "name": "Rasvi Zaman Siyam",
    "school": "Ulipur Maharani Sornomoyi School & College",
    "class": "Class 9",
    "location": "Ulipur, Kurigram, Bangladesh",
    "achievements": "2nd Place Winner, Science Fair 2026",
    "interest": "Robotics, AI, and Electronics Engineering",
    "goal": "বাংলাদেশি তরুণদের জন্য রোবটিক্স ল্যাব প্রতিষ্ঠা করা।"
}

# ২. মেইন পোর্টফোলিও পেজ (SEO Optimized)
@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Official Portfolio of Rasvi Zaman Siyam - Innovator of ARSVIM-V1 Humanoid, Smart Bridge, and Road Safety Systems.">
        <meta name="keywords" content="ARSVIM, ARSVIM-V1, Rasvi Zaman Siyam, Robotics Bangladesh, Smart U-Turn Project, Ulipur, Kurigram">
        <meta name="author" content="Rasvi Zaman Siyam">
        <title>ARSVIM | Engineering Portfolio by Siyam</title>
        
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            :root { --gold: #c5a059; --dark: #0f0f0f; --light: #f8f9fa; }
            body { background: var(--light); color: var(--dark); font-family: 'Inter', sans-serif; }
            .navbar { background: white; border-bottom: 2px solid var(--gold); padding: 20px 0; }
            .navbar-brand { font-size: 2.5rem; font-weight: 900; letter-spacing: 5px; color: var(--dark) !important; text-decoration: none; display: block; text-align: center; }
            
            .hero-header { padding: 120px 20px; text-align: center; background: radial-gradient(circle, #fff 0%, #f2f2f2 100%); border-bottom: 1px solid #ddd; }
            .hero-header h1 { font-size: 4rem; font-weight: 200; letter-spacing: 15px; margin-bottom: 15px; }

            .project-card { 
                background: white; border-radius: 20px; border: 1px solid #eee; transition: 0.5s; 
                text-decoration: none; color: inherit; display: block; height: 100%; overflow: hidden;
                box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            }
            .project-card:hover { transform: translateY(-15px); border-color: var(--gold); box-shadow: 0 20px 50px rgba(197, 160, 89, 0.15); }
            .img-wrap { height: 280px; overflow: hidden; }
            .img-wrap img { width: 100%; height: 100%; object-fit: cover; }
            .card-body { padding: 40px; text-align: center; }
            
            .bio-wrap { background: white; padding: 100px 0; border-top: 1px solid #eee; margin-top: 80px; border-bottom: 2px solid var(--gold); }
            .bio-card { max-width: 900px; margin: auto; padding: 60px; border-radius: 30px; background: #fdfaf4; }
            
            footer { padding: 60px; text-align: center; letter-spacing: 4px; color: #aaa; font-size: 0.8rem; }
        </style>
    </head>
    <body>

    <nav class="navbar"><div class="container text-center"><a href="#" class="navbar-brand">ARSVIM</a></div></nav>

    <div class="hero-header">
        <div class="container">
            <h1>ARSVIM-V3</h1>
            <p style="color: var(--gold); letter-spacing: 5px; font-weight: bold; font-size: 1.2rem;">THE FUTURE OF ROBOTICS & INFRASTRUCTURE</p>
        </div>
    </div>

    <div class="container py-5 mt-5">
        <div class="row g-5">
            {% for id, p in projects.items() %}
            <div class="col-md-4">
                <a href="/project/{{id}}" class="project-card">
                    <div class="img-wrap"><img src="{{p.image}}" alt="{{p.title}}"></div>
                    <div class="card-body">
                        <span style="color: var(--gold); font-weight: bold; letter-spacing: 2px; font-size: 0.8rem;">{{p.tag}}</span>
                        <h3 class="mt-3" style="font-weight: 300;">{{p.title}}</h3>
                        <p class="text-muted mt-3">Click for Deep Analysis</p>
                    </div>
                </a>
            </div>
            {% endfor %}
        </div>
    </div>

    <div class="bio-wrap">
        <div class="container">
            <div class="bio-card shadow-sm">
                <div class="text-center">
                    <span style="color: var(--gold); letter-spacing: 5px; font-weight: bold;">THE INNOVATOR</span>
                    <h2 class="mt-3" style="font-size: 3rem; font-weight: 200;">{{bio.name}}</h2>
                    <hr style="width: 60px; margin: 30px auto; border-top: 2px solid var(--gold); opacity: 1;">
                    <p style="font-size: 1.25rem; line-height: 2; color: #444;">
                        আমি <strong>{{bio.school}}</strong> এর <strong>{{bio.class}}</strong> এর একজন ছাত্র। <br>
                        আমার মিশন: <strong>{{bio.goal}}</strong> <br><br>
                        সায়েন্স ফেয়ার ২০২৬-এ আমার অর্জন: <span style="background: var(--gold); color: white; padding: 5px 15px; border-radius: 50px;">{{bio.achievements}}</span>
                    </p>
                </div>
            </div>
        </div>
    </div>

    <footer>© 2026 ARSVIM TECHNOLOGY | ENGINEERED IN BANGLADESH</footer>

    </body>
    </html>
    """
    return render_template_string(html, projects=projects, bio=bio_data)

# ৩. প্রজেক্টের বিস্তারিত পেজ
@app.route('/project/<project_id>')
def project_detail(project_id):
    p = projects.get(project_id)
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{p.title}} | ARSVIM Case Study</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #fff; padding: 60px 0; font-family: 'Helvetica Neue', Arial; line-height: 1.8; }
            .container-case { max-width: 850px; margin: auto; padding: 0 20px; }
            img { width: 100%; height: 500px; object-fit: cover; border-radius: 30px; box-shadow: 0 30px 60px rgba(0,0,0,0.1); }
            .section-box { border-left: 6px solid #c5a059; background: #fdfaf4; padding: 40px; margin: 40px 0; border-radius: 0 20px 20px 0; }
            h2 { color: #c5a059; font-weight: 200; font-size: 2.5rem; margin-bottom: 25px; }
            .tech-badge { border: 1px solid #c5a059; color: #c5a059; padding: 8px 20px; border-radius: 50px; margin: 5px; display: inline-block; font-size: 0.85rem; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container-case">
            <a href="/" style="color: #c5a059; text-decoration: none; font-weight: bold;">← BACK TO HUB</a>
            <img src="{{p.image}}" class="mt-5 mb-5 shadow-lg">
            <h1 style="font-size: 3.5rem; font-weight: 200; letter-spacing: 5px;">{{p.title}}</h1>
            <p style="font-size: 1.4rem; color: #555; margin-top: 30px;">{{p.overview}}</p>

            <div class="section-box">
                <h2>Technical Analysis</h2>
                <p><strong>Problem Statement:</strong> {{p.problem}}</p>
                <p><strong>Implemented Solution:</strong> {{p.solution}}</p>
                <p><strong>Unique Speciality:</strong> {{p.speciality}}</p>
            </div>

            <div class="mt-5">
                <h2>Gunnagun & Impact</h2>
                <p><strong>Main Benefits:</strong> {{p.benefits}}</p>
                <p><strong>Challenges & Limitations:</strong> {{p.bad_effects}}</p>
            </div>

            <div class="mt-5">
                <h2>Future Vision</h2>
                <p>{{p.future_scope}}</p>
            </div>

            <div class="mt-5">
                <h2>System Stack</h2>
                <div class="mt-3">
                    {% for t in p.tech %}
                    <span class="tech-badge">{{t}}</span>
                    {% endfor %}
                </div>
            </div>

            <div class="text-center mt-5 py-5">
                <a href="/" class="btn btn-outline-dark px-5 py-3 rounded-pill">BACK TO HOME</a>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, p=p)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
