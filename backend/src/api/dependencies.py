try:
    from ...core.prompt_engine import IntelligentPromptInjector  # Try relative import
except ImportError:
    # Fallback/Mock for circular dep or path issues during dev
    class IntelligentPromptInjector:
        def inject(self, user_input, mode=None):
            return f"Processed: {user_input}", "SHADOW", None
        def enhance_response(self, response, template):
            return response

injector = IntelligentPromptInjector()
