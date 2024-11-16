from openai import OpenAI
import sys
import os
import configparser

# Define the config file path
CONFIG_FILE = 'config.ini'

# Function to load API key from config file
def load_api_key():
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        print("Error: Config file not found. Please set the API key using: python transcribe_audio.py set_api_key <your_api_key>")
        sys.exit(1)

    config.read(CONFIG_FILE)
    if 'openai' not in config or 'api_key' not in config['openai']:
        print("Error: API key not found in config file.")
        sys.exit(1)

    return config['openai']['api_key']

# Function to set API key and save to config file
def set_api_key(api_key):
    config = configparser.ConfigParser()
    config['openai'] = {'api_key': api_key}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    print(f"API key has been saved to {CONFIG_FILE}.")

# Main function
def main():
    # Check if the first argument is to set the API key
    if len(sys.argv) >= 2 and sys.argv[1] == "set_api_key":
        if len(sys.argv) != 3:
            print("Usage: python transcribe_audio.py set_api_key <your_openai_api_key>")
            sys.exit(1)
        set_api_key(sys.argv[2])
        sys.exit(0)

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python transcribe_audio.py <path_to_audio_file> [<output_file_path>]")
        sys.exit(1)

    # Load the API key from the config file
    api_key = load_api_key()
    client = OpenAI(api_key=api_key)

    audio_file_path = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(audio_file_path):
        print(f"Error: The file '{audio_file_path}' does not exist.")
        sys.exit(1)

    # Default output file path: same as input but with .txt extension
    if len(sys.argv) == 3:
        output_file_path = sys.argv[2]
    else:
        output_file_path = os.path.splitext(audio_file_path)[0] + ".txt"

    # Open audio file for transcription
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
            # Save the transcription to a text file
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(transcription.text)
                print(f"Transcription saved to '{output_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

