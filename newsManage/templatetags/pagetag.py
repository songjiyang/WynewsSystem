#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from django import template
register = template.Library()


from django.utils.html import format_html


@register.simple_tag
def circle_page(curr_page,loop_page,date,xx):
    offset = abs(curr_page - loop_page)
    if offset < 4:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="/newsManage/archive?page=%s&date=%s&type=%s">%s</a></li>'%(loop_page,date,xx,loop_page)
        else:
            page_ele = '<li><a href="/newsManage/archive?page=%s&date=%s&type=%s">%s</a></li>'%(loop_page,date,xx,loop_page)
        return format_html(page_ele)
    else:
        return ''