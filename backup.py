from os import system, chdir
from datetime import datetime
from zoneinfo import ZoneInfo


def main():
  PATH = '/var/lib/docker/volumes/minecraft-server_minecraft_world/_data'
  now = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%d-%m-%Y %H:%M")

  chdir(PATH)
  system('git add .')
  system(f'git commit -m "bk-{now}"')
  system('git push')


if __name__ == '__main__':
  main()
