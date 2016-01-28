# Regex Snippets

## Prefix `r.*`

### [r.bcnpj] Brazilian CNPJ

**allow:** xx.xxx.xxx/xxxx-xx | xxxxxxxxxxxxxx

```javascript
(^(\d{2}.\d{3}.\d{3}/\d{4}-\d{2})|(\d{14})\$)
```

### [r.bcpfcnpj] Brazilian CPF/CNPJ

**allow:** xx.xxx.xxx/xxxx-xx | xxx.xxx.xxx-xx

```javascript
(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2})|(\d{3}\.\d{3}\.\d{3}\-\d{2})
```

### [r.bcpf] CPF

**allow:** xxx.xxx.xxx-xx | xxxxxxxxxxxx

```javascript
(^(\d{3}.\d{3}.\d{3}-\d{2})|(\d{11})\$)
```

### [r.bphone] Brazilian Phone

**allow:** (xx) xxxx-xxxx | (xx) xxxx-xxxxx | xx-xxxx-xxxxx | xx xxxx-xxxx | xx xxxxxxxxx | xxxxxxxx | xxxx-xxxx

```javascript
^(\(\d{2}\)?\s?|\d{2}(\-|\s))?\d{2,4}(\-|\s)?\d{4,5}\$
```

### [r.email] E-mail 

```javascript
^(([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5}){1,25})\$
```
