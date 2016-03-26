from hacksport.problem import Challenge
from hacksport.problem import files_from_directory,PreTemplatedFile

class Problem(Challenge):
    files = files_from_directory("grepy-words/")
    dont_template = ["grepy-words"]
    def setup(self):
        self.flag = '1_am_a_h1dd3n_p0tat0'
