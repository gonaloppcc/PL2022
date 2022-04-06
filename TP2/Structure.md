# Etapas

- Ler ficheiro → E guardar num dicionário

- Verificar LL(1) → e Validar

- Adaptar ao PLY

## Regras da linguagem

### Tokens

- Especificamos os tokens com a keyword `Tokens:` no início da linha.

- Armazenados num dicionário em que a chave vai ser o nome do símbolo terminal e o value vai ser a expressão regex
  correspondente.

### Símbolos não terminais

- No início da linha deve aparecer um símbolo não terminal seguido de `:` e nas linhas seguintes as regras de produção
  deste símbolo

### Exemplo das regras aplicadas

```
Tokens:
'$'
'+'
'('
')'
num \d+
id [a-zA-Z_]\w*

Z:
Exp '$'

Exp:
Exp '+' Termo
Termo

Termo:
'(' Exp ')'
id
```

# Estrutura do dicionário

- key : Estado, Value: Lista de regras que derivam de um estado

## Exemplo

- key : S, Value: `[abc, A]`