import time

def lyrics(lyrics_array):
    for sentence, speed, delay in lyrics_array:
        for letter in sentence:
            print(letter, end='', flush=True)
            time.sleep(speed)
        print()
        time.sleep(delay)
