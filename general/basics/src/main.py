from modules.point import Point
from modules.secretstring import SecretString
from modules.polymorphism import AudioFile,  MP3File,  WavFile,  OggFile

def main(args=None):
    print("--- POINT TEST ---")
    point1 = Point()
    point2 = Point()
    point1.reset()
    point2.move(5,  0)
    print(point2.calculate_distance(point1))
    assert(point2.calculate_distance(point1) == point1.calculate_distance(point2))
    point1.move(3,  4)
    print(point1.calculate_distance(point2))
    print(point1.calculate_distance(point1))
    
    point3 = Point(3,  5)
    print(point3.x,  point3.y)
    print("--- END POINT TEST ---")
    print("--- SECRET STRING TEST ---")
    secret_string = SecretString("ACME: Top Secret.",  "antwerp")
    print(secret_string.decrypt("antwerp"))
    print(secret_string._SecretString__plain_string)
    print("--- END SECRET STRING TEST ---")
    print("--- POLYMORPHISM TEST ---")
    mp3_file = MP3File("file1.mp3")
    wav_file = WavFile("file2.wav")
    ogg_file = OggFile("file3.ogg")
    mp3_file.play()
    wav_file.play()
    ogg_file.play()
    print("--- END POLYMORPHISM TEST ---")

if __name__ == "__main__":
    main() 
