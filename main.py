import time
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit as pk
import pyautogui as pg
import os
import requests
import pyjokes as pj
from translate import Translator as tr
import winsound as ws

#=============================================================
audio = sr.Recognizer()
maquina = pyttsx3.init()
pg.PAUSE=1


def executa_comando():
    try:
        with sr.Microphone() as source:
            audio.pause_threshold = 1
            audio.adjust_for_ambient_noise(source)

            audio.pause_threshold = 1
            audio.dynamic_energy_adjustment_ratio = 5
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            maquina.runAndWait()
            if 'miranda' in comando:
                ws.Beep(frequency=2000, duration=100, )  #beep inicial
                voz1 = audio.listen(source)
                comando = audio.recognize_google(voz1, language='pt-BR')
                comando = comando.lower()
                ws.Beep(frequency=1000, duration=100, ) #beep final
                print ('passou por aq')
                pass

            else:

                executa_comando()


    except:
        return executa_comando()
    return comando


def comando_voz_usuario():
    comando = executa_comando()
    time.sleep(0.5)

    time.sleep(0.5)
    try:

    # =================PESQUISA GOOGLE=========================
        comando = comando.replace('miranda', '')
        if 'pesquise' in comando:
            pesq = comando.casefold()
            pesq1 = pesq.replace('pesquise ', '')
            pesq2 = pesq1.replace(' ', '%20')
            os.system(f'start www.google.com/search?q={pesq2}')
            maquina.say('eu encontrei isto na internet')
            maquina.runAndWait()
        if 'pesquisar' in comando:
            pesq = comando.casefold()
            pesq1 = pesq.replace('pesquisar ', '')
            pesq2 = pesq1.replace(' ', '%20')
            os.system(f'start www.google.com/search?q={pesq2}')
            maquina.say('eu encontrei isto na internet')
            maquina.runAndWait()


        # ===================== PERGUNTANDO HORAS =================
        elif 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say('agora sao ' + hora)
            maquina.runAndWait()

    # ============= PESQUISANDO DIA em numero =================
        elif 'dia' in comando:
            hoje = datetime.datetime.now().strftime('%d')
            hoje1 = datetime.datetime.now().strftime('%m')
            if '01' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de janeiro')
                maquina.runAndWait()
            elif '02' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de fevereiro')
                maquina.runAndWait()
            elif '03' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de março')
                maquina.runAndWait()
            elif '04' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de abril')
                maquina.runAndWait()
            elif '05' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de maio')
                maquina.runAndWait()
            elif '06' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de junho')
                maquina.runAndWait()
            elif '07' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de julho')
                maquina.runAndWait()
            elif '08' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de agosto')
                maquina.runAndWait()
            elif '09' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de setembro')
                maquina.runAndWait()
            elif '10' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de outubro')
                maquina.runAndWait()
            elif '11' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de novembro')
                maquina.runAndWait()
            elif '12' in hoje1:
                maquina.say('Hoje é dia' + hoje + 'de dezembro')
                maquina.runAndWait()

        # ==========MUSICAS===========================

        elif 'pausar' in comando:
            pg.press('playpause')

        elif 'play' in comando:
            pg.press('playpause')

        elif 'próxima' in comando:
            pg.press('nexttrack')

        elif 'anterior' in comando:
            pg.press('prevtrack', presses=2)

        elif 'novamente' in comando:
            pg.press('prevtrack')

        elif 'tocar' in comando:
            musica = comando.replace('tocar', '')
            resultado = pk.playonyt(musica)
            maquina.say('Tocando sua música')
            maquina.runAndWait()

        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            resultado = pk.playonyt(musica)
            maquina.say('Tocando sua música')
            maquina.runAndWait()

        elif 'toca' in comando:
            musica = comando.replace('toca', '')
            resultado = pk.playonyt(musica)
            maquina.say('Tocando sua música')
            maquina.runAndWait()

    #===ABRIR PROGRAMAS======

        elif 'notas' in comando:
            maquina.say('abrindo bloco de notas')
            maquina.runAndWait()
            os.system('notepad')
        elif 'calculadora' in comando:
            maquina.say('abrindo calculadora')
            maquina.runAndWait()
            os.system('calc')
        elif 'google' in comando:
            maquina.say('abrindo o google')
            maquina.runAndWait()
            os.system('start https://google.com')
        elif 'youtube' in comando:
            maquina.say('abrindo o youtube')
            maquina.runAndWait()
            os.system('start https://youtube.com')
        elif 'tarefas' in comando:
            maquina.say('abrindo gerenciador de tarefas')
            maquina.runAndWait()
            os.system('start taskmgr')
        elif 'word' in comando:
            maquina.say('abrindo word')
            maquina.runAndWait()
            os.system('start winword')
        elif 'excel' in comando:
            maquina.say('abrindo excel')
            maquina.runAndWait()
            os.system('start excel')
        elif 'configurações' in comando:
            maquina.say('abrindo configurações')
            maquina.runAndWait()
            pg.hotkey('win','i')
        elif 'lupa' in comando:
            maquina.say('abrindo lupa')
            maquina.runAndWait()
            pg.hotkey('win','=')
        elif 'zoom' in comando:
            maquina.say('dando zoom')
            maquina.runAndWait()
            pg.hotkey('win','=')
        elif 'print' in comando:
            maquina.say('abrindo captura de tela')
            maquina.runAndWait()
            pg.hotkey('win','shift','s')



        #===============AÇÕES=================
        elif 'minimizar' in comando:
            maquina.say('minimizando')
            maquina.runAndWait()
            pg.hotkey('win','m')
        elif 'fechar' in comando:
            maquina.say('fechando janela')
            maquina.runAndWait()
            pg.hotkey('alt','f4')
        elif 'feche' in comando:
            maquina.say('fechando janela')
            maquina.runAndWait()
            pg.hotkey('alt','f4')



        # ======== PESQUISAR WIKIPEDIA===============
        elif 'wiki' in comando:
            pesquisar = comando.replace('wiki', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(pesquisar, 2)
            maquina.say(resultado)
            maquina.runAndWait()

        # =========PIADAS======================
        elif 'piada' in comando:
            piada = pj.get_joke(language='en', category='neutral')
            piada = piada.casefold()
            translator = tr(to_lang="pt")
            joke = translator.translate(piada)
            maquina.say(joke)
            maquina.runAndWait()


        # ====================CLIMA-OPENWETHERMAP================================
        elif 'clima' in comando:
            maquina.say('Pesquisando tempo')
            maquina.runAndWait()
            api_key = 'SUA_API_KEY' #coloque sua apiKey do OpenWetherMap
            city = 'SUA_CIDADE' #coloque sua Cidade
            lang = 'pt_br'
            link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric'
            req = requests.get(link)
            reqd = req.json()
            desc = reqd['weather'][0]['description']
            temp = reqd['main']['temp']
            temp = int(temp)
            maquina.say(f'{temp}°, e o tempo está, {desc}')
            maquina.runAndWait()
        elif 'temperatura' in comando:
            maquina.say('Pesquisando tempo')
            maquina.runAndWait()
            api_key = 'SUA_API_KEY' #coloque sua apiKey do OpenWetherMap
            city = 'SUA_CIDADE' #coloque sua Cidade
            lang = 'pt_br'
            link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric'
            req = requests.get(link)
            reqd = req.json()
            desc = reqd['weather'][0]['description']
            temp = reqd['main']['temp']
            temp = int(temp)
            maquina.say(f'{temp}°, e o tempo está, {desc}')
            maquina.runAndWait()

        # ================CRIADOR/CEO===========================================
        elif 'criou' in comando:
            maquina.say('O meu mestre Typcal Solution, ou vinícius, quem me criou. e meu nome é uma lua de urano')
            maquina.runAndWait()
        elif 'conselho' in comando:
            url = 'https://api.adviceslip.com/advice'
            data = requests.get(url)
            json_data = data.json()
            advice = json_data['slip']
            ad = advice['advice']
            translator = tr(to_lang="pt")
            myb = translator.translate(ad)
            maquina.say(myb)
            maquina.runAndWait()
      
        # ==================EXIT====================================
        elif 'obrigado' in comando:
            maquina.say('denada, Estou me retirando')
            maquina.runAndWait()
            exit()
        elif 'retirar' in comando:
            maquina.say('Estou me retirando')
            maquina.runAndWait()
            exit()
        elif 'retire' in comando:
            maquina.say('Estou me retirando')
            maquina.runAndWait()
            exit()
        # ======================DESLIGANDO O PC======================================
        elif 'desligar' in comando:
            maquina.say('Desligando, até logo.')
            maquina.runAndWait()
            os.system('shutdown /s /t 2')
        elif 'desligue' in comando:
            maquina.say('Desligando, até logo.')
            maquina.runAndWait()
            os.system('shutdown /s /t 2')
        elif 'reiniciar' in comando:
            maquina.say('Reiniciando, até daqui à pouco.')
            maquina.runAndWait()
            os.system('shutdown /r /t 2')
        elif 'reinicie' in comando:
            maquina.say('Reiniciando, até daqui à pouco.')
            maquina.runAndWait()
            os.system('shutdown /r /t 2')

        # ============CHAMANDO MIRANDA/SEMPRE DEIXAR POR ULTIMO NO CODIGO ESTA PARTE==================================
        elif 'esta aí' in comando:
            maquina.say('olá, estou aqui')
            maquina.runAndWait()

        return comando_voz_usuario()
    except:
        ws.Beep(frequency=1000, duration=100, ) #beep final
        pass
comando_voz_usuario()
