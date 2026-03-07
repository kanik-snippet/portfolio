from django.conf import settings


class AwardsData:

    awards = [

        {
            "id": 1,
            "title": "Gold Medal – Bot Combat | World Techoxian Championship",
            "credential_url": "",
            "description": "Secured Gold Medal in the Bot Combat category at the World Techoxian Championship, an international robotics competition often referred to as the robotics world cup. Designed and built a combat robot in collaboration with a multidisciplinary engineering team.",
            "issued": {
                "month": "Aug",
                "year": 2023
            },
            "institution": "World Techoxian Championship",
            "website": "https://www.techoxian.com/",
            "logo": f"{settings.BASE_URL}/static/img/logo/techoxian.png",
        },

        {
            "id": 2,
            "title": "Bronze Medal – Bot Combat | World Techoxian Championship",
            "credential_url": "",
            "description": "Achieved Bronze Medal in the Bot Combat competition at the World Techoxian Championship for designing and building a high-performance combat robot capable of competing at international level robotics events.",
            "issued": {
                "month": "Aug",
                "year": 2022
            },
            "institution": "World Techoxian Championship",
            "website": "https://www.techoxian.com/",
            "logo": f"{settings.BASE_URL}/static/img/logo/techoxian.png",
        },

        {
            "id": 3,
            "title": "Bronze Medal – Bot Combat | World Techoxian Championship",
            "credential_url": "",
            "description": "Secured Bronze Medal in the Bot Combat category at the World Techoxian Championship, competing with custom engineered combat robots built through interdisciplinary collaboration between mechanical and software engineering teams.",
            "issued": {
                "month": "Aug",
                "year": 2024
            },
            "institution": "World Techoxian Championship",
            "website": "https://www.techoxian.com/",
            "logo": f"{settings.BASE_URL}/static/img/logo/techoxian.png",
        },

        {
            "id": 4,
            "title": "Robotics Competition Participant – RC Racing & Sumo Bots",
            "credential_url": "",
            "description": "Actively participated in robotics competitions including RC Racing and Sumo Bot challenges, focusing on robot design, mechanical fabrication, and control systems development.",
            "issued": {
                "month": "Apr",
                "year": 2023
            },
            "institution": "Technical Robotics Competitions",
            "website": "",
            "logo": f"{settings.BASE_URL}/static/img/logo/robotics.png",
        },

        {
            "id": 5,
            "title": "Startup Incubation Recognition – ACIC MIET",
            "credential_url": "",
            "description": "Selected for startup incubation under ACIC MIET for developing the SERD Button, an IoT based emergency response device. Received support for patent filing, hardware prototyping, component sourcing, and 3D printed product casing development.",
            "issued": {
                "month": "Sep",
                "year": 2024
            },
            "institution": "ACIC MIET Incubation Center",
            "website": "https://miet.ac.in/",
            "logo": f"{settings.BASE_URL}/static/img/logo/miet.png",
        }

    ]