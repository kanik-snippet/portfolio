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
            "title": "SERD",
            "company": " Smart Emergency Response Device ",
            "logo": f"{settings.BASE_URL}/static/img/logo/ice.webp",
            "website": "https://serdevice.xyz",
            "period": {
                "start": {
                    "month": "July",
                    "year": 2025
                },
                "end": "Present"
            },
            "employment_type": employment_types["fn"],
            "location_type": location_types["rm"],
            "location": "Solo, India 🇮n",
            "is_current": True,
           "responsibilities": [
"Engineered IoT-enabled emergency system integrating Raspberry Pi, push-button hardware, and camera module for real-time SOS activation.",
"Developed backend services in Django to trigger instant video/audio recording upon button press with secure storage.",
"Implemented automated alert workflows sending SMS and call notifications to pre-registered SOS contacts with recorded media links.",
"Integrated geolocation services to capture and share the exact location of the incident alongside alerts.",
"Designed scalable APIs to handle device-to-server communication and SOS event logging with authentication and security layers.",
"Optimized system for low-latency event response ensuring real-time synchronization between device, server, and user contacts.",
"Deployed system with monitoring, logging, and fault recovery mechanisms for reliable 24/7 emergency response operations."
]   },
        {
            "id": 12,
            "title": "SERD",
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
            "location": "Solo, India 🇮n",
            "is_current": True,
            "responsibilities": [
                "Managed data for over 200 alumni, including advanced filtering and data visualization.",
                "Prepared organizational documents and meeting notes.",
                "Designed user-friendly interfaces for alumni management."
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
                "Led weekly mentoring sessions for 24 students, resulting in a 75% graduation rate and maintaining an average attendance of 84%.",
                "Led weekly mentoring sessions on beginner-friendly machine learning and soft skills for non-tech audiences, using simplified concepts and relatable examples.",
                "Provided 1.5 hours per week of personalized one-on-one sessions, addressing individual challenges and academic assignments to support student development.",
                "Conducted alternating weekly sessions on soft and technical skills (2 hours/week) for 50 participants, managing facilitator coordination, content preparation, session moderation, and cohort engagement monitoring.",
                "Participated in monthly 1.5-hour meetings and professional development sessions for mentors."
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
                "Acquired comprehensive knowledge of ML Ops to develop robust and scalable machine learning systems.",
                "Gained practical experience in deploying machine learning models in real-world production environments."
            ]
        }
       
    ]
