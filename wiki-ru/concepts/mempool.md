---
title: "Мемпул"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/izobretaem-bitkoin/glava-5", "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5"]
synthesized_date: "2026-04-09"
completeness: "medium"
language: "ru"
tags: [bitcoin, wiki, concept, protocol, mining]
reviewed: "2026-04-10"
---

## Определение

**Мемпул** (memory pool) — это хранилище **неподтверждённых [[ru/glossary#Транзакция|транзакций]]**, о которых узел узнал из сети. **[[ru/glossary#Майнер|Майнеры]]** выбирают транзакции из мемпула при сборке кандидата в блок — обычно с приоритетом по **удельной комиссии** ([[ru/glossary#Комиссия (Transaction Fee)|комиссия]] на единицу места в блоке).

Основа: [Изобретаем Биткоин — глава 5](https://21ideas.org/izobretaem-bitkoin/glava-5); [Суверенитет посредством математики — глава 5](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5).

## Поведение при реорганизациях

Если [[wiki-ru/glossary#Блок|блок]] **отвергнут** (победила другая ветка с большей работой), транзакции из отброшенного блока возвращаются в мемпул, **если остаются валидны** относительно новой цепи с большей проделанной работой. Конфликтующие траты разрешаются правилами цепи и порядком включения.

Основа: [Изобретаем Биткоин — глава 5](https://21ideas.org/izobretaem-bitkoin/glava-5).

## Источники

- [Изобретаем Биткоин — глава 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Суверенитет посредством математики — глава 5](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5)

## Дополнительные материалы

- [[ru/concepts/mining|Майнинг]] 
- [[ru/concepts/utxo|UTXO]] 
- [[ru/concepts/forks|Форки]] 
- [[ru/concepts/scarcity|Редкость]] 
- [[ru/concepts/lightning-network|Lightning Network]] 