from os import listdir

def getForgeApplicationFilename():
  filesAtDirectory = list(filter(lambda filename: 'forge-' in filename , listdir()))
  filename = filesAtDirectory[0] if len(filesAtDirectory) > 0 else ''
  return filename
