#!/usr/bin/env python3

colleges = {
    "aclc-bataan.html": {
        "name": "ACLC Bataan",
        "full_name": "AMA Computer Learning Center Bataan",
        "location": "Bataan",
        "phone": "(047) 312-3456",
        "email": "info@aclc-bataan.edu.ph",
        "website": "www.aclcbataan.edu.ph"
    },
    "heroes.html": {
        "name": "Heroes College",
        "full_name": "Heroes College of the Philippines",
        "location": "Bataan",
        "phone": "(047) 234-5678",
        "email": "info@heroescollege.edu.ph",
        "website": "www.heroescollege.edu.ph"
    },
    "letran-bataan.html": {
        "name": "Letran Bataan",
        "full_name": "Colegio de San Juan de Letran Bataan",
        "location": "Bataan",
        "phone": "(047) 289-3456",
        "email": "info@letran-bataan.edu.ph",
        "website": "www.letran-bataan.edu.ph"
    },
    "csm-dinalupihan.html": {
        "name": "CSM Dinalupihan",
        "full_name": "Centro San Miguel Dinalupihan",
        "location": "Dinalupihan, Bataan",
        "phone": "(047) 245-6789",
        "email": "info@csm-dinalupihan.edu.ph",
        "website": "www.csm-dinalupihan.edu.ph"
    },
    "lpc.html": {
        "name": "Lyceum-Pacific College",
        "full_name": "Lyceum-Pacific College",
        "location": "Bataan",
        "phone": "(047) 267-8901",
        "email": "info@lpc-bataan.edu.ph",
        "website": "www.lpc-bataan.edu.ph"
    },
    "maap.html": {
        "name": "MAAP College",
        "full_name": "MAAP College of Bataan",
        "location": "Bataan",
        "phone": "(047) 278-9012",
        "email": "info@maap-bataan.edu.ph",
        "website": "www.maap-bataan.edu.ph"
    },
    "mcbt.html": {
        "name": "MCBT",
        "full_name": "Mindanao College of Bataan and Techno",
        "location": "Bataan",
        "phone": "(047) 289-0123",
        "email": "info@mcbt.edu.ph",
        "website": "www.mcbt.edu.ph"
    },
    "pup-bataan.html": {
        "name": "PUP Bataan",
        "full_name": "Polytechnic University of the Philippines Bataan",
        "location": "Bataan",
        "phone": "(047) 224-5678",
        "email": "bataan@pup.edu.ph",
        "website": "www.pup.edu.ph"
    },
    "pwu-cdcec.html": {
        "name": "PWU CDCEC",
        "full_name": "Philippine Women's University CDCEC",
        "location": "Bataan",
        "phone": "(047) 234-5678",
        "email": "cdcec@pwu.edu.ph",
        "website": "www.pwu.edu.ph"
    }
}

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Campus Details</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f5f5;
            color: #333;
        }}

        /* Header */
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .logo {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .logo-icon {{
            width: 40px;
            height: 40px;
            background: #2542ff;
            border-radius: 8px;
        }}

        .logo-text h1 {{
            font-size: 1.2rem;
            color: #2542ff;
        }}

        .logo-text p {{
            font-size: 0.7rem;
            color: #666;
        }}

        nav {{
            display: flex;
            gap: 2rem;
        }}

        nav a {{
            text-decoration: none;
            color: #333;
            font-weight: 500;
            padding: 0.5rem 1rem;
            transition: all 0.3s;
        }}

        nav a:hover, nav a.active {{
            color: #2542ff;
        }}

        /* Back Button */
        .back-btn {{
            background: white;
            padding: 1rem 5%;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            cursor: pointer;
            border: none;
            width: 100%;
            text-align: left;
            font-size: 1rem;
            color: #2542ff;
            transition: all 0.3s;
        }}

        .back-btn:hover {{
            background: #f8f9fa;
        }}

        /* Main Container */
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem 5%;
        }}

        /* Campus Header Card */
        .campus-header {{
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: grid;
            grid-template-columns: auto 1fr auto;
            gap: 2rem;
            align-items: start;
        }}

        .campus-logo {{
            width: 120px;
            height: 120px;
            background: #f0f0f0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            color: #999;
            text-align: center;
        }}

        .campus-info h1 {{
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            color: #333;
        }}

        .campus-subtitle {{
            color: #666;
            margin-bottom: 1.5rem;
            font-size: 1rem;
        }}

        .info-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }}

        .info-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
        }}

        .info-icon {{
            color: #2542ff;
            font-size: 1.2rem;
        }}

        .campus-map {{
            width: 300px;
            height: 200px;
            background: #e9ecef;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #999;
            font-size: 0.9rem;
        }}

        /* Action Buttons */
        .action-buttons {{
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }}

        .btn {{
            padding: 0.8rem 2rem;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            border: none;
            font-size: 0.95rem;
        }}

        .btn-primary {{
            background: #2542ff;
            color: white;
        }}

        .btn-primary:hover {{
            background: #1a32cc;
        }}

        /* Content Grid */
        .content-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }}

        .main-content {{
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        .sidebar {{
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        /* Section Card */
        .section-card {{
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .section-header {{
            background: #2542ff;
            color: white;
            padding: 0.8rem 1.5rem;
            margin: -2rem -2rem 1.5rem -2rem;
            border-radius: 15px 15px 0 0;
            font-size: 1.1rem;
            font-weight: 600;
        }}

        .contact-info {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 0.8rem;
            padding: 1rem;
            background: #f8f9fa;
            border-radius: 8px;
            font-size: 0.9rem;
        }}

        .contact-icon {{
            color: #2542ff;
            font-size: 1.3rem;
        }}

        /* Footer */
        footer {{
            background: #1a1a1a;
            color: white;
            padding: 2rem 5%;
            margin-top: 3rem;
        }}

        .footer-content {{
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 2rem;
        }}

        .footer-section h3 {{
            margin-bottom: 1rem;
            color: #2542ff;
        }}

        .footer-section p, .footer-section a {{
            color: #ccc;
            font-size: 0.9rem;
            line-height: 1.8;
            text-decoration: none;
        }}

        .footer-section a:hover {{
            color: #2542ff;
        }}

        .footer-links {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .footer-bottom {{
            text-align: center;
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid #333;
            color: #999;
            font-size: 0.9rem;
        }}

        /* Responsive */
        @media (max-width: 1024px) {{
            .content-grid {{
                grid-template-columns: 1fr;
            }}

            .campus-header {{
                grid-template-columns: 1fr;
            }}

            .campus-map {{
                width: 100%;
            }}

            .footer-content {{
                grid-template-columns: 1fr;
            }}
        }}

        @media (max-width: 768px) {{
            nav {{
                display: none;
            }}

            .info-grid {{
                grid-template-columns: 1fr;
            }}

            .action-buttons {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">
            <div class="logo-icon"></div>
            <div class="logo-text">
                <h1>Bataan Campus Finder</h1>
                <p>Campus Details</p>
            </div>
        </div>
        <nav>
            <a href="../home.html">HOME</a>
            <a href="../campus.html" class="active">ALL CAMPUSES</a>
            <a href="../about.html">ABOUT</a>
            <a href="../contact.html">CONTACT</a>
        </nav>
    </header>

    <button class="back-btn" onclick="window.history.back()">
        ← Back to All Campuses
    </button>

    <div class="container">
        <div class="campus-header">
            <div class="campus-logo">
                Logo
            </div>
            <div class="campus-info">
                <h1>{full_name}</h1>
                <p class="campus-subtitle">Main Campus</p>
                <div class="info-grid">
                    <div class="info-item">
                        <span class="info-icon">📍</span>
                        <span>{location}, Bataan</span>
                    </div>
                    <div class="info-item">
                        <span class="info-icon">📞</span>
                        <span>{phone}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-icon">🌐</span>
                        <span>{website}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-icon">✉️</span>
                        <span>{email}</span>
                    </div>
                </div>
                <div class="action-buttons">
                    <button class="btn btn-primary">LEARN MORE</button>
                </div>
            </div>
            <div class="campus-map">
                Map Coming Soon
            </div>
        </div>

        <div class="content-grid">
            <div class="main-content">
                <div class="section-card">
                    <div class="section-header">OVERVIEW</div>
                    <p style="color: #666; line-height: 1.6; margin-bottom: 1rem;">
                        {name} is a leading educational institution in Bataan dedicated to providing quality higher education. The institution is committed to fostering academic excellence, student development, and community engagement.
                    </p>
                    <p style="color: #666; line-height: 1.6;">
                        With experienced faculty, modern facilities, and comprehensive programs, {name} offers students an excellent platform for personal and professional growth in today's competitive world.
                    </p>
                </div>
            </div>

            <div class="sidebar">
                <div class="section-card">
                    <div class="section-header">CONTACT INFORMATION</div>
                    <div class="contact-info">
                        <div class="contact-item">
                            <span class="contact-icon">📞</span>
                            <div>
                                <strong>Phone</strong><br>
                                {phone}
                            </div>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">✉️</span>
                            <div>
                                <strong>Email</strong><br>
                                {email}
                            </div>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">🌐</span>
                            <div>
                                <strong>Website</strong><br>
                                {website}
                            </div>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">📍</span>
                            <div>
                                <strong>Address</strong><br>
                                {location}, Bataan
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>Bataan Campus Finder</h3>
                <p>Your comprehensive guide to higher education institutions in Bataan. Discover programs, compare options, and find the perfect campus for your future.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <div class="footer-links">
                    <a href="../home.html">Home</a>
                    <a href="../campus.html">All Campuses</a>
                    <a href="../about.html">About Us</a>
                    <a href="../contact.html">Contact</a>
                </div>
            </div>
            <div class="footer-section">
                <h3>Need Help?</h3>
                <p>Contact us for any inquiries about higher education in Bataan.</p>
                <p style="margin-top: 1rem;">
                    Email: info@bataancampusfinder.com<br>
                    Phone: (047) XXX-XXXX
                </p>
            </div>
        </div>
        <div class="footer-bottom">
            © 2024 Bataan Campus Finder. All rights reserved. | Designed with ❤️ for Bataan Students
        </div>
    </footer>

    <script src="../assets/js/schools-data.js"></script>
</body>
</html>'''

import os

base_path = "c:\\Users\\YUKI\\Documents\\Bataan-Campus-Finder\\schools"

for filename, college_info in colleges.items():
    filepath = os.path.join(base_path, filename)
    
    content = template.format(
        name=college_info["name"],
        full_name=college_info["full_name"],
        location=college_info["location"],
        phone=college_info["phone"],
        email=college_info["email"],
        website=college_info["website"]
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {filename}")

print("\n✓ All 9 college pages have been updated with the template!")
