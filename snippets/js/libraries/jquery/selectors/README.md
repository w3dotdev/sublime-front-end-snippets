## Selectors

### [jqall] all

```javascript
${1:\$}("*");
```

### [jq:a] :animated

```javascript
${1:\$}("${2}:animated");
```

### [jq[]|] Attribute Contains Prefix

```javascript
${1:\$}("${2}[${3:attribute}|='${4:value}']");
```

### [jq[]*] Attribute Contains

```javascript
${1:\$}("${2}[${3:attribute}*='${4:value}']");
```

### [jq[]~] Attribute Contains Word

```javascript
${1:\$}("${2}[${3:attribute}~='${4:value}']");
```

### [jq[]$] Attribute Ends With

```javascript
${1:\$}("${2}[${3:attribute}$='${4:value}']");
```

### [jq[]=] Attribute Equals

```javascript
${1:\$}("${2}[${3:attribute}='${4:value}']");
```

### [jq[]!] Attribute Not Equal

```javascript
${1:\$}("${2}[${3:attribute}!='${4:value}']");
```

### [jq[]^] Attribute Starts With

```javascript
${1:\$}("${2}[${3:attribute}^='${4:value}']");
```

### [jq:b] button

```javascript
${1:\$}(":button");
```

### [jq:c] checkbox

```javascript
${1:\$}("${2}:checkbox");
```

### [jq:ch] checked

```javascript
${1:\$}("${2}:checked");
```

### [jq:chi] child

```javascript
${1:\$}("${2:parent} > ${3:child}");
```

### [jq:cl] class

```javascript
${1:\$}(".${2:class}");
```

### [jq:co] contains

```javascript
${1:\$}("${2}:contains('${3:text}')");
```

### [jqdes] descendant

```javascript
${1:\$}("${2:ancestor} ${3:descendant}");
```

### [jq:d] disabled

```javascript
${1:\$}("${2}:disabled");
```

### [jq$] element

```javascript
${1:\$}("${2}");
```

### [jq:e] empty

```javascript
${1:\$}("${2}:empty");
```

### [jq:en] enabled

```javascript
${1:\$}("${2}:enabled");
```

### [jq:eq] eq

```javascript
${1:\$}("${2}:eq(${3:indexFromEnd})");
```

### [jq:ev] even

```javascript
${1:\$}("${2}:even");
```

### [jq:f] :file

```javascript
${1:\$}("${2}:file");
```

### [jq:fc] :first-child

```javascript
${1:\$}("${2}:first-child");
```

### [jq:ft] :first-of-type

```javascript
${1:\$}("${2}:first-of-type");
```

### [jq:fi] :first

```javascript
${1:\$}("${2}:first");
```

### [jq:fo] :focus

```javascript
${1:\$}("${2}:focus");
```

### [jq:gt] :gt

```javascript
${1:\$}("${2}:gt(${3:indexFromEnd})");
```

### [jq[]] Has Attribute

```javascript
${1:\$}("${2}[${3:attribute}]");
```

### [jq:h] :has

```javascript
${1:\$}("${2}:has(${3:selector})");
```

### [jq:he] :header

```javascript
${1:\$}(":header");
```

### [jq:hi] :hidden

```javascript
${1:\$}("${2}:hidden");
```

### [jqid] id

```javascript
${1:\$}("#${2}");
```

### [jq:i] :image

```javascript
${1:\$}("${2}:image");
```

### [jq:in] :input

```javascript
${1:\$}("${2}:input");
```

### [jq:l] :lang

```javascript
${1:\$}("${2}:lang(${3:language})");
```

### [jq:lc] :last-child

```javascript
${1:\$}("${2}:last-child");
```

### [jq:lty] :last-of-type

```javascript
${1:\$}("${2}:last-of-type");
```

### [jq:la] :last

```javascript
${1:\$}("${2}:last");
```

### [jq:lt] :lt

```javascript
${1:\$}("${2}:lt(${3:indexFromEnd})");
```

### [jq[][]] Multiple Attribute

```javascript
${1:\$}("${2}[${3}][${4}]");
```

### [jq,] Multiple

```javascript
${1:\$}("${2:selector1}, ${3:selector2}, ${3:selectorN}");
```

### [jq+] Next Adjacent

```javascript
${1:\$}("${2:prev} + ${3:next}");
```

### [jq~] Next Siblings

```javascript
${1:\$}("${2:prev} ~ ${3:siblings}");
```

### [jq:not] not

```javascript
${1:\$}("${2}:not(${3:selector})");
```

### [jq:nc] :nth-child

```javascript
${1:\$}("${2}:nth-child(${3:index})");
```

### [jq:nlc] :nth-last-child

```javascript
${1:\$}("${2}:nth-last-child(${3:index})");
```

### [jq:nlt] :nth-last-of-type

```javascript
${1:\$}("${2}:nth-last-of-type(${3:index})");
```

### [jq:nt] :nth-of-type

```javascript
${1:\$}("${2}:nth-of-type(${3:index})");
```

### [jq:o] :odd

```javascript
${1:\$}("${2}:odd(${3:index})");
```

### [jq:oc] :only-child

```javascript
${1:\$}("${2}:only-child");
```

### [jq:ot] :only-of-type

```javascript
${1:\$}("${2}:only-of-type");
```

### [jq:p] :parent

```javascript
${1:\$}("${2}:parent");
```

### [jq:pa] :password

```javascript
${1:\$}("${2}:password");
```

### [jq:r] :radio

```javascript
${1:\$}("${2}:radio");
```

### [jq:re] :reset

```javascript
${1:\$}("${2}:reset");
```

### [jq:ro] :root

```javascript
${1:\$}("${2}:root");
```

### [jq:s] :selected

```javascript
${1:\$}("${2}:selected");
```

### [jq:su] :submit

```javascript
${1:\$}("${2}:submit");
```

### [jq:t] :target

```javascript
${1:\$}("${2}:target");
```

### [jq:tx] :text

```javascript
${1:\$}("${2}:text");
```

### [jq:v] :visible

```javascript
${1:\$}("${2}:visible");
```

### [jq] animate

```javascript

```
