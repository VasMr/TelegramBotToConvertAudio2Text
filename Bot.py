import telebot
import speech_recognition as sr
import soundfile as sf


bot = telebot.TeleBot('6086807016:AAFxwSbXkmzPnX2aUqPPasPjWdUSzxRV4mY')


def convert_from_mp3(srcw):
    r = sr.Recognizer()
    harvard = sr.AudioFile(srcw)
    with harvard as source:
        audio = r.record(source)
    print(type(audio))
    print(r.recognize_google(audio))
    return r.recognize_google(audio)



@bot.message_handler(content_types=["text", "audio", "voice"])
def get_text_messages(message):
    chat_id = message.chat.id
    if message.content_type == 'text':
        if message.text.lower() == "привет":
            bot.send_message(message.from_user.id, "Привет. Скинь мп3 или гс с ане ннглийской речью")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Скинь мп3 или гс с английской речью")
        else:
            bot.send_message(message.from_user.id, "/help")
        return

    if message.content_type == 'voice':
        try:
            file_info = bot.get_file(message.voice.file_id)
            print(file_info)
            downloaded_file = bot.download_file(file_info.file_path)
            print(type(downloaded_file))
            src = f'C:\Проекты\\' + message.voice.file_id + '.ogg'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            data, samplerate = sf.read(src)
            srcw = (f'C:\Проекты\\' + message.voice.file_id + '.wav')
            sf.write(srcw, data, samplerate)
            bot.send_message(message.from_user.id, 'Ожидайте')
            bot.send_message(message.from_user.id, convert_from_mp3(srcw))


        except:
            bot.reply_to(message, "Запиши гс или кинь аудио")

    if message.content_type == 'audio':
        try:
            file_info = bot.get_file(message.audio.file_id)
            print(file_info)
            downloaded_file = bot.download_file(file_info.file_path)
            print(type(downloaded_file))
            src = f'C:\Проекты\\' + message.audio.file_id + '.mp3'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            data, samplerate = sf.read(src)
            srcw = (f'C:\Проекты\\' + message.audio.file_id + '.wav')
            sf.write(srcw, data, samplerate)
            bot.send_message(message.from_user.id, 'Ожидайте')
            bot.send_message(message.from_user.id, convert_from_mp3(srcw))


        except:
            bot.reply_to(message, "Запиши гс или кинь аудио")


def main():
    bot.polling(none_stop=True, interval=0)

main()
