from celery import shared_task
from openai import OpenAI

@shared_task
def generate_chat_advice_task(profile_id):
    from .models import Profile
    profile = Profile.objects.get(pk=profile_id)
    if not profile.get_chat_advice():
            if profile.is_complete():
                    client = OpenAI(
                        api_key="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",
                    )
                    conversation = f"User Profile:\nHeight: {profile.height} cm.\nWeight: {profile.weight} kg.\nAge: {profile.age} years old.\nGender: {profile.get_gender_display()}\nActivity Level: {profile.get_activity_level_display()}\nWeight Goal: {profile.get_weight_goal_display()}"
                    messages = [
                        {
                            "role": "system",
                            "content": "Be super straightforward and simple. You are the good trainer and nutritionist. Give a detailed meal plan with calories count and a detailed workout plan in the gym with reps count for the given user profile data and rest plan. Don't write that you were given this data. Just give the answer.",
                        },
                        {
                            "role": "user",
                            "content": conversation,
                        }
                    ]
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=messages
                    )
                    chat_response = response.choices[0].message.content.strip()
                    profile.set_chat_advice(chat_response)