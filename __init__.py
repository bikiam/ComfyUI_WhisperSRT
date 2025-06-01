from .Whisper_text_srt import WhisperAudioToSRTText
# Node registration
NODE_CLASS_MAPPINGS = {
    "WhisperAudioToSRTText": WhisperAudioToSRTText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WhisperAudioToSRTText": "🗣️Whisper Audio to Text+SRT"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
