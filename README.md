# Zero Console

Console permettant de réaliser des publications de messages sur des addresses 0-MQ. Cet outil
est destiné à simuler des comportements en bouchon dans une architecture de messaging basée
sur 0-MQ.

## Usage interactif

```
$ ./zero-console.py
| zero-console > publish --to ipc:///tmp/zero-console-pub
Now publishing to: ipc:///tmp/zero-console-pub
| zero-console > pub "OMFG it's working"
Sent: ipc:///tmp/zero-console-pub ==> "OMFG it's working"
| zero-console >
```

Dans cet exemple, tout client 0-MQ abonné sur ```ipc:///tmp/zero-console-pub``` recevra le message
envoyé.

# Usage scripté

Vous pouvez aussi écrire des scripts correspondants dans un fichier et l'injecter dans la
console :

```
$ ./zero-console.py < zero-console-script.zcs
| zero-console > Now publishing to: ipc:///tmp/zero-console-pub
| zero-console > Sent: ipc:///tmp/zero-console-pub ==> "OMFG it's working"
```

Bon bouchonnage à tous.