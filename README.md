# GymBuddy

Welcome to GymBuddy, a fitness platform developed by a passionate team with a commitment to your health and well-being!

## Introduction

GymBuddy is a Django project crafted by a student from Lithuania. This platform is designed to revolutionize your fitness journey, combining cutting-edge technology with expert guidance to provide personalized meal and workout plans tailored to your unique needs and preferences. Whether you're aiming to gain muscle, lose weight, or maintain a healthy lifestyle, GymBuddy is your ultimate fitness companion.

## Features

- **Profile Data:** Create and manage personalized profiles, including fitness goals, dietary preferences, and specific requirements.
- **OpenAI Integration:** Harness the power of OpenAI for intelligent and personalized meal and workout plans.
- **Personalized Meal Plans:** Crafted meal plans aligned with your caloric needs, dietary preferences, and fitness goals.
- **Tailored Workout Plans:** Generate workout plans catering to your fitness level, preferences, and specific target areas.
- **Community Support:** Join a community of like-minded individuals striving for better health and receive guidance from our team of fitness experts.

## Installation

To run GymBuddy locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/GymBuddy.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your database: `python manage.py migrate`
4. Create a superuser account: `python manage.py createsuperuser`
5. Install and run Redis server:

    - **Linux:**
        ```bash
        sudo apt-get install redis-server
        ```

    - **Mac:**
        ```bash
        brew install redis
        ```

    - **Windows:**
        Download and install Redis from the [official Redis website](https://redis.io/download).

6. Install and configure Celery:

    - Install Celery:
        ```bash
        pip install celery
        ```

    - In your Django project directory, create a `celery.py` file and update your `settings.py` as described in the GymBuddy README.

7. Run Celery:
    ```bash
    celery -A your_project worker -l info
    ```

8. Run the development server:
    ```bash
    python manage.py runserver
    ```

Now, access GymBuddy by navigating to `http://localhost:8000` in your web browser.

Join GymBuddy today and embark on a journey to a healthier, happier you!
