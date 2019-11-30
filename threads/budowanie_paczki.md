## Budowanie wykonywalnej paczki z programem

- zainstalować pyinstaller (https://anaconda.org/acellera/pyinstaller)
- zaznaczyć folder 'threads' jako 'sources root' w pycharm (by nie pokazywał błędów)
- przejść do konsoli i do folderu 'threads'
- uruchomić budowanie: `pyinstaller bank_controller.py -n bank --onefile`
- utworzony zostanie folder `dist`, a w nim plik wykonywalny `bank` (na windows: `bank.exe`)
- plik można normalnie uruchamiać