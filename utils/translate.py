from deep_translator import GoogleTranslator

# deep-translator supports many providers; GoogleTranslator is lightweight for demos.
# For production, consider official APIs with keys and rate limits handled.

def translate_text(text: str, target_language: str = "en") -> str:
    """
    Translate text into target_language (ISO 639-1 codes like 'en', 'hi', 'ja', 'fr').
    If translation fails, return the original text plus a message.
    """
    try:
        # deep_translator expects language code like 'hi' 'ja' 'en'
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        # In production, log details
        return f"[Translation failed: {e}]\n\nOriginal text:\n{text}"
