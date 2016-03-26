from hacksport.problem import PHPApp, ProtectedFile, files_from_directory
import sqlite3

class Problem(PHPApp):
    files = files_from_directory("webroot/") + [ProtectedFile("users.db")]
    php_root = "webroot/"

    def setup(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('CREATE TABLE users (name text, password_hash text, admin integer);')

        c.execute('''INSERT INTO users VALUES ('admin', 'a8j-2&}r', 1)''')

        conn.commit()
        conn.close()
        self.flag = "someone_has_to_control_the_internal_state_why_not_the_user"
