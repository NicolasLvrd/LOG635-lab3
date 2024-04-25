import sounddevice as sd
import soundfile as sf
import whisper

def enregistrer_audio(nom_fichier, duree_enregistrement, frequence_echantillonnage=44100):
    # Enregistrement de l'audio
    print("\t\033[3;33m#tts : Enregistrement audio en cours...\033[0m")
    enregistrement = sd.rec(int(duree_enregistrement * frequence_echantillonnage), samplerate=frequence_echantillonnage, channels=2)
    sd.wait()
    print("\t\033[3;33m#tts : Enregistrement audio terminé.\033[0m")

    # Écriture des données audio dans un fichier WAV
    sf.write(nom_fichier, enregistrement, frequence_echantillonnage)
    #print(f"Fichier audio enregistré sous '{nom_fichier}'.")

def speech_recognition(nom_fichier):
    try: 
        print("\t\033[3;33m#tts : Reconnaissance vocale en cours...\033[0m")
        model = whisper.load_model("base")
        result = model.transcribe(nom_fichier, language="french")
        # print("\t\033[3;33m#tty : Retranscription : ", result["text"])
        return result["text"]
    
    except Exception as e:
        print(f"Erreur lors de la reconnaissance vocale : {e}")

if __name__ == "__main__":
    filename = "enregistrement.wav"
    enregistrer_audio(filename, duree_enregistrement=5)
    speech_recognition(filename)
# Exemple d'utilisation

