import glob

class DiscoverDataFiles:
    """Class to discover fully qualified path to given glob pattern

    Given a folder and a glob pattern find all the files that match that pattern in
    the folder and create a collection from them.
    """
    def __init__(self, folder, glob_pattern):
        self.targetFolder = folder
        self.glob_pattern = glob_pattern

    def read(self):
        fqp = self.targetFolder + "/" + self.glob_pattern
        files = glob.glob(fqp, recursive=True)
        return files
