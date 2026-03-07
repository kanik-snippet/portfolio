from django.conf import settings

class ExperiencesData:
    '''
    employment type:
    - Full-time (Pekerjaan penuh waktu)
    - Part-time (Pekerjaan paruh waktu)
    - Self-employed (Pekerjaan mandiri)
    - Freelance (Pekerjaan lepas)
    - Contract (Pekerjaan berdasarkan kontrak)
    - Internship (Magang)
    - Apprenticeship (Pelatihan kerja atau magang kejuruan)
    - Seasonal (Pekerjaan musiman)
    
    location type:
    - On-site: Bekerja langsung di lokasi fisik (contoh: kantor).
    - Hybrid: Kombinasi antara bekerja dari lokasi fisik dan jarak jauh.
    - Remote: Sepenuhnya bekerja jarak jauh (contoh: dari rumah).
    '''
    
    employment_types = {
        "ft": "Full-time",
        "fn":"Founder",
        "pt": "Part-time",
        "se": "Self-employed",
        "fr": "Freelance",
        "co": "Contract",
        "in": "Internship",
        "ap": "Apprenticeship",
        "sn": "Seasonal",
        "sc": "Scholarship"
    }
    
    location_types = {
        "on": "On-site",
        "hy": "Hybrid",
        "rm": "Remote"
    }
    
    experiences = [
        {
            "id": 13,
            "title": "Alessar Solutions Private Limited",
            "company": " Smart Emergency Response Device ",
            "logo": f"{settings.BASE_URL}/static/img/logo/ice.webp",
            "website": "https://www.serd-button.in",
            "period": {
                "start": {
                    "month": "July",
                    "year": 2025
                },
                "end": "Present"
            },
            "employment_type": employment_types["fn"],
            "location_type": location_types["rm"],
            "location": "New Delhi, India 🇮🇳",
            "is_current": True,
           "responsibilities": [
"Founded and leading the development of <strong>SERD (Smart Emergency Response Device)</strong>, an IoT-based safety system designed to trigger instant emergency alerts during critical situations.",
"Designed and developed the hardware architecture using <strong>Raspberry Pi, push-button trigger system, and camera module</strong> to capture real-time evidence during emergencies.",
"Built the backend infrastructure using <strong>Django and REST APIs</strong> to process SOS events, manage device communication, and securely store captured media.",
"Implemented automated <strong>SOS alert workflows</strong> that instantly notify registered emergency contacts through SMS, phone calls, and secure media links.",
"Integrated <strong>geolocation tracking</strong> to automatically capture and share the exact location of incidents during emergency activation.",
"Designed a scalable device-to-server communication architecture ensuring <strong>low-latency real-time synchronization</strong> between hardware and backend services.",
"Currently developing and expanding SERD as a flagship product under <strong>Alessar Solutions</strong>, with a successfully filed <strong>patent application</strong> for the innovation."
]   },
{
            "id": 14,
            "title": "Founder – SERD (Smart Emergency Response Device)",
            "company": "ACIC MIET Incubation Center",
            "logo": f"{settings.BASE_URL}/static/img/logo/miet.png",
            "website": "https://miet.ac.in/",
            "period": {
                "start": {"month": "Aug", "year": 2024},
                "end": "Present"
            },
            "employment_type": employment_types["fn"],
            "location_type": location_types["on"],
            "location": "Meerut, India 🇮🇳",
            "is_current": True,

            "responsibilities": [

                "Signed an official MOU with ACIC MIET as an incubated founder.",

                "Developing SERD Button, an IoT-based emergency response device designed to trigger real-time SOS alerts.",

                "ACIC supported the complete patent filing process for the innovation.",

                "Designed and built a working prototype including Raspberry Pi integration, hardware components, and camera modules.",

                "Developed product casing through 3D design and 3D printing.",

                "Built backend services using Django and REST APIs for device communication.",

                "Implemented automated emergency alerts including SMS, phone calls, and live location sharing.",

                "Collaborated with ACIC mentors and technical teams to refine product architecture."
            ]
        },
        {
            "id": 12,
            "title": "Alessar Solutions Private Limited",
            "company": "Bharat Sanhaar Nigam",
            "logo": f"{settings.BASE_URL}/static/img/logo/bsn.gif",
            "website": "https://github.com/kanik-snippet/bharat-sanchaar-nigam",
            "period": {
                "start": {
                    "month": "June",
                    "year": 2025
                },
                "end": "Present"
            },
            "employment_type": employment_types["fn"],
            "location_type": location_types["rm"],
            "location": "New Delhi, India 🇮🇳",
            "is_current": True,
            "responsibilities": [
"Designed and developed <strong>Bharat Sanchaar Nigam</strong>, a hierarchical location-based news and communication platform built with Django.",
"Implemented a structured governance model allowing different administrative roles such as <strong>Sabhasad, Chairman, Vidhayak, CM, and PM</strong> to publish updates at respective jurisdiction levels.",
"Developed location-aware content filtering logic ensuring users receive news based on their <strong>state, district, city, and ward</strong> hierarchy.",
"Built secure backend APIs for content publishing, user role management, and dynamic news distribution.",
"Designed the system architecture to support scalable public communication between government representatives and citizens."
]
        },
        {
            "id": 11,
            "title": "Netzwala Service Private Limited",
            "company": "Desktop App",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://github.com/kanik-snippet/desktop-app",
            "period": {
                "start": {
                    "month": "Aug",
                    "year": 2024
                },
                "end": {
                    "month": "Sep",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["on"],
            "location": "Okhla Newdelhi, India 🇮n",
            "is_current": False,
            "responsibilities": [
"Contributed to the development of a <strong>cross-platform desktop application</strong> designed to streamline internal workflows and productivity tasks.",
"Worked on backend integrations and system logic while improving application stability and performance.",
"Collaborated with team members to implement user-focused features and maintain efficient project workflows.",
"Participated in debugging, testing, and optimizing application modules to ensure smooth production deployment."
]
        },
        {
            "id": 10,
            "title": "Netzwala Service Private Limited",
            "company": "Post-Book",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://github.com/kanik-snippet/postbook",
            "period": {
                "start": {
                    "month": "July",
                    "year": 2024
                },
                "end": {
                    "month": "Aug",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["on"],
            "location": "Okhla Newdelhi, India 🇮n",
            "is_current": False,
            "responsibilities": [
"Worked on the development of <strong>PostBook</strong>, a social-style content management platform built with modern web technologies.",
"Designed backend APIs and implemented features for post creation, user interactions, and content management.",
"Gained hands-on experience working with scalable backend architectures and database management.",
"Collaborated with the development team to improve system performance and feature reliability."
]
        }
       
    ]
