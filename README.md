# syncere
This python script helps you sync a folder on your PC with a folder on your android device.
Recognises the files that are "on your PC but not on android device" and the files that are "on the device but not on PC" and eventually transfer these files to the folder via adb.

<hr>

## Pre-requisites
- working adb instance with address present in PATH Environment Variable.

### Syntax
python syncere.py /path/to/android/folder /path/of/local/pc/folder [-l]

## Usage
- Download the python script..
- Connect your device via USB.
- Run the python script on terminal/cmd/powershell
- Syncing Begins.

=> Opitonally, -l switch can be used to list the files and total size before you actually begin the transfer process.
