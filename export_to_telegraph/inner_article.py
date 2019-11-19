#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .common import _seemsValidText

def _seemsValidRawArticle(soup):
	if not _seemsValidText(soup):
		return False
	return not not soup.find('img')

def _getInnerArticle_(soup):	
	applicators = [
		lambda x: x.find("article"),
		lambda x: x.find("div", {"id" : "js_content"}),
		lambda x: x.find("div", class_ = "story-body__inner"),
		lambda x: x.find("div", class_ = "answercell"),
		lambda x: x.find("div", class_ = "post-text"),
		lambda x: x.find("div", {"id" : "bodyContent"}),
		lambda x: x.find("div", {"id" : "content_JS"}),
	]
	for applicator in applicators:
		candidate = applicator(soup)
		if _seemsValidRawArticle(candidate):
			soup = candidate
	return soup

def _getInnerArticle(soup):
	all_content = str(soup)
	inner = _getInnerArticle_(soup)
	index = all_content.find(str(inner))
	if index == -1:
		return inner, None
	return inner, all_content[:index]