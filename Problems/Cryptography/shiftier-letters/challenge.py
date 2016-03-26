from hacksport.problem import Remote, ProtectedFile

class Problem(Remote):
   program_name = "caesar.py"
   files = [ProtectedFile("words.txt")]

   def initialize(self) :
      self.flag = "shif73d-3n0ugh-ar3-we"
