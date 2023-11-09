#!/bin/bash

# title: copy_without_linebreaks
# author: Glutanimate (github.com/glutanimate)
# license: MIT license

# Parses currently selected text and removes 
# newlines that aren't preceded by a full stop

SelectedText="$(xsel)"

ModifiedText="$(echo "$SelectedText" | \
    sed 's/\.$/.|/g' | sed 's/^\s*$/|/g' | tr '\n' ' ' | tr '|' '\n')"

#   - first sed command: replace end-of-line full stops with '|' delimiter and keep original periods.
#   - second sed command: replace empty lines with same delimiter (e.g.
#     to separate text headings from text)
#   - subsequent tr commands: remove existing newlines; replace delimiter with
#     newlines
# This is less than elegant but it works.

echo "$ModifiedText" | xsel -bi