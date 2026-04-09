---
title: "Мемпул"
category: concepts
tags: [bitcoin, wiki, protocol, mining, transactions]
language: ru
quality: reference
sources:
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5"
synthesized_date: "2026-04-09"
completeness: high
---

# Мемпул

*Теги: неподтверждённые транзакции, рынок комиссий, майнинг*

---

## Определение

**Мемпул** (memory pool) — это хранилище **неподтверждённых транзакций**, о которых узел узнал из сети. **Майнеры** выбирают транзакции из мемпула при сборке кандидата в блок — обычно с приоритетом по **удельной комиссии** (комиссия на единицу места в блоке).

Источники: `raw/Books/izobretaem-bitkoin/glava-5.md`, `raw/Books/Suverenitet-posredstvom-matematiki/chapter-5.md`

---

## Поведение при реорганизациях

Если блок **отвергнут** (победила другая ветка с большей работой), транзакции из отброшенного блока возвращаются в мемпул, **если остаются валидны** относительно новой лучшей цепи. Конфликтующие траты разрешаются правилами цепи и порядком включения.

Источник: `raw/Books/izobretaem-bitkoin/glava-5.md`

---

## Пока нет «времени» сети

Пока транзакция не попала в валидный блок, у сети нет такого же **консенсусного времени**, как у подтверждённой траты — порядок якорится в **блоках**, а не в одном только мемпуле.

---

## Источники

- [Изобретаем Биткоин — гл. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Суверенитет посредством математики — гл. 5](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5)

---

## Связанные термины

[[ru/glossary|Глоссарий]] | [[ru/concepts/mining|майнинг]] | [[ru/concepts/utxo|UTXO]] | [[ru/concepts/forks|реорганизация]] | [[ru/concepts/difficulty-adjustment|корректировка сложности]] | [[ru/concepts/bitcoin|Биткоин]]

## Связанные страницы

- [[ru/concepts/mining]] — сбор блока из мемпула
- [[ru/concepts/utxo]] — что майнеры проверяют во входах/выходах
- [[ru/concepts/forks]] — устаревшие блоки и возврат в мемпул
- [[ru/concepts/scarcity]] — дефицит места в блоке
- [[ru/concepts/lightning-network]] — снижение конкуренции за место в мемпуле
