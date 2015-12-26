# -*- coding: utf-8 -*-
# Copyright (c) 2015 Spotify AB

from __future__ import absolute_import, division, print_function
import re

import inflect

__all__ = ["pluralize", "singularize"]

#####
# Tag functions to manipulate <<parameters>> from
# traits & resource types
#####

p = inflect.engine()


def pluralize(input_str):
    return p.plural(input_str)


def singularize(input_str):
    return p.singular_noun(input_str)
