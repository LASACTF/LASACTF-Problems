from hacksport.problem import PHPApp, files_from_directory

class Problem(PHPApp):
    files = files_from_directory("webroot/")
    php_root = "webroot/"

    def setup(self):
        self.flag = "matricies_linear"
