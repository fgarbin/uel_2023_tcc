import sqlparse

# Split a string containing two SQL statements:
raw = 'select * from foo; select * from bar;'
statements = sqlparse.split(raw)
statements

# Format the first statement and print it out:
first = statements[0]
print(sqlparse.format(first, reindent=True, keyword_case='upper'))

# Parsing a SQL statement:
parsed = sqlparse.parse('select * from foo')[0]
parsed.tokens
print(type(parsed))
token = parsed.token_first()
print(type(token))

import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML

def is_subselect(parsed):
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        if from_seen:
            if is_subselect(item):
                yield from extract_from_part(item)
            elif item.ttype is Keyword:
                return
            elif item.is_whitespace:
                continue 
            else:
                from_seen = False
                yield item
        elif item.ttype is Keyword and (item.value.upper() == 'FROM' or item.value.upper() == 'INNER JOIN' or item.value.upper() == 'LEFT JOIN'):
            from_seen = True


def extract_table_identifiers(token_stream):
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


def extract_tables(sql):
    stream = extract_from_part(sqlparse.parse(sql)[0])
    return list(extract_table_identifiers(stream))


if __name__ == '__main__':
    sql = """
    select K.a,K.b from (select H.b from (select G.c from (select F.d from
    (select E.e from A, B, C, D, E), F), G), H), I, J, K order by 1,2;
    """
    sql = 'select * from foo'
    parsed = sqlparse.parse(sql)

    print(sqlparse.format(sql, reindent=True, indent_width=2))
    tables = ', '.join(extract_tables(sql))
    print('Tables: {}'.format(tables))