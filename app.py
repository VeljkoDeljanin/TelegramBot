import os

import telebot
import yt_dlp
from urllib.parse import urlparse

bot = telebot.TeleBot("6275176649:AAEBuWf6GlYeVWGoOdBrKSJHQvPTY2BYFhw")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello, welcome to my bot! Send me a link to a video to get started.")


def is_valid_url(url):
    """Check if the given URL is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def download_and_convert_video(url, file_path):
    """Downloads and converts a video to MP4 format using yt-dlp"""
    try:
        # Create a yt-dlp object with the appropriate options for video conversion
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': file_path
        }
        ydl = yt_dlp.YoutubeDL(ydl_opts)

        # Download and convert the video using yt-dlp
        ydl.download([url])
        return True
    except Exception as e:
        print(f"Error downloading and converting video: {e}")
        return False


@bot.message_handler(func=lambda message: True)
def handle_video_url(message):
    """Handles messages containing valid video URLs"""
    try:
        url = message.text.strip()

        # Check if the message contains a valid video URL
        if not is_valid_url(url):
            bot.reply_to(message, "The provided URL is not a valid video.")
            return

        # Download and convert the video to MP4 format
        video_file = 'video.mp4'
        download_and_convert_video(url, video_file)

        # Send the video file to the user as a media document
        with open(video_file, 'rb') as f:
            bot.send_document(message.chat.id, f, timeout=30)

        # Delete the video file after sending it to the user
        os.remove(video_file)

    except Exception as e:
        bot.reply_to(message, f"Error processing the video URL: {e}")


bot.polling()
