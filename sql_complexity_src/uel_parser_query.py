import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML

class SQLParser:
    def __init__(self, qry):
        self.query_in = qry
        self.sql_parsed = None
        self.sql_tables = None
        self.sql_outVars = None

    def parser(self):
        res = 0
        self.sql_parsed = sqlparse.parse(self.query_in)
        return res
    
    def is_subselect(self, item):
        if not item.is_group:
            return False
        for item in item.tokens:
            if item.ttype is DML and item.value.upper() == 'SELECT':
                return True
        return False

    def extract_out_part(self, sqlparsed):
        for item in sqlparsed.tokens:
            if item.ttype is Keyword and (item.value.upper() == 'FROM' or item.value.upper() == 'INNER JOIN' or item.value.upper() == 'LEFT JOIN'):
                break
            elif item.ttype is Keyword:
                return
            elif item.is_whitespace:
                continue 
            else:
                yield item

    def extract_from_part(self, sqlparsed):
        from_seen = False
        for item in sqlparsed.tokens:
            if from_seen:
                if self.is_subselect(item):
                    yield from self.extract_from_part(item)
                elif item.ttype is Keyword:
                    return
                elif item.is_whitespace:
                    continue 
                else:
                    from_seen = False
                    yield item
            elif item.ttype is Keyword and (item.value.upper() == 'FROM' or item.value.upper() == 'INNER JOIN' or item.value.upper() == 'LEFT JOIN'):
                from_seen = True

    def extract_field_identifiers(self, token_stream):
        for item in token_stream:
            if isinstance(item, IdentifierList):
                for identifier in item.get_identifiers():
                    yield identifier.get_name()
            elif isinstance(item, Identifier):
                yield item.get_name()
            elif isinstance(item, sqlparse.sql.Token) and item.value == '*':
                yield item.value
            # It's a bug to check for Keyword here, but in the example
            # above some tables names are identified as keywords...
            elif item.ttype is Keyword:
                yield item.value

    def extract_table_identifiers(self, token_stream):
        for item in token_stream:
            if isinstance(item, IdentifierList):
                for identifier in item.get_identifiers():
                    yield identifier.get_name()
            elif isinstance(item, Identifier):
                yield item.get_name()
            # It's a bug to check for Keyword here, but in the example
            # above some tables names are identified as keywords...
            elif item.ttype is Keyword:
                yield item.value


    def extract_tables(self):
        stream = self.extract_from_part(self.sql_parsed[0])
        self.sql_tables = list(self.extract_table_identifiers(stream))

    def extract_outputvars(self):
        stream = self.extract_out_part(self.sql_parsed[0])
        self.sql_outVars = list(self.extract_field_identifiers(stream))


    def getTables(self):
        self.extract_tables()
        return self.sql_tables
    
    def getOutPutVars(self):
        self.extract_outputvars()
        return self.sql_outVars

    def getJoinsQty(self):
        qtJoins = 0
        tokens =self.sql_parsed[0].tokens
        for item in tokens:
            if  item.is_keyword and 'JOIN' in item.normalized:
                qtJoins += 1
        return qtJoins
    
    def calcComplexity(self, qtdTables, qtdOutPutVars, qtdJoins):
        complex_amount = 0;
        complex_table = qtdTables * 0.3
        complex_outVars = qtdOutPutVars * 0.1
        complex_joins = qtdJoins * 0.25
        complex_amount = complex_table + complex_outVars + complex_joins
        
        return complex_amount



if __name__ == '__main__':
    sql = 'select * from foo, abc;'
    sql = 'SELECT INDICE,ORDEM,CHAVE,DESCRICAO,DESCSPA,DESCENG,F3,NICKNAME,SHOWPESQ FROM SIX010 WHERE  D_E_L_E_T_ = ' ' AND INDICE = ?'
    sql = "SELECT M_NAME,I_TABLES,I_TABLE_M FROM MPMENU_MENU MPN INNER JOIN MPMENU_ITEM MPI ON I_ID_MENU = M_ID AND MPI.D_E_L_E_T_ = ' ' LEFT JOIN MPMENU_FUNCTION MPF ON F_ID = I_ID_FUNC AND MPF.D_E_L_E_T_ = ' ' WHERE  M_ID = ? AND F_FUNCTION = ? AND MPN.D_E_L_E_T_ = ' '  ORDER BY  I_ORDER"
    oSQL = SQLParser(sql)
    oSQL.parser()

    qryTables = oSQL.getTables()
    qryOutVars = oSQL.getOutPutVars()
    qryQtJoins = oSQL.getJoinsQty()
    print(oSQL.calcComplexity(len(qryTables), len(qryOutVars), qryQtJoins))

#1 Variable Output 0,10 -> getOutPutVars
#2 Variable Input 0,15 
#3 Nested Query 0,20 
#4 Join Table 0,25 -> getJoinsQty
#5 Number of Table 0,30 -> getTables