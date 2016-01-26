# HTML Snippets

Prefix `h*`

## Structure

### [hb] html basic

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>${1:Document}</title>
  </head>
  <body>
    $2
  </body>
</html>
```

### [hdoc] html document

```html
<!DOCTYPE html>
<html class="no-js" lang="${2:pt-BR}" xml:lang="${2:pt-BR}">
  <head>
    <meta charset="utf-8">
    <title>${1:Document}</title>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
      <script type="text/javascript">
        // to identify if javascript is active
        var tagHtml = document.getElementsByTagName("html")[0];
            tagHtml.className = tagHtml.className.replace('no-js', 'js');
      </script>
  </head>
  <body>
    $2
  </body>
</html>
```

### [hhtags] head tags

```html
<meta name="format-detection" content="telephone=no">
<meta name="referrer" content="origin">
<meta name="description" content="${1:Description}">

<!-- facebook -->
<meta property="og:site_name" content="${2:Site name}">
<meta property="og:title" content="${3:Title}">
<meta property="og:type"  content="website">
<meta property="og:url" content="${4:Url}">
<meta property="og:description" content="${1:Description}">
<meta property="og:image" content="${5:Image}">
<meta property="fb:admins" content="$6">
<meta property="fb:app_id" content="$7">

<link rel="image_src" href="${5:Image}">

<!-- component schema.org -->
<meta itemprop="name" content="${2:Site name}">
<meta itemprop="description" content="${1:Description}">
<meta itemprop="image" content="${5:Image}">
<meta itemprop="url" content="${4:Url}">

<meta name="geo.country" content="$8">
<meta name="geo.region" content="$9">
<meta name="geo.placename" content="$10">

<!-- favicon -->
<link rel="apple-touch-icon" href="$11/apple-touch-icon.png">
<link rel="shortcut icon" href="$12/favicon.ico" type="image/x-icon">
<link rel="icon" href="$13/favicon.ico" type="image/x-icon">

<!-- canonical -->
<link rel="canonical" href="${4:Url}">
```
