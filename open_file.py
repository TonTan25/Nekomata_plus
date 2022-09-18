from turtle import delay
import webbrowser as wb
#from pygame import mixer



if __name__ == "__main__":
    url_1 = f"F:/VIDEO/BGM 2 - Enemy.mp3"
    url_2 = f"F:/VIDEO"
    a = str(input("a : "))
    b = str(input("b : "))
    c = str(input("c : "))
    d = str(input("d : "))
    url = f'{a}/{b}/{c}/{d}'
    print("đường dẫn : " + url)
    """
    mixer.music.load(url)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    """
    wb.open(url)


    delay = input("nhan phim bat ky")

