# uel_ES2022_tcc
Artigo de conclusão para a Pós-Graduação em Engenharia de Software - ES2022

# Objetivo

Artigo de conclusão da Pós-Graduação em Engegnharia de Software - Universidade de Londrina (UEL)

O artigo realiza uma comparação ser  as ferramentas de IA, ChatGPT e Bard, podem ser funcionais para a melhoria de performance em querys existentes.

# Estrutura

* uel_ES2022_tcc
  * data
    * imdb
      * querys.csv: Arquivo com querys analisadas
      * IMDB_DER.png: Imagegm DER do dataset IMDB
      * qry??
        * qry??.sql: Query inicial da análise
        * qry??_explain_1.json: Resultado do comando EXPLAIN para a qry01.sql
        * qry??_explain_2_bard.json: Resultado do comando EXPLAIN para a qry??_bard.sql
        * qry??_explain_2_chatgpt.json: : Resultado do comando EXPLAIN para a qry??_ChatGPT.sql
        * qry??_Bard.pdf: Iteração com a ferramenta Bard
        * qry??_bard.sql: querys sugeridas pela ferramenta Bard
        * qry??_ChatGPT.pdf: Iteração com a ferramenta ChatGPT
        * qry??_question.txt: Iteração inicial com as ferramentas de IA
        * qry??_chatgpt.sql: querys sugeridas pela ferramenta ChatGPT
  * latex
  * sql_complexity_src
    * uel_load_data.py: Carrega os dados de querys a partir de um arquivo CSV.
    * uel_parser_query.py: Classe para realizar o parser e calcular a complexidade da query.
    * uel_process_data.py: Função que executa o processamento de parser e cálculo da complexidade.

 # Requisitos

 * Python 3.9 ou superior
   * SQL Parser: https://github.com/andialbrecht/sqlparse
 * PostgreSQL 15
 * ChatGPT
 * Bard

 # Referências:
  * IMDB Dataset: https://developer.imdb.com/non-commercial-datasets/
  * Ian Thomas (2023). The great sql bot bake off: Comparing the big llm beasts on sql code generation. https://www.linkedin.com/pulse/great-sql-bot-bake-off-comparing-big-llm-beasts-code-ian-thomas/
  * The PostgreSQL Global Development Group (n.d.). Explain, https://www.postgresql.org/docs/15/sql-explain.html
  * Chris Rickman, Nilesh Acharya (2023). Use natural language to execute sql queries. https://devblogs.microsoft.com/semantic-kernel/use-natural-language-to-execute-sql-queries/
  * Li, J., Hui, B., Qu, G., Li, B., Yang, J., Li, B., Wang, B., Qin, B., Cao, R., Geng, R.,
et al. (2023). Can llm already serve as a database interface. A big bench for large-scale
database grounded text-to-sqls. CoRR abs/2305.03111
  * Robinson, N., McIlraith, S., and Toman, D. (2014). Cost-based query optimization via ai
planning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 28.
  * Subali, M. A. P. and Rochimah, S. (2018). A new model for measuring the complexity of
sql commands. In 2018 10th International Conference on Information Technology and
Electrical Engineering (ICITEE), pages 1–5. IEEE
        