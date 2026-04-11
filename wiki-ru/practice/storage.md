---
title: "Хранение биткоинов"
category: "practice"
quality: "reference"
sources: ["https://21ideas.org/practice/hodl", "https://21ideas.org/electrum", "https://21ideas.org/blue", "https://21ideas.org/coldcard", "https://21ideas.org/seedsigner"]
synthesized_date: "2026-04-08"
completeness: "high"
language: "ru"
tags: [bitcoin, wiki, security, privacy, multisig, concept, reference]
updated: "2026-04-11"
reviewed: "2026-04-11"
---

## Введение

[[ru/concepts/security|Самостоятельное хранение (self-custody)]] — хранение [[ru/concepts/bitcoin|биткоинов]] на [[ru/glossary#Кошелёк|кошельке]], где только вы контролируете [[ru/glossary#Приватный ключ|приватный ключ]]. Это единственный способ по-настоящему владеть биткоинами.

Основа: [раздел «Хранение» на 21ideas](https://21ideas.org/practice/hodl).

## Уровни хранения

### Уровень 1: [[ru/glossary#Горячий кошелёк|Горячий кошелёк]] (телефон/компьютер)

Подходит для небольших сумм и повседневных платежей. Ключи хранятся на устройстве, подключённом к интернету.

**Blue Wallet** — гид на 21ideas: [BlueWallet](https://21ideas.org/blue).

- Простейший кошелёк для iOS и Android
- Поддержка [[ru/concepts/lightning-network|Lightning]]
- Нет проверки личности — просто установите и получите [[ru/concepts/address-types|адрес]]
- Для небольших сумм (до ~$500)

**Electrum** — гид на 21ideas: [кошелёк Electrum](https://21ideas.org/electrum).

- Настольный кошелёк для Windows/Mac/Linux
- Полный контроль над [[ru/concepts/utxo|UTXO]], [[ru/glossary#Комиссия (Transaction Fee)|комиссиями]], coin control
- Поддержка [[ru/glossary#Аппаратный кошелёк|аппаратных кошельков]]
- Рекомендуется для технически грамотных пользователей

### Уровень 2: [[ru/glossary#Аппаратный кошелёк|Аппаратный кошелёк]] ([[ru/glossary#Холодное хранение|холодное хранение]])

Ключи никогда не покидают устройство. Идеально для основных сбережений.

**Coldcard** — гид на 21ideas: [что такое Coldcard](https://21ideas.org/coldcard).

- Самый безопасный аппаратный кошелёк
- Работает в полностью air-gapped режиме (через SD-карту или QR)
- Поддержка [[ru/concepts/multisig|мультиподписи]]
- Прозрачный корпус, несколько уровней PIN-защиты
- Рекомендован для опытных пользователей и крупных сумм

**SeedSigner** — гид на 21ideas: [SeedSigner своими руками](https://21ideas.org/seedsigner).

- DIY-кошелёк на базе Raspberry Pi Zero
- Полностью air-gapped: работает без интернета, без постоянной памяти
- Seed-фраза вводится каждый раз при включении через скан QR-кода
- Открытый исходный код — можно собрать самостоятельно
- Оптимальный баланс между [[ru/concepts/security|безопасностью]] и стоимостью

### Уровень 3: Мультиподпись

Для крупных сумм. [[ru/concepts/multisig|Мультисиг]] 2-из-3 устраняет единую точку отказа.

## Правила безопасного хранения

### [[ru/glossary#Сид-фраза (Seed Phrase / Мнемоническая фраза)|Seed-фраза]] (12 или 24 слова)

- **Запишите на бумаге или металле** — никогда в цифровой форме
- **Никому не показывайте** — кто знает seed, контролирует ваши биткоины
- **Храните в надёжном месте** — огнеупорный сейф, банковская ячейка, несколько копий в разных местах
- **Проверьте восстановление** — убедитесь, что можете восстановить кошелёк по сид-фразе

### Passphrase (опционально)

25-е слово к seed-фразе создаёт отдельный кошелёк. Даже при краже физического устройства — без passphrase средства недоступны.

## Типичные ошибки

- Хранение сид-фразы в телефоне или облаке
- Покупка аппаратного кошелька с рук (может быть скомпрометирован)
- Отсутствие резервной копии
- Использование только одного устройства без резервирования

## С чего начать

1. Установите **Blue Wallet** на телефон для небольших сумм
2. При накоплении от ~$1000 — купите **Coldcard** или соберите **SeedSigner**
3. Запишите сид-фразу и проверьте восстановление
4. При значительных суммах — переходите на [[ru/concepts/multisig|мультиподпись]]

## Источники

- [Хранение — раздел на 21ideas](https://21ideas.org/practice/hodl)
- [Electrum](https://21ideas.org/electrum)
- [BlueWallet](https://21ideas.org/blue)
- [Coldcard](https://21ideas.org/coldcard)
- [SeedSigner](https://21ideas.org/seedsigner)

## Дополнительные материалы

- [[ru/concepts/security|Безопасность и self-custody]]
- [[ru/concepts/multisig|Мультиподпись для крупных сумм]]
- [[ru/concepts/utxo|UTXO и coin control]]
- [[ru/practice/buying|Как купить биткоин]]
- [[ru/practice/privacy-practice|Приватность при хранении и тратах]]
- [[ru/practice/lightning-tools|Lightning-кошельки для горячего слоя]]
- [[ru/practice/running-a-node|Собственный узел и приватность запросов]]
