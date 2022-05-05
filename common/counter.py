from os import chdir, listdir, path, system
from random import choices
from string import ascii_letters, digits

if 'tex_experiments' in listdir():
    chdir('tex_experiments')
system('rm -rf _minted* *.aux *.fls *.log *.out *.fdb_latexmk *.synctex.gz *.xdv')
filenames = lambda d: map(lambda it: path.splitext(it)[0], listdir(d))

used = set(filenames('.')) | set(listdir('./common')) | set(listdir('./data'))
print(used)
alphabet = ascii_letters + digits + '-_'
while True:
    number = ''.join(choices(alphabet, k=4))
    if number not in used:
        print(number, '.tex', sep='')
        break