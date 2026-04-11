---
title: "Приватность в Биткоине: исследования OXT"
category: "series"
quality: "synthesized"
sources: ["https://21ideas.org/privacy/oxt", "https://21ideas.org/privacy/oxt-1", "https://21ideas.org/privacy/oxt-2", "https://21ideas.org/privacy/oxt-3", "https://21ideas.org/privacy/oxt-4"]
synthesized_date: "2026-04-08"
completeness: "medium"
language: "ru"
tags: [bitcoin, wiki, privacy, utxo, concept, security, synthesized]
updated: "2026-04-11"
reviewed: "2026-04-11"
---

Серия из четырёх статей от разработчиков кошелька Samourai, опубликованных в блоге OXT Research. Технический анализ [[ru/concepts/privacy|приватности]] [[ru/glossary#Транзакция|транзакций]] [[ru/concepts/bitcoin|Биткоина]]: как работает анализ [[ru/concepts/blockchain|блокчейна]] и как от него защититься.

Основа: [хаб цикла на 21ideas](https://21ideas.org/privacy/oxt); части [1](https://21ideas.org/privacy/oxt-1)–[4](https://21ideas.org/privacy/oxt-4).

## Структура серии

| Часть | Название | Содержание |
| --- | --- | --- |
| 1 | [Анализ цепочки и приватность транзакций](https://21ideas.org/privacy/oxt-1) | Что раскрывает блокчейн наблюдателю |
| 2 | [Ключевые концепции анализа цепочки](https://21ideas.org/privacy/oxt-2) | Эвристики, паттерны, fingerprinting |
| 3 | [Защита от анализа цепочки](https://21ideas.org/privacy/oxt-3) | Практические методы защиты |
| 4 | [Применение концепций для улучшения приватности](https://21ideas.org/privacy/oxt-4) | Пошаговое руководство |

## Часть 1: Анализ цепочки

Биткоин — псевдоанонимная система. Все транзакции публичны в [[ru/concepts/blockchain|блокчейне]]. Анализ цепочки (chain analysis) — методология деанонимизации участников транзакций:

- Кластеризация адресов: если несколько [[ru/concepts/utxo|UTXO]] использованы как входы одной [[ru/glossary#Транзакция|транзакции]], они, вероятно, принадлежат одному кошельку
- Отслеживание потоков монет: «помеченные» биткоины (связанные с биржами или незаконной деятельностью) можно отследить

## Часть 2: Ключевые концепции

**Эвристики** — предположения, позволяющие с высокой вероятностью деанонимизировать участников:

- **Common Input Ownership**: все входы транзакции принадлежат одному владельцу
- **Change detection**: выход с нестандартной суммой — сдача; выход с «ровной» суммой — платёж
- **Address reuse**: повторное использование [[ru/concepts/address-types|адреса]] раскрывает историю транзакций

## Часть 3: Защита

Методы защиты от анализа цепочки:

- **[[ru/practice/privacy-practice#CoinJoin|CoinJoin]]**: несколько участников объединяют транзакции, делая трассировку монет неоднозначной
- **Payjoin**: продавец и покупатель объединяют UTXO в одну транзакцию
- **[[ru/practice/privacy-practice#Coin Control|Coin control]]**: ручной выбор UTXO для каждой транзакции
- **[[ru/concepts/lightning-network|Lightning Network]]**: офчейн-платежи не видны в блокчейне

## Часть 4: Практическое применение

Конкретные рекомендации для пользователей Samourai (теперь Ashigaru) и других кошельков с поддержкой приватности. Ключевой принцип: приватность требует активных усилий — по умолчанию [[ru/concepts/blockchain|блокчейн]] прозрачен.

## Источники

- [Понимание приватности в сети Биткоин с помощью OXT — хаб цикла](https://21ideas.org/privacy/oxt)
- [Часть 1: Анализ цепочки и приватность транзакций](https://21ideas.org/privacy/oxt-1)
- [Часть 2: Ключевые концепции анализа цепочки](https://21ideas.org/privacy/oxt-2)
- [Часть 3: Защита от анализа цепочки](https://21ideas.org/privacy/oxt-3)
- [Часть 4: Применение концепций анализа цепочки для улучшения приватности пользователей](https://21ideas.org/privacy/oxt-4)

## Дополнительные материалы

- [[ru/concepts/privacy|Приватность в Биткоине — основы]]
- [[ru/concepts/utxo|UTXO — модель и след в блокчейне]]
- [[ru/practice/privacy-practice|Практики приватности: CoinJoin, coin control, Tor]]
- [[ru/concepts/lightning-network|Lightning Network — офчейн-платежи]]
