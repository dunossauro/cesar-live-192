# Cifra de cesar

A ideia desse projeto é representar uma biblioteca capaz de executar a cifra de cesar (ROT13)

## Exemplos de uso

### Encriptação

```python
from cesar import encripta

encripta('Eduardo')  # rqhneqb
```

### Decriptação
```python
from cesar import decripta

decripta('rqhneqb')  # eduardo
```

### Rotações diferentes de 13
```python
from cesar import decripta, encripta

encripta('Eduardo')  # sriofrc
decripta('sriofrc', 14)  # eduardo
```
