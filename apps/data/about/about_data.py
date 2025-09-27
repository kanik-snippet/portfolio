from django.conf import settings
from datetime import datetime
import pytz

class AboutData:
    @staticmethod
    def is_working_hours():
        jakarta_tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(jakarta_tz)

        is_weekday = now.weekday() < 5
        is_work_hour = 15 <= now.hour < 20

        return is_weekday and is_work_hour

    @classmethod
    def get_about_data(cls):
        return {
            "name": "Kanik Gupta",
            "first_name": "Kanik",
            "last_name": "Gupta",
            "username": "kanik-snippet", # GitHub username
            "aka": "bunny",
            "image_url": settings.AUTHOR_IMG,
            "personal_website": "https://kanik.serdevice.xyz",
            "cvs": "https://drive.google.com/file/d/1K3oVOFPJs5hDq6TlMMllzJWZbC49EIvA/view",
            "cv_latest": "https://drive.google.com/file/d/1K3oVOFPJs5hDq6TlMMllzJWZbC49EIvA/view?usp=sharing",
            "cv_copy": "https://drive.google.com/file/d/1K3oVOFPJs5hDq6TlMMllzJWZbC49EIvA/view?usp=sharing",
            "role": "Python Developer",
            "is_active": cls.is_working_hours(),
            "is_open_to_work": True,
            "is_hiring": False,
            "short_description": "a quiet space where machine learning, open-source, and reflections converge.",
            "short_bio_old": "I explore through code, share with empathy, and reflect on every challenge. My work weaves machine learning, web creation, and open-source. This site archives the curious, the technical, and the quietly thoughtful.",
            "short_bio": "I explore through code, share with empathy, and reflect on every challenge. My work weaves machine learning, web creation, and open source. I thrive on collaborating with teams to develop AI and web solutions that blend function with clarity.",
            "short_cta": "Stay a while and see what lives beyond the code.",
            "long_description": "I'm a machine learning engineer and web developer, building AI apps and slick websites that solve real problems. I've memorized nearly 30 Juz of the Quran, which has wired me for grit, focus, and discipline. I've mentored 50+ coders at DBS Foundation's Coding Camp and guided 100+ interns at GAOTek Inc. I've shipped 45+ projects using TensorFlow, PyTorch, and more. I'm all in on using AI to tackle big challenges fast, growing Copilot ID, and dropping value in open-source communities.",
            "stories": [
"I’m Kanik, Founder of Serd — a company dedicated to building impactful technology products. Our flagship product, also named Serd, is where I’m currently focused full-time, bringing together my passion for development and innovation.",
"As a Python and Django developer, I specialize in crafting scalable web applications, SaaS platforms, and IoT-based solutions. Over the past year, I’ve gained hands-on experience in designing APIs, building secure systems, and developing end-to-end digital products that solve real-world problems.",
"Previously, I worked at Netzwala Service Private Limited, where I contributed to SaaS and product-based projects after completing a 4-month internship. Alongside, I’ve been freelancing and helping clients turn ideas into impactful solutions.",
"With Serd, my vision is to create technology that not only scales but also makes a meaningful difference. I’m passionate about clean architecture, performance-driven systems, and exploring mobile app development as the next big step.",
"If you’re interested in collaborating, exploring product synergies, or just talking tech and startups, let’s connect and build something transformative together. 🚀"
],
            "location": {
                "regency": "New Delhi",
                "residency": "New Delhi",
                "province": "Central Java",
                "prov": "Central Java",
                "country": "India",
                "flag": "🇮N"
            },
            "social_media": {
                "email": "bunny.official@serdevice.xyz",
                "github": "https://github.com/kanik-snippet",
                "linkedin": "https://www.linkedin.com/in/bunny0522/",
                "follow_linkedin": "https://linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=bunny0522",
                "instagram": "https://www.instagram.com/whokanikgupta/",
                "x": "https://x.com/bunnyGamer0522",
                "website": "https://kanik.serdevice.xyz",
            },
            # "donate": [
            #     {
            #         "github_sponsor": "https://github.com/sponsors/ridwaanhall",
            #         "donate_text": "Back me on GitHub Sponsors"
            #     },
            #     {
            #         "sociabuzz": "https://sociabuzz.com/ridwaanhall/support",
            #         "donate_text": "Become a patron through Sociabuzz"
            #     },
            #     {
            #         "buy_me_a_coffee": "https://www.buymeacoffee.com/ridwaanhall",
            #         "donate_text": "Support my work with a coffee"
            #     },
            #     {
            #         "saweria": "https://saweria.co/ridwaanhall",
            #         "donate_text": "Support my journey on Saweria"
            #     },
            # ],
            "skills": [
                "Python",
                "Django",
                "React.js",
                "Node.js",
                "Springboot"
            ],
        }
