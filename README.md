# # OCR Data Extraction ETL

Python ETL pipeline for extracting, cleaning, validating, and exporting data from scanned documents using OCR

> This project uses fictitious scanned documents created exclusively for OCR an ETL testing. No real client, company, or banking data is used.

Este projeto implementa um fluxo ETL em python para transformar documentos em dados estruturados.

A solução lê arquivos PDF ou imagem, aplica OCR, identifica tabelas, converte os dados extrídos em DataFrames, realiza etapas de limpeza e padronização com pandas e exporta o resultados final para Excel.

Como primeiro caso de uso, o projeto utiliza relatórios fictícios de conciliação bancária para testar a extração de tabelas em documentos escaneados. A arquitetura porém pode ser adaptada para outros tipos de documentos tabulares.

## Objetivo

Automatizar etapas manuais de extração e preparação de dados em documentos escaneados, reduzindo retrabalho e facilitando a análise, validação e uso dos dados em processos internos.

## Pipeline

```

`text
Documento escanedo
↓
OCR
↓
Extração de tabelas
↓
DataFrame brutos
↓
Tratamento com pandas
↓
Validação dos dados
↓
Exportação para Excel
```

## Status do projeto

Em desenvolvimento.

Etapas planejadas:

* [X] Definição da arquitetura ETL
* [X] Criação de documentos fictícios para teste
* [X] Extração de tabelas com OCR
* [X] Tratamento dos DataFrames com pandas
* [ ] Validação automática de colunas
* [ ] Exportação estruturada para Excel
* [ ] Documentação completa do fluxo
