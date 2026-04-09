---
title: "Блокчейн (Биткоин)"
category: concepts
tags: [bitcoin, wiki, protocol, ledger, security]
language: ru
quality: reference
sources:
  - "https://21ideas.org/start/start"
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8"
synthesized_date: "2026-04-09"
completeness: high
---

# Блокчейн (Биткоин)

*Теги: реестр, цепь блоков, PoW, проверка*

---

## Что это в Биткоине

**Блокчейн** — **аппендиксный реестр**: **линейная цепь блоков** от **генезис-блока** до актуального конца, каждый блок фиксирует **транзакции** и ссылается на **хэш предыдущего**. Связь делает историю **изменочувствительной**: правка старой транзакции меняет хэш её блока и **ломает** все последующие, пока не пересчитана вся следующая **работа PoW**.

В «Изобретаем Биткоин» предупреждают: слово **злоупотребляют в маркетинге**; в Биткоине это просто **структура данных**, упорядочивающая эмиссию и траты.

Источники: `raw/Books/izobretaem-bitkoin/glava-5.md`, `raw/Start/start.md`

---

## Консенсус и копии

Тысячи участников хранят **идентичные копии**, синхронизируемые протоколом. **Алгоритм консенсуса** сравнивает **работу**; новому узлу достаточно одного **честного** пира с цепью **наибольшей работы**, если его не **изолировали** от честной сети.

Источники: `raw/Start/start.md`, `raw/Books/izobretaem-bitkoin/glava-5.md`

---

## Скептическая рамка из того же корпуса

«Суверенитет посредством математики»: важное изобретение — **правила консенсуса Биткоина, решающие задачу византийских генералов**; **«блокчейн»** без этих правил часто — **хайп**. См. [[ru/concepts/byzantine-generals-problem]].

Источник: `raw/Books/Suverenitet-posredstvom-matematiki/chapter-8.md`

---

## Источники

- [Что такое Биткоин? (теоретический гид)](https://21ideas.org/start/start)
- [Изобретаем Биткоин — гл. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Суверенитет посредством математики — гл. 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8)

---

## Связанные термины

[[ru/glossary|Глоссарий]] | [[ru/concepts/mining|майнинг]] | [[ru/concepts/proof-of-work|Proof of Work]] | [[ru/concepts/utxo|UTXO]] | [[ru/concepts/double-spend|двойная трата]] | [[ru/concepts/forks|форк / реорг]]

## Связанные страницы

- [[ru/concepts/bitcoin]] — место блокчейна в системе
- [[ru/concepts/mining]] — как появляются новые блоки
- [[ru/concepts/double-spend]] — что предотвращает порядок
- [[ru/concepts/forks]] — конкурирующие кончики и реорги
- [[ru/concepts/mempool]] — транзакции до включения
- [[ru/concepts/governance]] — кто валидирует блоки
