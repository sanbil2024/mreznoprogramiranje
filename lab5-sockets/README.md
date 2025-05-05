# Laboratorijska vježba 5 – Socket programiranje

Ova vježba prikazuje osnovne primjere komunikacije putem mreže korištenjem Pythonovog `socket` modula. Implementirani su jednostavni serveri i klijenti koji međusobno komuniciraju putem TCP protokola.

## Kako pokrenuti servere i klijente

### 1. Pokretanje servera

U terminalu, navigirajte do direktorija `lab5-sockets` i pokrenite server:

```bash
python3 server.py
```

Server će se pokrenuti i čekati dolazne veze na definiranom portu (npr. 5000).

### 2. Pokretanje klijenta

U drugom terminalu, također navigirajte do direktorija `lab5-sockets` i pokrenite klijenta:

```bash
python3 client.py
```

Klijent će se pokušati povezati na server i omogućiti unos poruka koje će se slati serveru.

> **Napomena:** Prije pokretanja klijenta, osigurajte da je server već pokrenut kako bi veza mogla biti uspostavljena.

## Primjeri izlaza iz programa

### Server

Nakon pokretanja servera i uspostavljanja veze s klijentom, izlaz može izgledati ovako:

```
Server pokrenut. Čeka veze...
Povezan s: ('127.0.0.1', 54321)
Primljeno od klijenta: Pozdrav, servere!
Poslano klijentu: Poruka primljena.
```

### Klijent

Nakon pokretanja klijenta i slanja poruke serveru, izlaz može izgledati ovako:

```
Povezan sa serverom na 127.0.0.1:5000
Unesite poruku: Pozdrav, servere!
Odgovor servera: Poruka primljena.
```

## Sadržaj projekta

- **server.py** – TCP server koji prima poruke i odgovara na njih.
- **client.py** – Klijent koji šalje poruke serveru i prima odgovor.

## Napomena

Kod pokretanja skripti uvjerite se da imate instaliran Python 3 i da se nalazite u odgovarajućem direktoriju.

