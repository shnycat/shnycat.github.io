#!/usr/bin/env bash
f="$1"

sed -i 's/\\\[/$$/g;s/\\\]/$$/g' "$f" &&
	sed -i 's/\\(/$/g;s/\\)/$/g' "$f" &&

echo done
