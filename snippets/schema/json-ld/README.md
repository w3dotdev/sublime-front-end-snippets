# JSON-LD Snippets

## Prefix `sj.*`

## Organization

### [sj.logo] Logotype

```html
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "Organization",
  "url": "${1:http://www.example.com}",
  "logo": "${2:http://www.example.com/images/logo.png}"
}
</script>
```
