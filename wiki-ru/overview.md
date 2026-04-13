---
title: "Введение в 21wiki"
category: "overview"
quality: "synthesized"
sources: []
synthesized_date: "2026-04-08"
completeness: "high"
language: "ru"
tags: [bitcoin, wiki, overview, navigation]
updated: "2026-04-11"
reviewed: "2026-04-11"
---

Эта вики — синтезированная база знаний по Биткоину на русском языке. Все страницы написаны на основе оригинальных русскоязычных источников сайта 21ideas.org и курируются автором проекта [Тони](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7).

## О пректе

21ideas.org — некоммерческий образовательный проект, посвящённый только Биткоину. За годы работы на сайте накопились сотни материалов: переводы книг, серии статей, руководства, история. 21wiki — структурированный дистиллят этих знаний.

**Вики не заменяет оригинальные материалы** — она служит картой и точкой входа. Для глубокого погружения читайте первоисточники по ссылкам на каждой странице.

## Как читать

### Если вы только начинаете

1. Прочитайте [[ru/concepts/bitcoin]] — базовое понимание протокола
2. Изучите [[ru/glossary]] — словарь терминов
3. Прочитайте [[ru/concepts/money]] — почему понимание концепта денег важно
4. Продолжите с книгами [[ru/books/inventing-bitcoin|Изобретаем Биткоин]] или [[ru/books/sovereignty-through-mathematics|Суверенитет посредством математики]] — каждая уместила самое важное в 100 страниц А5

### Если вас интересует история

1. [[ru/history/pre-bitcoin-cypherpunks]] — откуда взялся Биткоин
2. [[ru/entities/cypherpunks]] — люди, непосредственно повлиявшие на создание Биткоина
3. [[ru/series/genesis-files]] — детальный разбор каждого предшественника
4. [[ru/history/timeline]] — хронология ключевых событий
5. [[ru/history/blocksize-war]] — война за размер блока (2015–2017)

### Если вас интересует экономика

1. [[ru/concepts/money]] — функции денег и их история
2. [[ru/concepts/cantillon-effect]] — как инфляция перераспределяет богатство
3. [[ru/concepts/scarcity]] — о значимости редкости и ограничения в 21 миллион 
4. [[ru/series/gradually-then-suddenly]] — 17 эссе Паркера Льюиса

### Если вас интересует философия и культура

1. [[ru/philosophy/overview]] — философские основы Биткоина
2. [[ru/books/21-ways]] — Gigi: «21 способ понять Биткоин»
3. [[ru/topics/bitcoin-dissidents]] — Биткоин как инструмент свободы
4. [[ru/topics/network-effects]] — сетевые эффекты и устойчивость системы

### Если вы хотите начать использовать Биткоин

1. [[ru/practice/buying]] — как купить
2. [[ru/practice/storage]] — как безопасно хранить
3. [[ru/practice/lightning-tools]] — как использовать Lightning для повседневных платежей
4. [[ru/concepts/security]] — основы безопасности
5. [[ru/practice/privacy-practice]] — приватность в Биткоине: coin control, CoinJoin, Tor
6. [[ru/practice/running-a-node]] — свой узел: верификация правил и независимость

### Если вас интересует техническая сторона

1. [[ru/concepts/proof-of-work]] — механизм консенсуса
2. [[ru/concepts/mining]] — как устроена добыча блоков (майнинг)
3. [[ru/concepts/utxo]] — модель хранения балансов
4. [[ru/concepts/segwit]] и [[ru/concepts/taproot]] — ключевые обновления протокола
5. [[ru/concepts/protocol-stack]] — многоуровневая архитектура
6. [[ru/concepts/lightning-network]] — платёжные каналы и Lightning поверх базового слоя

## Структура вики

```
wiki-ru/
├── index.md                    ← каталог всех страниц
├── overview.md                 ← этот файл
├── glossary.md                 ← словарь терминов
├── concepts/                   ← 35 концептуальных страниц
├── entities/                   ← 12 биографических страниц
├── history/                    ← 3 исторические страницы
├── philosophy/                 ← 1 философская страница
├── books/                      ← 8 книг
├── series/                     ← 7 серий статей
├── practice/                   ← 5 практических руководств
└── topics/                     ← 2 тематические страницы
```

## О качестве

Каждая страница содержит метаданные в YAML frontmatter (строковые поля, список `tags:`; подробности в `CLAUDE.md` и `PAGE-ENHANCEMENT-STANDARD.md`):

- `quality: "synthesized"` — написано на основе нескольких источников
- `quality: "reference"` — описание конкретного источника (книги, серии)
- `completeness: "high"` / `"medium"` / `"low"` — степень охвата темы

Страницы с `completeness: medium` и `completeness: low` можно расширить при появлении новых источников.

## Навигация через Obsidian

В Obsidian используйте:
- **Graph view** — визуальная карта связей между страницами
- **Backlinks** — что ссылается на текущую страницу
- **wikilinks** — переходы между статьями
- **Dataview** ([плагин](obsidian://show-plugin?id=dataview)) — динамические запросы по тегам и категориям

## Принять участие

- Начните здесь: [Участие в 21wiki](./contribute)
- Если вики оказалась полезной, [поддержите 21wiki](./support)
- Предложите тему или сообщите об ошибке, [открыв GitHub Issue](https://github.com/21ideas-org/21ideas-wiki/issues/new/choose)

## Дополнительные материалы

- [[ru/index]] — полный каталог вики
- [[ru/glossary]] — словарь терминов
- [[ru/concepts/bitcoin]] — с чего начать
- [[ru/philosophy/overview]] — философия
- [[ru/history/timeline]] — хронология

---

*⚡️ Проект оказался полезным? [Закиньте пару сат](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [автору](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7)*
