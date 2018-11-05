"""Arxiv module for Sopel

Add a simple wrapper around python arxiv api wrapper
and allows sopel bot to search on arxiv
"""

import arxiv
from sopel import module
from dateutil import parser

@module.commands('arx')
def arxiv_handler(bot, trigger):
    search_query = trigger.group(2)
    results = arxiv.query(search_query=search_query)
    print_search_results(bot, results)


def print_search_results(bot, records):
    for record in records:
        updated = record['updated']
        updated_date = parser.parse(updated)
        updated_date_str = updated_date.strftime('%Y-%m-%d')
        outlines = "[%s] %s -- %s" % (updated_date_str, \
                                      record['title'], \
                                      record['id'])
        bot.say(outlines)
