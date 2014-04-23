from basecommand import BaseCommand

class Init(BaseCommand):
    def execute(self):
        print 'Init! Args:', ', '.join(self.args)
