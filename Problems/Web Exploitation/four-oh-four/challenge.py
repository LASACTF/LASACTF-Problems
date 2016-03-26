from hacksport.problem import FlaskApp,files_from_directory

class Problem(FlaskApp):
  files = files_from_directory("templates/")
  def setup(self):
    self.flag = 'welc0m3_to_web_dev'
