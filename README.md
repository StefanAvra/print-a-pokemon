# print_a_pokemon.py
This script prints a Pokemon once a day on thermal paper.
Data is retrieved via pokeapi.co.

Example of a print:

![bulbasaur scan](https://github.com/StefanAvra/print-a-pokemon/blob/main/bulbasaur.jpeg?raw=true)

## Printer
I'm using a cheap thermal printer and the [ZJ-58 Driver](https://github.com/klirichek/zj-58) on Raspberry Pi. Text is printed via serial connection and images are sent to CUPS, so CUPS has to be configured.

## Usage
```print_a_pokemon.py``` depends on [ImageMagick](https://imagemagick.org/script/download.php). Install that first and check if it can be executed via ```convert``` in terminal.

Clone this repo and cd into ./print-a-pokemon.

Create and activate virtual env
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

To create a cron job that runs ```print_pokemon.sh``` everyday at 20:00 you can run
```sh
crontab -e
```
and add
```sh
0 20 * * * /path/to/directory/print-a-pokemon/print_pokemon.sh
```
