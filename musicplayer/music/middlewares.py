from django.shortcuts import redirect

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/SoundSphere/home/') and not request.user.is_authenticated:
            return redirect('signup')
        response = self.get_response(request)
        return response