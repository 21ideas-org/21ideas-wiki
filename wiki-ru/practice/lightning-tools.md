---
title: "Лайтнинг: инструменты и кошельки"
category: "practice"
quality: "reference"
sources: ["https://21ideas.org/practice/lightning", "https://21ideas.org/phoenix", "https://21ideas.org/mutiny", "https://21ideas.org/lnbits", "https://21ideas.org/alby-i-nostr", "https://21ideas.org/zapplanner", "https://21ideas.org/zapgram", "https://21ideas.org/ochishchaem-bitcoin-cherez-lajtning", "https://21ideas.org/likvidnost-v-lajtning"]
synthesized_date: "2026-04-08"
completeness: "high"
language: "ru"
tags: [bitcoin, wiki, lightning, privacy, security, multisig, concept, reference]
updated: "2026-04-11"
reviewed: "2026-04-11"
---

## Введение

[[ru/concepts/lightning-network|Lightning Network]] — сеть платёжных каналов поверх [[ru/concepts/bitcoin|Биткоина]]. Мгновенные [[ru/glossary#Транзакция|транзакции]] с минимальными [[ru/glossary#Комиссия (Transaction Fee)|комиссиями]]. Для работы с Lightning нужен отдельный [[ru/glossary#Кошелёк|кошелёк]].

Основа: [раздел «Лайтнинг на практике» на 21ideas](https://21ideas.org/practice/lightning).

## Мобильные кошельки

### Phoenix Wallet

**Лучший выбор для большинства пользователей.** Гид: [кошелёк Phoenix на 21ideas](https://21ideas.org/phoenix).

- iOS и Android
- Некастодиальный: вы контролируете [[ru/glossary#Ключ (приватный / публичный)|ключи]]
- Автоматическое управление каналами (не нужно понимать, как работают каналы)
- Поддержка BOLT 12 (обновлённый стандарт Lightning-инвойсов)
- Разработчик: ACINQ (Франция)

Phoenix — наиболее сбалансированный вариант: некастодиальный, но при этом простой в использовании.

### Mutiny

Некастодиальный кошелёк в браузере. Гид: [Mutiny на 21ideas](https://21ideas.org/mutiny).

- Ключи в браузере, можно резервировать
- LSP для входящей ликвидности
- Интеграция с Nostr
- Удобно без установки из магазина приложений; есть компромиссы [[ru/concepts/security|безопасности]] браузерных кошельков

## Инструменты для продвинутых пользователей

### LNbits

«Швейцарский нож» Lightning-экосистемы. Гид: [LNbits на 21ideas](https://21ideas.org/lnbits).

- Набор приложений для вашего Lightning-[[ru/glossary#Нода (Узел)|узла]]
- Плагины: точка продаж (PoS), сплит-платежи, подписки, фаустет (кран для тестирования), Discord/Telegram-бот
- Можно развернуть на собственном сервере или использовать публичный инстанс
- Подходит для Lightning-экосистемы вашего сообщества или бизнеса
- Требуется бэкенд-узел (LND, Core Lightning и т.д.); см. [[ru/practice/running-a-node|запуск узла]]

### Alby

Браузерное расширение для Lightning и Nostr. Гид: [Alby и Nostr на 21ideas](https://21ideas.org/alby-i-nostr).

- Интеграция с веб-сайтами: оплата одним кликом (WebLN)
- Поддержка Nostr: автоматические zap-платежи
- Lightning-адрес в формате `имя@домен`
- Работает с вашим Lightning-узлом, LNbits, хабом Alby и др.

## Дополнительные инструменты

### ZapPlanner

Сервис для настройки регулярных Lightning-платежей (подписок). Гид: [подписки через Lightning на 21ideas](https://21ideas.org/zapplanner). Поддерживает расписание автоматических транзакций без необходимости держать кошелёк открытым.

### ZapGram

Telegram-бот для приёма и отправки биткоинов через Lightning прямо в чате. Гид: [ZapGram на 21ideas](https://21ideas.org/zapgram). Подходит для сообществ и групп.

## Управление ликвидностью

Для продвинутых пользователей, запускающих собственный Lightning-узел. Подробнее: [руководство по ликвидности на 21ideas](https://21ideas.org/likvidnost-v-lajtning).

- **Входящая ликвидность**: без неё нельзя принимать платежи
- **Балансировка каналов**: поддержание ликвидности на обеих сторонах
- **Loop и Pool**: сервисы Lightning Labs для управления ликвидностью

## Lightning и ончейн-приватность

Перевод средств через Lightning с последующим выводом на цепь может снижать тривиальную ончейн-следимость (не замена полноценному CoinJoin). Гид: [«Очищаем биткоины через сеть Лайтнинг» на 21ideas](https://21ideas.org/ochishchaem-bitcoin-cherez-lajtning). См. [[ru/practice/privacy-practice|приватность на практике]].

## С чего начать

1. Установите **Phoenix** на телефон
2. Получите первый биткоин через Lightning (с [[ru/glossary#Биржа|биржи]] или от друга)
3. Попробуйте сделать первый платёж в магазине, поддерживающем Lightning

## Источники

- [Лайтнинг на практике (оглавление)](https://21ideas.org/practice/lightning)
- [Phoenix](https://21ideas.org/phoenix)
- [Mutiny](https://21ideas.org/mutiny)
- [LNbits](https://21ideas.org/lnbits)
- [Alby и Nostr](https://21ideas.org/alby-i-nostr)
- [ZapPlanner — подписки](https://21ideas.org/zapplanner)
- [ZapGram](https://21ideas.org/zapgram)
- [Очищаем биткоины через Лайтнинг](https://21ideas.org/ochishchaem-bitcoin-cherez-lajtning)
- [Управление ликвидностью в Lightning](https://21ideas.org/likvidnost-v-lajtning)

## Дополнительные материалы

- [[ru/concepts/lightning-network|Как устроен Lightning Network]]
- [[ru/practice/running-a-node|Запуск узла Биткоина / Lightning]]
- [[ru/practice/privacy-practice|Приватность на практике]]
- [[ru/practice/storage|Хранение ончейн-биткоинов]]
- [[ru/concepts/privacy|Приватность в Биткоине и Lightning]]
- [[ru/concepts/security|Безопасность и ключи]]
- [[ru/concepts/multisig|Мультиподпись (в т.ч. эскроу в P2P)]]
