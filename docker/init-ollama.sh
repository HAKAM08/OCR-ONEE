#!/bin/sh

echo "Waiting for Ollama..."

until curl -s http://ollama:11434/api/tags >/dev/null
do
    sleep 2
done

echo "Downloading llama3.2:1b..."

ollama pull llama3.2:1b

echo "Done."