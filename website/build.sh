#!/bin/bash

./obsidian-to-docusaurus.py
git add ./docs ./public
git commit -m "update docs"
git push
