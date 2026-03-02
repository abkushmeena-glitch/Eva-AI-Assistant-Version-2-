from AppOpener import close, open as appopen, features
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import keyboard
import requests
import asyncio
import os

env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_vk FzWSB YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table", "dDoNo ikb4Bb gsrt", "sXLaOe",
            "LWkfKe", "VQf4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64, x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/100.0.4896.75 Safari/537.36'

client = Groq(api_key=GroqAPIKey)

professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.", 
    "I'm at your service for any additional questions or support you may need-don't hesitate to ask.",
]

messages = []

SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."}]

def GoogleSearch(Topic):
    search(Topic)
    return True

def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})

        completion = client.chat.completions.create(
            model= "llama-3.3-70b-versatile",
            messages= SystemChatBot + messages,
            max_tokens= 2048,
            temperature=0.7,
            top_p= 1,
            stream= True,
            stop= None,
        )

        Answer = ""

        for chunk in completion: 
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        
        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer
    
    Topic: str = Topic.replace("Content ", "")
    ContentBYAI = ContentWriterAI(Topic)

    content_dir = os.path.join("Data", "Content")
    os.makedirs(content_dir, exist_ok=True)  
    
    filename = f"{Topic.lower().replace(' ', '')}.txt"
    file_path = os.path.join(content_dir, filename)

    with open(rf"Data\{Topic.lower().replace(' ','')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentBYAI)
        file.close()

    OpenNotepad(rf"Data\{Topic.lower().replace(' ','')}.txt")
    return True

# Content("write a code to find a leap year in python")

def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

# PlayYoutube("ui amma")

def OpenApp(app, sess=requests.session()):
    try:
        
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True  
    except Exception as e:
        print(f"Error opening app locally: {e}")

    
    try:
        query = f"{app}" 
        url = f"https://www.{query}.com"  
 
        webbrowser.open(url)
        return True
    except Exception as e:
        print(f"Error opening the webpage: {e}")
        return False
    
# OpenApp("telegram")

def CloseApp(app):
    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False

# CloseApp("whatsapp")

def System(command):
   
    def mute():
        keyboard.press_and_release("volume mute")

    def unmute():
        keyboard.press_and_release("volume mute")

    def volume_up():
        keyboard.press_and_release("volume up")

    def volume_down():
        keyboard.press_and_release("volume down")

    def play_pause():
        keyboard.press_and_release("play/pause")

    def next_track():
        keyboard.press_and_release("next track")

    def previous_track():
        keyboard.press_and_release("previous track")
 
    def take_screenshot():
        keyboard.press_and_release("print screen")

    def brightness_up():
        keyboard.press_and_release("brightness up")

    def brightness_down():
        keyboard.press_and_release("brightness down")

    # def shutdown():
    #     system = platform.system()
    #     if system == "Windows":
    #         os.system("shutdown /s /t 1")
    #     elif system == "Linux":
    #         os.system("systemctl poweroff")
    #     elif system == "Darwin":
    #         os.system("osascript -e 'tell app \"System Events\" to shut down'")

    # def restart():
    #     system = platform.system()
    #     if system == "Windows":
    #         os.system("shutdown /r /t 1")
    #     elif system == "Linux":
    #         os.system("systemctl reboot")
    #     elif system == "Darwin":
    #         os.system("osascript -e 'tell app \"System Events\" to restart'")

    # def lock_system():
    #     system = platform.system()
    #     if system == "Windows":
    #         ctypes.windll.user32.LockWorkStation()
    #     elif system == "Linux":
    #         os.system("gnome-screensaver-command -l")
    #     elif system == "Darwin":
    #         os.system("/System/Library/CoreServices/Menu/Extras/User.menu/Contents/Resources/CGSession -suspend")

    command_handlers = {
        "mute": mute,
        "unmute": unmute,
        "volume up": volume_up,
        "volume down": volume_down,
        "play/pause": play_pause,
        "next track": next_track,
        "previous track": previous_track,
        "screenshot": take_screenshot,
        "brightness up": brightness_up,
        "brightness down": brightness_down,
        # "shutdown": shutdown,
        # "restart": restart,
        # "lock the system": lock_system,
    }

    handler = command_handlers.get(command)

    if handler:
        try:
            handler()
            return True
        except Exception as e:
            print(f"Error executing command '{command}': {e}")
            return False
    else:
        return False 
# System("screenshot")

async def TranslateAndExecute(commands: list[str]):
    funcs = []

    for command in commands:
        if command.startswith("open "):
            if "open it" in command:
                pass
            if "open file" == command:
                pass
            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
                funcs.append(fun)
        
        elif command.startswith("general "):
            pass
        elif command.startswith("realtime "):
            pass
        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
        elif command.startswith("play "):
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
            funcs.append(fun)
        elif command.startswith("content "):
            fun = asyncio.to_thread(Content, command.removeprefix("content "))
            funcs.append(fun)
        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))
            funcs.append(fun)
        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search"))
            funcs.append(fun)
        elif command.startswith("system "):
            fun = asyncio.to_thread(System, command.removeprefix("system "))
            funcs.append(fun)

        else:
            print(f"No Funtion Found. For{command}")
    
    results = await asyncio.gather(*funcs)

    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result

async def Automation(commands: list[str]):

    async for result in TranslateAndExecute(commands):  
        pass

    return True

# if __name__ == "__main__":
#     asyncio.run(Automation([ "write a code to build a simple calculator in python" ]))