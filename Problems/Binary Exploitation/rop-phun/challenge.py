from hacksport.problem import Challenge, ProtectedFile, ExecutableFile,Remote

class Problem(Remote):
    program_name = "rop_fun"
    files = [ProtectedFile("flag.txt")]
    def initialize(self) :
        self.flag = "s0_much_r0p_4hhhhhh"
