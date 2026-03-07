from django.conf import settings

class EducationData:

    education = [

        {
            "degree": "Computer Science and Engineering",
            "alias": "Bachelor of Technology",
            "date": {
                "start": {"year": 2021, "month": "Sep"},
                "end": {"year": 2024, "month": "July"}
            },

            "institution": "Meerut Institute of Engineering and Technology",
            "website": "https://miet.ac.in/",
            "logo": f"{settings.BASE_URL}/static/img/logo/miet.png",
            "is_last": True,

            "location": {
                "regency": "Meerut",
                "province": "Uttar Pradesh",
                "prov": "Uttar Pradesh",
                "country": "India",
                "flag": "🇮🇳"
            },

            # NEW FIELD
            "tech_focus": [
                "Full Stack Development",
                "Robotics Engineering",
                "IoT Systems",
                "Backend Architecture",
                "Machine Learning"
            ],

            # NEW FIELD
            "robotics_achievements": [
                "🥇 Gold Medal – Bot Combat (World Techoxian Championship)",
                "🥉 Bronze Medal – Bot Combat (World Techoxian Championship)",
                "🥉 Bronze Medal – Bot Combat (World Techoxian Championship)"
            ],

            "achievements": [
                "Participated in robotics competitions including Bot Combat, RC Racing, and Sumo Bots.",
                "Collaborated with Mechanical Engineering students to design and build combat robots.",
                "Worked hands-on in mechanical laboratories performing metal cutting and robot fabrication.",
                "Represented the team in the international World Techoxian Championship robotics competition.",
                "Built interdisciplinary engineering skills combining mechanical design, electronics, and programming."
            ]
        },

        {
            "degree": "Diploma in Computer Science and Engineering",
            "years": "2017 - 2021",
            "institution": "Digamber Jain Polytechnic",
            "website": "https://djpbaraut.com/",
            "logo": f"{settings.BASE_URL}/static/img/logo/djp.jpg",
            "is_last": False,

            "location": {
                "regency": "Baraut",
                "province": "Uttar Pradesh",
                "prov": "Uttar Pradesh",
                "country": "India",
                "flag": "🇮🇳"
            },

            "tech_focus": [
                "Programming Fundamentals",
                "HTML",
                "CSS",
                "PHP",
                "Database Basics"
            ],

            "achievements": [
                "Developed early web projects using HTML, CSS, and PHP.",
                "Built strong programming foundations and software development skills.",
                "Participated in collaborative technical projects and debugging exercises."
            ]
        },

        {
            "degree": "High School",
            "years": "2016 - 2017",
            "institution": "Shri Ram Inter College",
            "website": "https://www.instagram.com/",
            "logo": f"{settings.BASE_URL}/static/img/logo/shri.webp",
            "is_last": False,

            "location": {
                "regency": "Baraut",
                "province": "Uttar Pradesh",
                "prov": "Uttar Pradesh",
                "country": "India",
                "flag": "🇮🇳"
            },

            "achievements": [
                "Developed an early interest in computers and technology.",
                "Started learning the basics of web development and programming."
            ]
        }

    ]