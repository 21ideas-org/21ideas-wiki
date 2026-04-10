---
title: "Блокчейн (Биткоин)"
category: "concepts"
quality: "reference"
sources:
  - "https://21ideas.org/start/start"
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8"
synthesized_date: "2026-04-10"
completeness: "high"
language: "ru"
tags: [bitcoin, wiki, concept, protocol, security, mining, decentralization]
reviewed: "2026-04-10"
---

**Блокчейн** — **[[ru/glossary#Реестр (Ledger)|реестр]]**: **линейная цепь [[ru/glossary#Блок|блоков]]** от **[[ru/glossary#Генезис-блок|генезис-блока]]** до актуальной вершины, каждый блок фиксирует **[[ru/glossary#Транзакция|транзакции]]** и ссылается на **хэш предыдущего**. Связь делает историю **чувствительной к изменениям**: правка старой транзакции меняет хэш её блока и **ломает** все последующие; требует пересчёта всей последующей **работы [[ru/concepts/proof-of-work|PoW]]**.

В [пятой главе книги Яна Прицкера «Изобретаем Биткоин»](https://21ideas.org/izobretaem-bitkoin/glava-5) и в [вводном материале «Что такое Биткоин?»](https://21ideas.org/start/start) подчёркивается: термином *Блокчейн* часто **злоупотребляют в маркетинге**; в [[ru/concepts/bitcoin|Биткоине]] это просто **структура данных**, упорядочивающая эмиссию и траты.

---

## Консенсус и копии

Тысячи участников хранят **идентичные копии**, синхронизируемые протоколом. **Алгоритм [[ru/glossary#Консенсус Накамото|консенсуса]]** сравнивает **работу**; новому [[ru/concepts/bitcoin-node|узлу]] достаточно одного **честного** пира с цепью **наибольшей работы**, если его не **изолировали** от честной сети.

Основа: [Что такое Биткоин? (теоретический гид)](https://21ideas.org/start/start); [Изобретаем Биткоин — глава 5](https://21ideas.org/izobretaem-bitkoin/glava-5).

---

## Скептическая рамка из того же корпуса

«Суверенитет посредством математики»: важное изобретение — **правила консенсуса Биткоина, решающие [[ru/concepts/byzantine-generals-problem|задачу византийских генералов]]**; **«блокчейн»** без этих правил часто — **хайп**.

Основа: [Суверенитет посредством математики — глава 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8).

---

## Источники

- [Что такое Биткоин? (теоретический гид)](https://21ideas.org/start/start)
- [Изобретаем Биткоин — гл. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Суверенитет посредством математики — гл. 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8)

---

## Дополнительные материалы

- [[ru/glossary|Глоссарий]]
- [[ru/concepts/bitcoin|Биткоин: место блокчейна в системе]]
- [[ru/concepts/mining|Майнинг: как появляются новые блоки]]
- [[ru/concepts/proof-of-work|Proof of Work]]
- [[ru/concepts/utxo|UTXO]]
- [[ru/concepts/double-spend|Двойная трата и порядок транзакций]]
- [[ru/concepts/forks|Форки и реорганизации цепи]]
- [[ru/concepts/mempool|Мемпул: транзакции до включения в блок]]
- [[ru/concepts/governance|Управление сетью и валидация блоков]]
