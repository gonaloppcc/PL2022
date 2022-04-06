# Etapas

- Ler ficheiro → E guardar num dicionário

- Verificar LL(1) → e Validar

- Adaptar ao PLY

# Estrutura do ficheiro

```
S:
a B c
c
B:
b B
c
c:
C c
c
```

# Estrutura do dicionário

- key : Estado, Value: Lista de regras que derivam de um estado

## Exemplo

- key : S, Value: `[abc, A]`