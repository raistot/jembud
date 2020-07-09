class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'up'
        self.UnzipMirrorCommand = 'unpack'
        self.TarMirrorCommand = 'tar'
        self.CancelMirror = 'abort'
        self.CancelAllCommand = 'clear'
        self.ListCommand = 'find'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'info'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "gcopy"
        self.WatchCommand = 'vdl'
        self.TarWatchCommand = 'vdltar'

BotCommands = _BotCommands()
