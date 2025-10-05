from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests # جایگزین کتابخانه گوگل شد
from django.conf import settings

def chat_view(request):
    """
    این ویو صفحه اصلی چت با دستیار هوشمند را نمایش می‌دهد.
    """
    return render(request, '../templates/chat.html')

@csrf_exempt
def get_ai_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            if not user_message:
                return JsonResponse({'error': 'پیامی دریافت نشد'}, status=400)

            # آدرس API از فایل تنظیمات خوانده می‌شود
            api_url = settings.LM_STUDIO_API_URL

            # ساختار پیام برای ارسال به LM Studio (سازگار با OpenAI)
            payload = {
                "model": "qwen2-nextgen-8b", # مهم: نام مدل خود را در اینجا قرار دهید
                "messages": [
                    {"role": "system", "content": "شما یک دستیار متخصص در زمینه میکسرهای صنعتی هستید و به زبان فارسی پاسخ می‌دهید."},
                    {"role": "user", "content": user_message}
                ],
                "temperature": 0.7,
            }

            headers = {
                "Content-Type": "application/json"
            }

            # ارسال درخواست به سرور محلی LM Studio
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()  # اگر خطایی رخ دهد، استثنا ایجاد می‌کند

            response_data = response.json()
            ai_response = response_data['choices'][0]['message']['content']

            return JsonResponse({'response': ai_response})

        except requests.exceptions.RequestException as e:
            error_message = f"خطا در ارتباط با سرور LM Studio: {e}"
            print(error_message)
            return JsonResponse({'error': "قادر به اتصال به سرور محلی LM Studio نیستم. لطفاً مطمئن شوید که سرور در حال اجراست."}, status=500)
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 
            return JsonResponse({'error': f"یک خطای پیش‌بینی نشده رخ داد: {e}"}, status=500)
            
    return JsonResponse({'error': 'درخواست نامعتبر'}, status=400)

