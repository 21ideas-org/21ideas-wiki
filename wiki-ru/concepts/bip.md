---
title: "BIP (Bitcoin Improvement Proposal)"
category: concepts
tags: [bitcoin, wiki, protocol, governance, upgrades]
language: ru
quality: reference
sources:
  - "https://21ideas.org/izobretaem-bitkoin/glava-8"
  - "https://21ideas.org/vojna-za-razmer-bloka/"
synthesized_date: "2026-04-09"
completeness: high
---

# BIP (Bitcoin Improvement Proposal)

*Теги: стандарты, активация софтфорков*

---

## Что такое BIP

Изменения в **Bitcoin Core** и экосистеме проходят открытый процесс; в «Изобретаем Биткоин» названы **Bitcoin Improvement Proposals (BIP)** как формат предложений — с **публичным ревью**, видимым кодом и обсуждением.

BIP — это **документ дизайна**, а не закон: **узлы сами выбирают**, какое ПО запускать; **экономические участники** решают, что считать «биткоином».

Источник: `raw/Books/izobretaem-bitkoin/glava-8.md`

---

## Активация на практике (примеры из «войны за размер блока»)

В источниках описаны **пороги сигнализации майнеров** (например **95%** блоков за период сложности) для ряда софтфорков до **SegWit** — **BIP 66**, **BIP 65**, пакет **BIP 68 / 112 / 113** — и отмечено, что **ошибочная сигнализация** (без фактического соблюдения правил) вызывала кратковременные **разрывы цепи**, пока сеть не сошлась.

Политика активации **SegWit** привела к **BIP 148** (UASF) как давлению со стороны пользователей — спорно из-за риска **расхождения консенсуса**, если бы майнеры не сотрудничали.

Источники: `raw/Books/vojna-za-razmer-bloka/glava-5.md`, `raw/Books/vojna-za-razmer-bloka/glava-17.md`

---

## Связь с форками

**Софтфорки** часто описываются и внедряются через BIP; **хардфорки** тоже могут идти как реализации клиентов (эпоха **BIP 101** / Bitcoin XT), но требуют **обновления всех** желающих остаться в одной цепи — иначе появляются два актива.

См. [[ru/concepts/forks]] и [[ru/concepts/governance]].

---

## Источники

- [Изобретаем Биткоин — гл. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [Война за размер блока (хаб книги)](https://21ideas.org/vojna-za-razmer-bloka/)

---

## Связанные термины

[[ru/glossary|Глоссарий]] | [[ru/concepts/governance|управление]] | [[ru/concepts/forks|форки]] | [[ru/concepts/segwit|SegWit]] | [[ru/concepts/taproot|Taproot]]

## Связанные страницы

- [[ru/concepts/governance]] — кто принимает смену правил
- [[ru/concepts/forks]] — софтфорк и хардфорк
- [[ru/history/blocksize-war]] — политический контекст дебатов вокруг BIP
- [[ru/concepts/segwit]] — крупное обновление той эпохи
- [[ru/concepts/taproot]] — последующий софтфорк
