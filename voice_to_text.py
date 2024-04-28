import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

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

    # Création d'un objet de reconnaissance vocale
    reconnaisseur = sr.Recognizer()

    # Ouverture du fichier audio
    with sr.AudioFile(nom_fichier) as source:
        audio = reconnaisseur.record(source)

    # Reconnaissance vocale
    try:
        texte = reconnaisseur.recognize_google(audio, language="fr-FR")
        
        if "Move" in texte:
            texte = texte.replace("Move", "mauve")

        if "12 h" in texte:
            texte = texte.replace("12 h", "12h")
        
        print(f"\t\033[3;33m#tts : Texte reconnu : '{texte}'\033[0m")
        return texte
    except sr.UnknownValueError:
        print("\t\033[3;33m#tts : Google Speech Recognition n'a pas pu comprendre l'audio\033[0m")
    except sr.RequestError as e:
        print(f"\t\033[3;33m#tts : Erreur lors de la requête à Google Speech Recognition : {e}\033[0m")
    return None



if __name__ == "__main__":
    filename = "enregistrement.wav"
    enregistrer_audio(filename, duree_enregistrement=5)
    speech_recognition(filename)
# Exemple d'utilisation

