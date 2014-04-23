class BaseCommand(object):
    def __init__(self, args):
        super(BaseCommand, self).__init__()
        self.args = args

    def execute(self):
        raise Exception('You must override execute() in your Command.')
