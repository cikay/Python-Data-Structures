
import time
import random

class Music:

    def __init__(self, music_name, isrepeated=False):
        self.music_name = music_name
        self.isrepeated = isrepeated
        self.next = None
        self.prev = None


        if self.isrepeated:
            self.next = self


class MusicPlayer:

    def __init__(self, music_name=None):
        
        self.__isrepeated = False
        self.root = None
        self.play_inorder = True

    @property
    def isrepeated(self):
        return self.__isrepeated
    
    @isrepeated.setter
    def isrepeated(self, value):
        self.__isrepeated = value


    def add_music(self, music_name):

        if self.root is None:
            self.root = Music(music_name)
            self.root.next = self.root
            return 
        
        iter = self.root

        while iter.next != self.root:
            iter = iter.next
        
        music = Music(music_name)
        iter.next = music
        music.next = self.root

    def __play_mixed(self):

        while True:

            squence = random.randint(0, 5)

            iter = self.root 

            for i in range(squence):
                iter = iter.next
            
            print(f"{iter.music_name} is playing")
            time.sleep(2)


    def play(self):

        if self.play_inorder:
            self.__play_inorder()
        
        else:
            self.__play_mixed()


    def __play_inorder(self):

        iter = self.root

        if not self.__isrepeated:
            print(f"{self.root.music_name} is playing")
            time.sleep(2)
            iter = iter.next
            while iter is not self.root:
                print(f"{iter.music_name} is playing")
                time.sleep(2)
                iter = iter.next
            
            print("player list finished")
        else:
            print("Music player repeating")
            print(f"{self.root.music_name} is playing")
            time.sleep(2)
            iter = iter.next
            while True:
                
                print(f"{iter.music_name} is playing")
                time.sleep(2)
                iter = iter.next


mp = MusicPlayer()
mp.add_music("Xacirek")
mp.add_music("Bihare")
mp.add_music("Kocer")
mp.add_music("Lo dilo")
mp.add_music("Aylo dilo")
mp.add_music("Biranin")

mp.play_inorder = False
mp.play()

# mp.isrepeated = True
# mp.play()


