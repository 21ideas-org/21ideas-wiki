---
title: "BIP (Bitcoin Improvement Proposal)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/izobretaem-bitkoin/glava-8", "https://21ideas.org/vojna-za-razmer-bloka/", "https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch05_wallets.adoc", "https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki", "https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki", "https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "ru"
tags: [bitcoin, wiki, concept, protocol, governance, bip]
updated: "2026-08-01"
reviewed: "2026-08-01"
---

## Что такое BIP

Изменения в **[[ru/concepts/bitcoin-core|Bitcoin Core]]** и экосистеме проходят открытый процесс; в «Изобретаем Биткоин» [названы](https://21ideas.org/izobretaem-bitkoin/glava-8) **Bitcoin Improvement Proposals (BIP)** как формат предложений — с **публичным ревью**, видимым кодом и обсуждением.

BIP — это **документ дизайна**, а не закон: **[[ru/glossary#Нода (Узел)|узлы]] сами выбирают**, какое ПО запускать; **экономические участники** решают, что считать «биткоином».

## Активация на практике: примеры из «войны за размер блока»

В источниках описаны **пороги сигнализации майнеров** (например **95%** блоков за период сложности) для ряда софтфорков до **[[ru/concepts/segwit|SegWit]]** — **BIP 66**, **BIP 65**, пакет **BIP 68 / 112 / 113** — и отмечено, что **ошибочная сигнализация** (без фактического соблюдения правил) вызывала кратковременные **разрывы цепи**, пока сеть не сошлась обратно.

Политика активации **SegWit** привела к **BIP 148** (UASF) как давлению со стороны пользователей — спорно из-за риска **расхождения консенсуса**, если бы майнеры отказались сотрудничать.

## Стандарты кошельков

Не всякий BIP касается правил консенсуса. Значительная часть — это **стандарты совместимости**: они ничего не меняют в протоколе, но описывают, как программам договариваться между собой, чтобы сид-фраза, созданная в одном кошельке, открывалась в другом. Узлы за соблюдением таких стандартов не следят; следит только практика.

| BIP | Что задаёт |
| --- | --- |
| BIP-32 | иерархически детерминированные кошельки: дерево ключей из одного сида |
| BIP-39 | представление сида человекочитаемыми словами и вывод сида через PBKDF2 |
| BIP-43 | первый закалённый уровень как «назначение» дерева |
| BIP-44 | пятиуровневая структура `m/purpose'/coin_type'/account'/change/address_index` |
| BIP-49 | схема деривации для P2WPKH, вложенного в P2SH |
| BIP-84 | схема деривации для нативного SegWit (P2WPKH) |
| BIP-86 | схема деривации для Taproot с одним ключом (P2TR) |
| BIP-174 | частично подписанные транзакции (PSBT) |
| BIP-380…386, 389 | дескрипторы выходных скриптов |

Показательна судьба BIP-49, BIP-84 и BIP-86: каждый из них меняет ровно одно число — значение `purpose'` — и на этом всё. Разработчики сознательно сделали их несовместимыми с предшественниками, рассуждая так: пусть несовместимый кошелёк не найдёт счёт вовсе, чем найдёт частично и молча потеряет часть средств. Отказ должен быть заметным.

Подробный разбор — на странице [[ru/concepts/hd-wallets|HD-кошельки: BIP-32 и пути деривации]].

## Связь с форками

**[[ru/glossary#Софтфорк (Soft Fork)|Софтфорки]]** часто описываются и внедряются через BIP; **[[ru/glossary#Хардфорк|хардфорки]]** тоже могут идти как реализации клиентов (эпоха **BIP 101** / Bitcoin XT), но требуют **обновления всех** желающих остаться в одной цепи — иначе появляются два актива.

## Источники

- [Изобретаем Биткоин — гл. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [Война за размер блока. Глава 5: SegWit](https://21ideas.org/vojna-za-razmer-bloka/glava-5/)
- [Война за размер блока. Глава 17: UASF – Активируемый пользователями софтфорк](https://21ideas.org/vojna-za-razmer-bloka/glava-17/)
- [Mastering Bitcoin, 3rd edition — Chapter 5: Wallet Recovery](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch05_wallets.adoc) (CC BY-SA 4.0)
- [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki), [BIP-84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki), [BIP-86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki)

## Дополнительные материалы

- [[ru/concepts/hd-wallets|HD-кошельки: BIP-32 и пути деривации]]
- [[ru/concepts/seed-phrase|Сид-фраза и BIP-39]]
- [[ru/concepts/governance|Кто принимает смену правил]]
- [[ru/concepts/forks|Софтфорк и хардфорк]]
- [[ru/history/blocksize-war|Политический контекст дебатов вокруг BIP]]
- [[ru/concepts/segwit|Крупное обновление той эпохи]]
- [[ru/concepts/taproot|Последующий софтфорк]]
