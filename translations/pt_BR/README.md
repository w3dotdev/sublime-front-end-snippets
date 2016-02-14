# Front-end Project Snippets

[![Travis](https://img.shields.io/travis/brazilian-dev/sublime-front-end-snippets.svg?style=flat-square)](https://travis-ci.org/brazilian-dev/sublime-front-end-snippets)
[![issues](https://img.shields.io/github/issues/brazilian-dev/sublime-front-end-snippets.svg?style=flat-square)](https://github.com/brazilian-dev/sublime-front-end-snippets/issues)
[![Package Control](https://img.shields.io/packagecontrol/dt/Front-end%20Project%20Snippets.svg?style=flat-square)](https://packagecontrol.io/packages/Front-end%20Project%20Snippets)
[![GitHub release](https://img.shields.io/github/release/brazilian-dev/sublime-front-end-snippets.svg?style=flat-square)](https://github.com/brazilian-dev/sublime-front-end-snippets/releases)
[![licence mit](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](http://hemersonvianna.mit-license.org/)

![animation](https://cloud.githubusercontent.com/assets/1963897/12625364/a94decc8-c51a-11e5-8546-ca331af65982.gif)

## Traduções

* [ORIGINAL](https://github.com/brazilian-dev/sublime-front-end-snippets/)

## Instalação

Se você já tem o [Package Control](http://wbond.net/sublime_packages/package_control) instalado, basta procurar por `Front-end Project Snippets`. Se você não tiver instalado no Sublime, você pode fazê-lo [aqui](http://wbond.net/sublime_packages/package_control/installation).

Você pode baixar manualmente o pacote e colocá-lo dentro do seu diretório `Packages`. Ele vai funcionar, mas ele não será atualizado automaticamente.

Você pode ver os snippets instalados em `Tools > Snippets...`, no Sublime Text.

[Testado no windows] Quando o "."(ponto) é utilizado, o autocomplete desaparece. Para resolver esse problema, basta colocar em seu usuário `Preferences >  Settings - User`, a propriedade `word_separators` com o valor sem "."(ponto). Você pode ver um exemplo [aqui](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/Preferences.sublime-settings).

## Snippets e prefixos/chaves

- [HTML - h.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/html/)
  - [Microdata - hm.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/html/schema/microdata)
  - [WAI-ARIA - hw.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/html/wai-aria)
- [CSS - c.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/css/) 
- [JavaScript - j.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/vanilla)
  - [EcmaScript 2015 - je.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/es6/)
  - [Libraries](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/libraries)
    - [jQuery - jq.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/libraries/jquery)
    - [React - jr.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/libraries/react)
  - [Patterns](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/patterns)
    - [Design Patterns - jdp.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/patterns/design-patterns)
    - [UMD - jumd.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/patterns/umd)
  - [Tests](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests)
    - [Common - t.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/common)
    - [Chai - tc.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/chai)
    - [Jasmine - tj.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/jasmine)
    - [Mocha - tm.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/mocha)
    - [Node - tn.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/node)
    - [QUnit - tq.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/qunit)
    - [Sinon - ts.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/js/tests/sinon)
- [Regex](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/regex/)
- [Schema.org](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/schema)
  - [JSON-LD - sj.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/schema/json-ld)
  - [Microdata - sm.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/schema/microdata)
  - [RDFa - sr.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/schema/rdfa)
- [External - e.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/external/)
- [Comment](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/comment/)
  - [HTML - hc.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/comment/html)
  - [CSS - cc.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/comment/css)
  - [JavaScript - jc.*](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/comment/js)
- [Structure data](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/structured-data) (***examples***)
  - [Microdata - z.microdata](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/structured-data/microdata)
  - [JSON-LD - z.jsonld](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/structured-data/json-ld)
  - [RDFa - z.rdfa](https://github.com/brazilian-dev/sublime-front-end-snippets/blob/master/snippets/structured-data/rdfa)

## Referências

* [@caiogondim](https://github.com/caiogondim) (Caio Gondim)
  [https://github.com/caiogondim/js-patterns-sublime-snippets](https://github.com/caiogondim/js-patterns-sublime-snippets)
* [@zenorocha](https://github.com/zenorocha) (Zeno Rocha)
  [https://github.com/zenorocha/sublime-javascript-snippets](https://github.com/zenorocha/sublime-javascript-snippets)
* [@joshnh](https://github.com/joshnh) (Joshua Hibbert)
  [https://github.com/joshnh/CSS-Snippets](https://github.com/joshnh/CSS-Snippets)
* (Schema.org) [http://schema.org/](http://schema.org/)
* (jQuery) [https://api.jquery.com/](https://api.jquery.com/)
* (jQuery Boilerplate)[https://jqueryboilerplate.com/](https://jqueryboilerplate.com/)
* (JSDuck) [https://github.com/senchalabs/jsduck](https://github.com/senchalabs/jsduck)
* (idiomatic CSS) [https://github.com/necolas/idiomatic-css](https://github.com/necolas/idiomatic-css)
* (JS Design Patterns) [https://addyosmani.com/resources/essentialjsdesignpatterns/book/](https://addyosmani.com/resources/essentialjsdesignpatterns/book/)
* (Node.js Assert) [https://nodejs.org/api/assert.html](https://nodejs.org/api/assert.html)
* (Jasmine) [http://jasmine.github.io/2.0/introduction.html](http://jasmine.github.io/2.0/introduction.html)
* (ReactJS cheatsheet) [http://reactcheatsheet.com/](http://reactcheatsheet.com/)
* (ES6 Features) [https://github.com/lukehoban/es6features#readme](https://github.com/lukehoban/es6features#readme)

## Contribuindo

- Faça o fork!
- Crie a sua branch feature: `git checkout -b my-new-feature`
- Faça o commit das suas alterações: `git commit -m 'Add some feature'`
- Faça o push para o servidor: `git push origin my-new-feature`
- E realize o pull request

## Log

Verifique os [Releases](https://github.com/brazilian-dev/sublime-front-end-snippets/releases) ver detalhado o log de alterações.

## Licença

[MIT license](http://hemersonvianna.mit-license.org/) © Hemerson Vianna
