"""middleware"""

class CustomHeaderMiddleware:
    """
    Middleware to add custom header to the response
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add custom header to the response
        response = self.get_response(request)
        response['X-Custom-Header'] = 'Hello from Custom Middleware'
        return response