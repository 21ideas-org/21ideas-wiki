---
title: "Bitcoin Core"
category: concepts
tags: [bitcoin, wiki, bitcoin-core, full-node, software, open-source, governance, upgrades]
quality: reference
sources:
  - "https://21ideas.org/kto-kontroliruet-bitkoin-kor/"
  - "https://21ideas.org/izobretaem-bitkoin/glava-8"
  - "https://21ideas.org/o-zakostenenii-protokola"
synthesized_date: "2026-04-09"
completeness: high
language: ru
---

# Bitcoin Core

*Теги: реализация, ПО полной ноды, open source, обновления*

---

## Что такое Bitcoin Core (и чем он не является)

Источники проводят границу между:

- **Биткоином как протоколом / правилами** — тем, что узлы проверяют и применяют ([[ru/concepts/governance]])
- **Bitcoin Core как программной реализацией** — самым распространённым кодом, реализующим эти правила

Статья «Кто контролирует Bitcoin Core?» утверждает, что Core — это скорее **центр координации разработки**, а не орган управления. Если Core исчезнет, разработка может переехать в другое место; пользователей нельзя заставить обновляться.

Источник: `raw/Theory/protocol/who-controls-bitcoin-core.md`

---

## Почему Core доминирует на практике

В «Изобретаем Биткоин» сказано, что реализаций много, но ошибки консенсуса крайне опасны: если две реализации трактуют правила по-разному, сеть может расколоться.

Лопп добавляет два практических объяснения:

- у протокола нет единой формальной «спеки», поэтому наиболее распространённая реализация — самый безопасный ориентир;
- в Core сосредоточены ревью, тестирование и инженерная «закалка».

Источники: `raw/Books/izobretaem-bitkoin/glava-8.md`, `raw/Theory/protocol/who-controls-bitcoin-core.md`

---

## Как изменения проходят через процесс (BIP, ревью, релизы)

Код-изменения проходят через:

- публичные предложения (pull requests),
- ревью контрибьюторов,
- слияния (merge) дежурными с ограниченными правами,
- релизы — при этом **автообновления для нод намеренно нет**.

Контекст обновлений как социальных изменений правил — см. [[ru/concepts/bip]] и [[ru/concepts/forks]].

Источники: `raw/Theory/protocol/who-controls-bitcoin-core.md`, `raw/Books/izobretaem-bitkoin/glava-8.md`

---

## Дежурные, подписи и «не доверяй GitHub»

В статье подчёркнут подход к безопасности: GitHub — не корень доверия. Слияния подписываются PGP-ключами; историю можно проверять инструментами Core (например `verify-commits`).

Это не «идеальная защита», но усложняет внедрение вредоносного кода.

Источник: `raw/Theory/protocol/who-controls-bitcoin-core.md`

---

## Закостенение vs эволюция

«О закостенении протокола» описывает напряжение: чем больше сеть, тем труднее координировать изменения. Преждевременная «заморозка» может вытолкнуть сложность на верхние уровни и вернуть доверие/централизацию. Автор выступает за осторожную эволюцию на основе консенсуса.

Источник: `raw/Theory/protocol/on-ossification.md`

---

## Источники

- [Кто контролирует Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/)
- [Изобретаем Биткоин — гл. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [О закостенении протокола](https://21ideas.org/o-zakostenenii-protokola)

---

## Связанные термины

[[ru/glossary|Глоссарий]] | [[ru/concepts/governance|управление]] | [[ru/concepts/bip|BIP]] | [[ru/concepts/forks|форки]] | [[ru/concepts/bitcoin-node|Биткоин-нода]] | [[ru/practice/running-a-node|своя нода]]

## Связанные страницы

- [[ru/concepts/governance]] — кто применяет правила
- [[ru/concepts/bitcoin-node]] — узел vs майнер
- [[ru/concepts/bip]] — предложения и контекст активации
- [[ru/concepts/forks]] — несовместимые изменения и расколы
- [[ru/concepts/third-parties]] — почему проверка снижает TTP-риск
