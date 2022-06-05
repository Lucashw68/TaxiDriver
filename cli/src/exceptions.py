class Error(Exception):
    """Base class for other exceptions"""
    pass

################################################################################
# GENERAL
################################################################################

class InvalidParams(Error):
    """Raised when parameters are invalid"""
    pass

################################################################################
# INPUTS
################################################################################

class InvalidGraph(Error):
    """Raised when the graph build on the timetables is invalid or empty"""
    pass

class InvalidTrip(Error):
    """Raised when the departure or destination doesn't exists in graph"""
    pass

################################################################################
# NLP
################################################################################

class InvalidLanguage(Error):
    """Raised when the input language is not French"""
    pass

class InvalidCommand(Error):
    """Raised when the input command is not a valid command"""
    pass

################################################################################
# UTILS
################################################################################

class OpenFile(Error):
    """Raised when opening a file failed"""
    pass
