class Release:
    STABLE = 0
    DEV    = 1

    Names = [
        'Stable',
        'Dev'
    ]

class Version:
    def __init__(self, major: int, minor: int, patch: int, release: int):
        self.major: int = major
        self.minor: int = minor
        self.patch: int = patch
        self.release : str = release


    def version(self):
        return f'v{self.major}.{self.minor}.{self.patch}'

    def __str__(self):
        return f'v{self.major}.{self.minor}.{self.patch} {Release.Names[self.release]}'

    DEFAULT = None

Version.DEFAULT = Version(1, 0, 0, Release.STABLE)