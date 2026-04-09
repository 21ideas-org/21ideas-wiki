---
title: "Биткоин-нода"
category: concepts
tags: [bitcoin, wiki, node, full-node, validation, privacy, sovereignty, p2p]
quality: reference
sources:
  - "https://21ideas.org/practice/bitcoin-node/"
  - "https://21ideas.org/izobretaem-bitkoin/glava-8"
  - "https://21ideas.org/izobretaem-bitkoin/glava-2"
synthesized_date: "2026-04-09"
completeness: high
language: ru
---

# Биткоин-нода

*Теги: полная нода, валидация, ретрансляция, суверенитет*

---

## Что такое биткоин-нода

**Биткоин-нода** — это компьютер с установленным биткоин-программным обеспечением, который участвует в P2P-сети: обменивается транзакциями и блоками и (в случае полной ноды) независимо проверяет их по правилам консенсуса.

Источник: `raw/Practice/interact/bitcoin-node.md`

---

## Две роли: сеть и применение правил

В практическом материале выделяются две ключевые функции:

- **Сетевая:** ноды ретранслируют транзакции и блоки, помогая сети синхронизироваться.
- **Валидация:** полные ноды загружают блоки и проверяют каждую транзакцию; нарушения правил автоматически отклоняются.

Отсюда смысл лозунга «не доверяй — проверяй» как практики: своя нода — это проверка реальности без посредника.

Источник: `raw/Practice/interact/bitcoin-node.md`

---

## Полная нода и лёгкий клиент (SPV)

Материал также сравнивает:

- **Полная нода:** всё проверяет и хранит цепь; применяет правила локально.
- **Лёгкий / SPV-клиент:** дешевле, но не проверяет всю историю и слабее по модели доверия.

Источник: `raw/Practice/interact/bitcoin-node.md`

---

## Как нода уменьшает зависимость от третьих сторон

В «Изобретаем Биткоин» традиционные системы описаны как централизованные реестры. Нода — это способ иметь собственную копию реестра и не зависеть от обозревателей, кастодианов и процессоров платежей при проверке баланса и правил.

Источники: `raw/Books/izobretaem-bitkoin/glava-2.md`, `raw/Practice/interact/bitcoin-node.md`

---

## Ноды, Bitcoin Core и изменение правил

В «Изобретаем Биткоин» сказано: реализаций много, но наиболее распространённая — **Bitcoin Core**. При этом именно узлы являются слоем применения правил: майнеры производят блоки, а узлы решают, считать ли их валидными.

См. [[ru/concepts/bitcoin-core]] и [[ru/concepts/governance]].

Источник: `raw/Books/izobretaem-bitkoin/glava-8.md`

---

## Источники

- [Каждому следует запустить собственную Биткоин-ноду!](https://21ideas.org/practice/bitcoin-node/)
- [Изобретаем Биткоин — гл. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [Изобретаем Биткоин — гл. 2](https://21ideas.org/izobretaem-bitkoin/glava-2)

---

## Связанные термины

[[ru/glossary|Глоссарий]] | [[ru/concepts/bitcoin-core|Bitcoin Core]] | [[ru/concepts/governance|управление]] | [[ru/concepts/decentralization|децентрализация]] | [[ru/concepts/third-parties|третьи стороны]] | [[ru/concepts/censorship-resistance|цензуроустойчивость]] | [[ru/concepts/proof-of-work|Proof of Work]]

## Связанные страницы

- [[ru/practice/running-a-node]] — практические шаги
- [[ru/concepts/governance]] — кто и как применяет правила
- [[ru/concepts/third-parties]] — почему аутсорс валидации = TTP
- [[ru/concepts/censorship-resistance]] — почему важна распределённость узлов
