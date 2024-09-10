import logging


logger = logging.getLogger(__name__)

class CacheLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if getattr(response, 'from_cache', False):
            logger.info(f"Cached page is being rendered for: {request.path}")
            print(f"Cached page is being rendered for: {request.path}")
        else:
            print("Not caching")
        
        return response
