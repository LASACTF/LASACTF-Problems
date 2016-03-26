from hacksport.problem import PHPApp, ProtectedFile, files_from_directory

class Problem(PHPApp):
  files = files_from_directory("webroot/")
  php_root = "webroot/"

  def setup(self):
    self.flag = 'a_long_tw1sted_maz3'
