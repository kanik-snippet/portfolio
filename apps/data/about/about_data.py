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
"I’m <strong>Kanik Gupta</strong>, a full-stack developer and the founder of <strong>Alessar Solutions</strong>, a technology company focused on building meaningful digital products and real-world solutions. My journey into development started with curiosity about how systems work behind the scenes, and over time that curiosity evolved into a passion for creating scalable products and solving real problems through technology.",

"At <strong>Alessar Solutions</strong>, I’m currently working on one of our flagship innovations — the <strong>Serd Button</strong>. It is designed as an emergency-response solution aimed at improving safety and accessibility during critical situations. The concept has already been <strong>successfully filed for a patent</strong>, marking an important milestone in turning this idea into a real product that can create meaningful impact.",

"As a <strong>Full-Stack Developer</strong>, I work across multiple layers of technology — from backend architecture and APIs to modern web interfaces and connected systems. My focus is on building <strong>scalable web applications</strong>, <strong>SaaS platforms</strong>, and <strong>robust backend systems</strong> that are efficient, secure, and ready for real-world scale.",

"Along with my personal work, I collaborate with a team of <strong>enthusiastic developers</strong> who share the same passion for building technology. Together we help startups and businesses develop products across multiple domains including <strong>web applications</strong>, <strong>websites</strong>, <strong>mobile apps</strong>, <strong>desktop software</strong>, <strong>AI chatbots</strong>, <strong>IoT projects</strong>, and <strong>machine learning models</strong> — using whichever tech stack best fits the problem.",

"Our mission at <strong>Alessar Solutions</strong> is not just to build software, but to build <strong>technology products that solve real-world problems</strong>. Whether it's helping startups turn ideas into scalable platforms or developing innovative products like the <strong>Serd Button</strong>, we focus on creating solutions that combine <strong>innovation, reliability, and performance</strong>.",

"I’m always <strong>open to collaborations</strong>, partnerships, and ambitious projects. If you’re building something exciting or need a team that can help transform your idea into a real product, feel free to connect — let’s build something impactful together."
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
