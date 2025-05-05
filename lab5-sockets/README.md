# Laboratorijska vježba 5 – Socket programiranje

Ova vježba prikazuje primjere komunikacije putem mreže korištenjem Pythonovog `socket` modula. Implementirani su:

- Echo server i echo klijent (jedan-na-jedan komunikacija)
- Chat server i chat klijent (višekorisnička komunikacija)

## Kako pokrenuti servere i klijente

### 1. Echo Server i Echo Klijent

**Pokretanje Echo servera:**

```bash
python3 echo_server.py
```

Server će se pokrenuti na `localhost:65432` i čekati dolazne veze.

**Pokretanje Echo klijenta:**

U drugom terminalu:

```bash
python3 echo_client.py
```

Klijent se povezuje na server, šalje tekstualnu poruku i prima istu poruku natrag (echo mehanizam).

### 2. Chat Server i Chat Klijent

**Pokretanje Chat servera:**

```bash
python3 chat_server.py
```

Chat server se pokreće na `localhost:65433` i podržava više klijenata istovremeno.

**Pokretanje Chat klijenta:**

U drugom (ili više) terminala:

```bash
python3 chat_client.py
```

Klijent unosi korisničko ime, a zatim može slati poruke koje svi povezani korisnici vide.

## Primjeri izlaza iz programa

### Echo server

```
[SERVER] Listening on localhost:65432
[NEW] Connection from ('127.0.0.1', 54321)
[RECV from ('127.0.0.1', 54321)] Bok!
```

### Echo klijent

```
Unesite poruku: Bok!
Odgovor servera: Bok!
```

### Chat server

```
[CHAT SERVER] Listening on localhost:65433
[NEW] Connection from ('127.0.0.1', 54322)
[LOGIN] Ivan from ('127.0.0.1', 54322)
Ivan: Pozdrav svima!
```

### Chat klijent

```
Unesite korisničko ime: Ivan
Chat započet. Koristite Ctrl+C za izlaz.
> Pozdrav svima!
```

## Sadržaj projekta

- `echo_server.py` – jednostavan TCP echo server
- `echo_client.py` – klijent koji šalje poruku i prima je natrag
- `chat_server.py` – višenitni server za višekorisnički chat
- `chat_client.py` – klijent koji se pridružuje chatu i komunicira s ostalima

