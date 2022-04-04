import os

class Config(object):
      def __init__(self):
          self.BotToken     = os.environ["5264378890:AAFYQiPiHQkaCNMtLxVVmFZ3SttMu6HnngU"]
          self.ChunkSize    = 80
          self.ChunkSizeTel = 1000
          self.ChunkFixed   = 150
          self.FileLimit    = 1024 * 1024 * 500
          self.ExcludeFiles = ['MoodleApp.pyproj','bot.py','Config.py','multiFile.py','MoodleUhoClient.py','S5Crypto.py','S4Crypto.py','nuvidb.txt','requirements.txt','Procfile','__pycache__','.git','.profile.d','.heroku','bot.session','bot.session-journal','output','.cache']
          self.ChunkedFileLimit = 1024 * 1024 * 1024
          self.InProcces = False
          self.BotChannel = '-100654502479'
          self.AdminUsers = ['BigSmoke19']
          self.current_user_msg = ''
          self.current_chanel_msg = ''
          self.procesing = False
          self.watching = False
          self.watch_message = []
          self.moodleUser = os.environ["darian.borges@estudiantes.fbio.uh.cu"]
          self.moodlepassword = os.environ["darian1995"]
          self.users = [BigSmoke19]
          self.userindex = 0
          self.nuvContent = ''
          self.msgurls = 'https://evea.uh.cu/'


      def setS3Token(self,token : str):
          self.S3Token = token

      def setBotToken(self,token : str):
          self.BotToken = token

      def setChunkSize(self,chunk : int):
          self.ChunkSize = chunk

      def setChunkSizeTel(self,chunk : int):
          self.ChunkSizeTel = chunk

      def setAccount(self,user='',passw=''):
          self.moodleUser = user
          self.moodlepassword =  passw

      def toStr(self):
          return '[Chunk Size]\n' + str(self.ChunkSize) + '\n\n[ChunkSizeTel]\n' + str(self.ChunkSizeTel)
      

      #Cosas de los Usuarios
      def stepUser(self):
          self.userindex += 1
          if self.isAvailableNub() == False:
              return False
          self.moodleUser = self.users[self.userindex]['user']
          self.moodlepassword = self.users[self.userindex]['passw']
          return True

      def stepUserZero(self):
          self.userindex = 0
          self.moodleUser = self.users[self.userindex]['user']
          self.moodlepassword = self.users[self.userindex]['passw']

      def isAvailableNub(self):
          if self.userindex >= len(self.users):
              return False
          return True
