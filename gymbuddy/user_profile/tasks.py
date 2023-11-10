from celery import shared_task

@shared_task
def generate_chat_advice_task(profile_id):
    from .models import Profile
    profile = Profile.objects.get(pk=profile_id)
    if created or not instance.get_chat_advice():
            if instance.is_complete():
                    client = OpenAI(
                        api_key="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",
                    )
                    conversation = f"User Profile:\nHeight: {instance.height} cm.\nWeight: {instance.weight} kg.\nAge: {instance.age} years old.\nGender: {instance.get_gender_display()}\nActivity Level: {instance.get_activity_level_display()}\nWeight Goal: {instance.get_weight_goal_display()}"
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
                    instance.set_chat_advice(chat_response)