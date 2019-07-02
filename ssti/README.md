# уязвимость/атака

## Описание
Попытайтесь описать почему возникает проблема, чтобы стало понятно как это работает

Template engines are widely used by web applications to present dynamic data via web pages and emails. Unsafely embedding user input in templates enables Server-Side Template Injection, a frequently critical vulnerability that is extremely easy to mistake for Cross-Site Scripting (XSS), or miss entirely. Unlike XSS, Template Injection can be used to directly attack web servers' internals and often obtain Remote Code Execution (RCE), turning every vulnerable application into a potential pivot point.

Template Injection can arise both through developer error, and through the intentional exposure of templates in an attempt to offer rich functionality, as commonly done by wikis, blogs, marketing applications and content management systems. Intentional template injection is such a common use-case that many template engines offer a 'sandboxed' mode for this express purpose. This paper defines a methodology for detecting and exploiting template injection, and shows it being applied to craft RCE zerodays for two widely deployed enterprise web applications. Generic exploits are demonstrated for five of the most popular template engines, including escapes from sandboxes whose entire purpose is to handle user-supplied templates in a safe way.

For a slightly less dry account of this research, you may prefer to watch my Black Hat USA presentation on this topic. This research is also available as printable whitepaper.

## Классификация
Если существует какая-то классификация уязвимости/атаки - напишите о ней. Например, могут быть разные техники эксплуатации

## Условия
- ОС: если проблема специфична для определенной ОС
- язык: если проблема специфичная для определенных языков
- компоненты: какие компоненты подвержены проблеме. Это могут быть библиотеки, базы данных, фреймворки, брокеры очередей и т.д.
- настройки: может есть какие-то специфичные настройки

Можно добавить еще информацию, которая не подходит под пункты выше, самостоятельно

## Детектирование
Описать как проблема детектируется. На что обращают внимание. Можно ли проблему детектировать автоматизированно или только вручную.
Если автоматизированно, то как лучше детектировать - код ревью или сканирование уязвимостей?

Информация:
- в каждый пункт можно добавлять необходимую информацию из статей в ввиде ссылок - [google.com](https://www.google.com)

## Эксплуатация
Здесь необходимо описать пример ручной эксплуатации. Сразу уточните какой это язык, какие компоненты используются, если эксплуатация специфична только для этих условий. Можно записать сюда порядок действий при эксплуатации тестового задания

### Инструменты
- здесь можно перечислить ссылками инструменты и полезную информацию, которая может понадобиться для эксплуатации

## Ущерб
Описать во что возможно развитие вектора атаки, если не существует защитных мер вовсе. То есть описать, что максимльно может получить злоумышленник, если все условия сойдутся.

Написать, к чему могут привести в итоге эксплуатация этих векторов атак

## Защита
### Основные меры
В основных мерах описываем способы как 100% защититься от уязвимости/атаки

### Превентивные меры
А здесь описываем как можем уменьшить ущерб от уязвимости/атаки, если она существует. То есть, подход Defense in Depth.

## Дополнительно
Здесь приложить дополнительную информацию и источники, которые использовали, но не указали выше в других местах.

## Обход защиты
Если существуют варианты обхода защиты, то можно их здесь перечислить.

Если есть возможность, то надо написать в чем заключается защита и каким образом она обходится.
