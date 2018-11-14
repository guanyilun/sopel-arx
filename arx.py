"""Arxiv module for Sopel

Add a simple wrapper around python arxiv api wrapper
and allows sopel bot to search on arxiv
"""

import arxiv
from sopel import module
from dateutil import parser
import shlex

@module.commands('arx')
def arxiv_handler(bot, trigger):
    query = trigger.group(2)
    if not query:
        print_usage(bot)

    else:
        keywords = shlex.split(query)
        
        if len(keywords) < 2:
            print_usage(bot)
        else:
            if keywords[0] == 'search':
                search_query = ' '.join(keywords[1:])
                results = arxiv.query(search_query=search_query)
                print_search_results(bot, results)
            elif keywords[0] == 'id':
                id_list = keywords[1:]
                results = arxiv.query(id_list=id_list)
                print_search_results(bot, results)
            elif keywords[0] == 'help':
                print_usage(bot)

            else:
                bot.say('Unrecognized commands')
                print_usage(bot)


def print_usage(bot):
    bot.say('Usage: ')
    bot.say('  arx search SEARCH_TERM')
    bot.say('  arx id SEARCH_IDS')
    bot.say('  arx help')

def print_search_results(bot, records):
    for record in records:
        updated = record['updated']
        updated_date = parser.parse(updated)
        updated_date_str = updated_date.strftime('%Y-%m-%d')
        outlines = "[arx] [%s] %s -- %s" % (updated_date_str, \
                                      record['title'], \
                                      record['id'])
        bot.say(outlines)
