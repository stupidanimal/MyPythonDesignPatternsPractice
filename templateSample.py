from abc import ABCMeta,abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass
    @abstractmethod
    def compileToObject(self):
        pass
    @abstractmethod
    def run(self):
        pass
    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):
    def collectSource(self):
        print('Collecting Swift Source Code')
    def compileToObject(self):
        print('Compiling Swift code to LLVM bitcode')
    def run(self):
        print('Program running on runtime environment')

iOS = iOSCompiler()

iOS.compileAndRun()

#模板执行者制作具体步骤，模板设定着制定过程，或者组合过程
    