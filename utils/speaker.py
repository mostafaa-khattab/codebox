import asyncio
import os
import re
import tempfile


import edge_tts


class Speaker:
    """Professional Text-To-Speech system for CodeBox."""

    def __init__(self):
        self.arabic_voice = "ar-EG-SalmaNeural"
        self.english_voice = "en-US-JennyNeural"

    # ==========================================
    # Clean Text
    # ==========================================

    def clean_text(self, text: str) -> str:

        if not text:
            return ""

        # Remove code blocks
        text = re.sub(
            r"```.*?```",
            "",
            text,
            flags=re.DOTALL,
        )

        # Remove bold / italic Markdown
        text = text.replace("**", "")
        text = text.replace("__", "")
        text = text.replace("*", "")
        text = text.replace("_", " ")

        # Remove headings
        text = re.sub(
            r"^#+\s*",
            "",
            text,
            flags=re.MULTILINE,
        )

        # Convert Markdown links to text
        text = re.sub(
            r"\[([^\]]+)\]\([^)]+\)",
            r"\1",
            text,
        )

        # Remove inline code markers
        text = text.replace("`", "")

        # Remove bullet symbols
        text = re.sub(
            r"^\s*[-•]\s*",
            "",
            text,
            flags=re.MULTILINE,
        )

        # Remove excessive spaces
        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        return text.strip()

    # ==========================================
    # Detect Language
    # ==========================================

    def is_arabic(self, text: str) -> bool:

        arabic_count = 0
        english_count = 0

        for char in text:

            if "\u0600" <= char <= "\u06ff":
                arabic_count += 1

            elif char.isalpha():
                english_count += 1

        return arabic_count > english_count

    # ==========================================
    # Generate Audio
    # ==========================================

    async def _generate_audio(
        self,
        text,
        voice,
        filename,
    ):

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="+0%",
            volume="+0%",
        )

        await communicate.save(filename)

    # ==========================================
    # Speak — returns MP3 bytes for st.audio()
    # ==========================================

    def speak(self, text: str) -> bytes | None:
        """Generate TTS audio and return MP3 bytes.

        The caller is responsible for playing the audio
        (e.g. via st.audio(bytes, format='audio/mp3', autoplay=True)).
        Returns None if generation fails.
        """

        text = self.clean_text(text)

        if not text:
            return None

        temp_file = None

        try:

            # Select voice
            voice = (
                self.arabic_voice
                if self.is_arabic(text)
                else self.english_voice
            )

            # Write to a temporary MP3 file
            with tempfile.NamedTemporaryFile(
                suffix=".mp3",
                delete=False,
            ) as file:
                temp_file = file.name

            # Generate audio via edge-tts
            asyncio.run(
                self._generate_audio(
                    text,
                    voice,
                    temp_file,
                )
            )

            # Read bytes and return them
            with open(temp_file, "rb") as f:
                return f.read()

        except Exception as error:
            print(f"Speech Error: {error}")
            return None

        finally:
            if temp_file and os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

    # ==========================================
    # Stop (no-op — browser handles playback)
    # ==========================================

    def stop(self):
        """Playback is handled by the browser; nothing to stop server-side."""
        pass

    # ==========================================
    # Status (no-op — browser handles playback)
    # ==========================================

    def is_playing(self) -> bool:
        """Playback is handled by the browser; always returns False."""
        return False

    # ==========================================
    # Cleanup (no-op)
    # ==========================================

    def cleanup(self):
        pass